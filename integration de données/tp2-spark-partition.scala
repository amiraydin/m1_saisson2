// préparer la clé de partitionnement
var rddKV = rddV.map (v => (v.split (" ")(1), v))

// Partitionnement pas hashage de la clé
import org.apache.spark.HashPartitioner

rddKV.partitionBy(new HashPartitioner(3)).glom().collect()

// Partitionnement pas intervalle de valeurs de la clé
import org.apache.spark.RangePartitioner
rddKV.partitionBy (new RangePartitioner (2, rddKV)).glom().collect()