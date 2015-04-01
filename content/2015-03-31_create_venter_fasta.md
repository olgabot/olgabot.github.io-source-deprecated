Title: How to create a custom genome fasta from a vcf file
Date: 2015-04-01 11:08
Modified: 015-04-01 11:08
Category: bioinformatics
Tags: bioinformatics, genomics, ensembl
Slug: how-to-create-a-custom-genome-fasta-from-a-vcf-file
Authors: Olga Botvinnik
Summary: Short version for index and feeds

I've tried to create a custom genome for the J. Craig Venter genome several times using `vcf-consensus` and other tools and they have never worked. Finally, I've gotten something to work, and hopefuly this helps you too! This is a log of all the steps I had to take to create a new reference genome. This requires a few tools:

1. [samtools](http://samtools.sourceforge.net/)
2. [vcftools](http://vcftools.sourceforge.net/index.html)
3. [PicardTools](http://broadinstitute.github.io/picard/)
4. [GATK](https://www.broadinstitute.org/gatk/)

Lucky for me, I already all of these tools installed on our server, but this may not be the case for you. I'm not the expert on installing these things, for the most part they were installed by other lab members. If you need help with these tools, I suggest searching on [biostars.org](https://www.biostars.org/) and [seqanswers.com](http://seqanswers.com/) for advice.

Let's get started. The goal is to be able to run [`FastaAlternativeReferenceMaker`](https://www.broadinstitute.org/gatk/gatkdocs/org_broadinstitute_gatk_tools_walkers_fasta_FastaAlternateReferenceMaker.php) from GATK, which requires:

1. Properly prepared reference fasta (we'll see what *"properly prepared"* means in a bit)
2. Karyotypically sorted "variant call format" (`vcf`) file for the new genome.

First, we need to obtain and decompress human genome assembly. I like to keep my directories organized like the original source, so we'll move to the `/projects/ps-yeolab/genomes/ensembl/v75/fasta/homo_sapiens/dna/` first. Notice we do this for-loop, that's because GATK is extremely strict and requires your reference genome to be in karyotypic order (e.g. `1, 2, 3, ...`) not lexicographical order (e.g. `1, 10, 11, 12, ...`), and in the exact same order as the VCF, which is sorted in this way. Also, we want to make sure not to download any of the haplotypes or unassembled contigs, e.g. `GL000246.1`. Also, notice that the chromosomes are numbered ENSEMBL-style, as `1`, `2`, `3`... rather than UCSC-style with `chr` prepended, as `chr1`, `chr2`, `chr3`, ... Just something to keep in mind in case you need to do this for other genomes, there could be other caveats.

	cd /projects/ps-yeolab/genomes/ensembl/v75/fasta/homo_sapiens/dna/
	for C in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 MT X Y
	do
		curl "ftp://ftp.ensembl.org/pub/release-75/fasta/homo_sapiens/dna/Homo_sapiens.GRCh37.75.dna.chromosome.${C}.fa.gz" |\
			gunzip -c >> Homo_sapiens.GRCh37.75.fa
	done

Next, obtain and decompress Venter vcf file. Again, we'll do this in the corresponding directory on our server, which matches the folder layout of the ENSEMBL ftp site.

	cd /projects/ps-yeolab/genomes/ensembl/v75/variation/vcf/homo_sapiens/
	wget ftp://ftp.ensembl.org/pub/release-75/variation/vcf/homo_sapiens/Venter.vcf.gz
	gunzip Venter.vcf.gz

This VCF file is in lexicographically sorted order, so we will use [`vcf-sort`](http://vcftools.sourceforge.net/perl_module.html#vcf-sort) from `vcftools` to sort the genome karyotypically, aka in chromosomal order.
	
	cat Venter.vcf | vcf-sort --chromosomal-order > Venter.sorted.vcf

Now we need to follow the instructions provided on the [GATK forums](http://gatkforums.broadinstitute.org/discussion/1601/how-can-i-prepare-a-fasta-file-to-use-as-reference) about how to prepare a fasta file as a reference.

Now that we have a properly ordered genome, we will build an index of it using [`samtools`](http://samtools.sourceforge.net/). I'm specifying a specific `samtools`, because the bleeding edge version doesn't work on our server and we have to use version `0.1.19`.

	/projects/ps-yeolab/software/samtools-0.1.19_built_by_hand/samtools faidx Homo_sapiens.GRCh37.75.fa

Create a sequence dictionary of the genome using [PicardTools](http://broadinstitute.github.io/picard/). Our `PicardTools` are located in `/projects/ps-yeolab/software/picard-tools-1.93/`, yours are probably somewhere else. I'm using the full path to be illustrative of the many components of bioinformatics :)

	java -jar /projects/ps-yeolab/software/picard-tools-1.93/CreateSequenceDictionary.jar R=Homo_sapiens.GRCh37.75.fa O=Homo_sapiens.GRCh37.75.dict

Now we are ready to run the `FastaAlternativeReferenceMaker` command. My compiled `GATK` distribution is in `~/workspace-git/gatk/dist`, and again, yours is probably somewhere else. I've separated this out onto several lines so it's easier to read.

	 java -Xmx2g -jar ~/workspace-git/gatk/dist/GenomeAnalysisTK.jar \
	 	-R /projects/ps-yeolab/genomes/ensembl/v75/fasta/homo_sapiens/dna/Homo_sapiens.GRCh37.75.fa  \
	 	-T FastaAlternateReferenceMaker \
	 	-o /projects/ps-yeolab/genomes/ensembl/v75/fasta/homo_sapiens/dna/Venter.fasta \
	 	--variant /projects/ps-yeolab/genomes/ensembl/v75/variation/vcf/homo_sapiens/Venter.sorted.vcf 