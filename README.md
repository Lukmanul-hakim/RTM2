# RTM2 - Batch Processing Pipeline

## Deskripsi
Tugas implementasi pipeline batch menggunakan:
- Hadoop MapReduce (Streaming Python)
- Apache Spark (PySpark + MLlib)

## Dataset
Heart Disease Dataset

## Struktur Project
- MapReduceHeart/
  - mapper & reducer (Python)
  - run.sh
  - results/ (output)
- PysparkHeart/
  - pyspark notebook (EDA + ML)

## Hasil MapReduce
- Count:
  - 0 = 499
  - 1 = 526
- Average Age:
  - 0 = 56.56
  - 1 = 52.40

## Hasil Spark
- Random Forest Accuracy: 94%
- Precision:0.943
- Recall:0.941
- F1-score:0.941

## Perbandingan
- Hadoop MapReduce: berbasis disk → lebih lambat
- Spark: in-memory → lebih cepat

## Kesimpulan
Spark lebih unggul dalam performa, sedangkan MapReduce lebih sederhana untuk batch processing skala besar.
