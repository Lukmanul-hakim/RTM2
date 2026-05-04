#!/bin/bash

mkdir -p results

# CLEAN OUTPUT
hdfs dfs -rm -r -f /output/count
hdfs dfs -rm -r -f /output/avg

echo "Running COUNT..."

time hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
-files mapper.py,reducer.py \
-input /input/heart.csv \
-output /output/count \
-mapper "python3 mapper.py" \
-reducer "python3 reducer.py" 2>&1 | tee results/log_count.txt

# AMBIL OUTPUT DARI HDFS
hdfs dfs -cat /output/count/part-00000 > results/count.txt


echo "Running AVG..."

time hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
-files mapper_avg.py,reducer_avg.py \
-input /input/heart.csv \
-output /output/avg \
-mapper "python3 mapper_avg.py" \
-reducer "python3 reducer_avg.py" 2>&1 | tee results/log_avg.txt

# AMBIL OUTPUT
hdfs dfs -cat /output/avg/part-00000 > results/avg.txt

# SYNC KE WINDOWS (opsional)
cp -r results /mnt/d/Lukman\ S2/Semester\ 2/IT\ PLATFORM\ AND\ INFRASTRUCTURE/Tugas/RTM\ 2/mapreduceheart/