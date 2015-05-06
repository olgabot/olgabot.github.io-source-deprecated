Title: IGV: Null pointer exceptions, invalid GZIP header, invalid BZIP header
Date: 2015-05-06 15:04
Modified: 2015-05-06 15:04
Category: bioinformatics
Tags: bioinformatics, samtools, igv, java
Slug: igv-java-lang-nullpointerexception
Authors: Olga Botvinnik
Summary: If you've run into a `java.lang.NullPointerException` or "Invalid Gzip Header" or some complaint about bzip while using the Integrative Genomics Viewer, then you've run into the same problem as me. Turns out I had too many index (`*.bai`) files that had similar naming to my `*.bam` files, and IGV assigned the wrong ones as the index, so whenever I tried to view reads from those samples, the index pointed to the wrong location in the bam, and one of those many errors would happen. So the solution is simple (and relatively fast): use `samtools index` on your bam files!

If you've run into a `java.lang.NullPointerException` or "Invalid Gzip Header" or some complaint about bzip while using the Integrative Genomics Viewer, then you've run into the same problem as me. Turns out I had too many index (`*.bai`) files that had similar naming to my `*.bam` files, and IGV assigned the wrong ones as the index, so whenever I tried to view reads from those samples, the index pointed to the wrong location in the bam, and one of those many errors would happen. So the solution is simple (and relatively fast): use `samtools index` on your bam files!