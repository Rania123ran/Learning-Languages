import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-etudiant',
  templateUrl: './etudiant.component.html',
  styleUrls: ['./etudiant.component.css']
})
export class EtudiantComponent {
  nomEtud : string = "Iyad"
  reponseEtud : number | null = null 
  @Output() reponseEtudiant : EventEmitter<number> = new EventEmitter<number> 
  EnvoyerReponse(){
    if(this.reponseEtud !== null){
      this.reponseEtudiant.emit(this.reponseEtud)
    }
  }
  

}
