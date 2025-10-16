class Personne{
  double poids ;
  double taille ;
  Personne({required this.poids,required this.taille,});

  Calculer (){
    double tailleEnMetres = taille / 100;
    return poids / (tailleEnMetres * tailleEnMetres);
  }
  getMessage (double imc){
    if(imc <18.6) return "Poids trés bas"  ;
    else if(imc <24.9) return "Poids idéal" ;
    else if(imc <29.9) return "Surpoids" ;
    else if(imc <34.9) return "Obésité grade 1" ;
    else if(imc <39.9) return "Obésité grade 2" ;
    else return "Obésité grade 2" ;
  }
}