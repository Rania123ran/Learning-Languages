import Avert from "./Avert.jsx" 
import Taches from "./Tache.jsx"
import Counter from "./Counter.jsx"
import BoutonBascule from "./BoutonBascule.jsx"
import States from "./States.jsx"
import CompteurV1Hook from "./CompteurV1Hook.jsx"
import CompteurV1Class from "./CompteurV1Class.jsx"
import CrudYT from ".//CrudYT.jsx"
import "./style.css"
import { Component } from "react"
import App1Tp3 from "./App1Tp3.jsx"
export default  function App() {
   const age = 17
  const isconnect = true 
  const isGreen =true
  return <>
  <App1Tp3/>
  <hr></hr>
  <Formulaire/>
<hr></hr>
    <Forms/>
    <hr/>
    <CrudYT/><hr/><div className="app-div1">
    <CompteurV1Hook/>
     <CompteurV1Class/>

    </div> 

    <States/>
    <BoutonBascule/> 
    <Counter/>  
    <Taches tab ={["Faire les courses",
                  "Terminer le projet React" , 
                  "Envoyer le rapport", 
                  "Prendre rendez-vous"]}/>
    <Avert msg="Attention : Vous Avez des mises à jour en Attente"/>
  <Avert msg ="Erreur : Impossible de charger les données ."/>
    <Job salary={9000} position="Senior SDE" company="Google"/>
  <Job salary={1200} position="Junior SDE" company="Amazon"/> 
  <div style={{backgroundColor : "red",padding:"20px",width:"100px"}}>Styles</div> 
  {<h3 style={{color : isGreen ? "green":"red"}}>This has Color</h3>} 
  {isGreen && <button>Click me ! </button>}
    {age >=18 ? <h4 style={{color:"green"}}>Over Age</h4> : <h4 style={{color:"red"}}> Under Age</h4> }
    {isconnect ? "True" : "False "}
  </>
}
const Job = (props) => {
  return <>
  <div>
    <h5>Salary : {props.salary} position : {props.position} company : {props.company} </h5>
  </div>
  </>
}
class Forms extends Component {
  constructor (props) {
    super(props)
    this.state =  {
      personne : ""}}
  per = (event) => {
      this.setState({personne:event.target.value})
  }
  addPers = (event) => {
      event.preventDefault() ; 
  }
  render(){
    return <>
    <div>
      <form onSubmit={this.addPers}>
        <h1>Bonjour {this.state.personne}</h1>
        <input onChange={this.per}></input> (classe)

      </form>
    </div>
    </>
  }
}
class Formulaire extends Component {
  constructor (props){
    super(props)
    this.state = {
        nom : "" , prenom : "" , email : "" ,sub:false
    }
  }
  addnom = (event) => {this.setState({nom : event.target.value})}
  addprenom = (event) => {this.setState({prenom : event.target.value})}
  addemail = (event) => {this.setState({email : event.target.value})}
  handleform = (event) =>{event.preventDefault() 
    this.setState({sub : true})
  }
  render(){
    return<>
  <div className="div-formulaire">
  <form onSubmit={this.handleform}>
    <div className="form-row">
      <label>Prénom : </label>
      <input onChange={this.addnom} />
    </div>
    <div className="form-row">
      <label>Nom :</label>
      <input onChange={this.addprenom} />
    </div>
    <div className="form-row">
      <label>Email :</label>
      <input onChange={this.addemail} />
    </div>
    <button type="submit">Envoyer</button>
  </form>
</div>

   {this.state.sub && <div className="div2">
          <h3>Résumé des informations</h3>
          <p>Prenom : {this.state.prenom} ,Nom : {this.state.nom} , Email : {this.state.email}</p>
        </div>}
    </>
  }
}

