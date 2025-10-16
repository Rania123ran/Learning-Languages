import { Component } from '@angular/core';

@Component({
  selector: 'app-enseignant',
  templateUrl: './enseignant.component.html',
  styleUrls: ['./enseignant.component.css']
})
export class EnseignantComponent {
  nomEns : string ="X"
  question : string ="Combien de types de classes on peut avoir dans un composant Angular ?"
  reponse : number = 3 
  checkAnswer = false
  reponseEt : number | null = null 
  RecevoirReponse(rep : number){
    this.reponseEt = rep
    this.checkAnswer = (this.reponse === this.reponseEt)
  }
  
}
