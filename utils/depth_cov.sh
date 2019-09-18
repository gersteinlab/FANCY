####
samtools depth <bam file> | awk '{if ($3>0) {print $0}}' > depth.txt
a=($(awk '{ sum += $3; n++ } END { if (n > 0) print sum / n; }' depth.txt))
b=($(wc -l depth.txt))
echo $a $b > depthANDcov.txt
#####

