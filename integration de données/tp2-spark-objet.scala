var rddPers = sc.textFile ("chein-vers-le-fichier/Personnel2.csv")
var ligne1Entete = rddPers.first
var rddPers2 = rddPers.filter (ligne => ligne != ligne1Entete)

def transformPersToObj (p : String): Personne = {    
    return Personne (p.split(";")(0).toInt, p.split(";")(1), p.split(";")(2));
}

var rddObjP = rddPers2.map (chP => transformPersToObj(chP))

rddObjP.map (p => p.prenom.toUpperCase).collect.foreach(println)
