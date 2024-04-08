var listeNb = (0 to 10).toList
var rddNb = sc.parallelize (listeNb)
rddNb.getNumPartitions
rddNb.glom.collect
rddNb.collect.foreach (e => println(e))

def fMultiplier (nb : Int, facteur : Double) : Double = {
	return nb * facteur;
}
var rddNbMultiplie = rddNb.map (e => fMultiplier (e, 100))
def fSeuilMin (nb : Int, seuilMin : Int) : Boolean = {
	if (nb >= seuilMin)
		return true;
	else
		return false;
}
var rddSup7 = rddNb.filter (e => fSeuilMin(e, 7))