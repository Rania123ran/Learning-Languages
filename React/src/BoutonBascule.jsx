import { Component } from "react"

export default class BoutonBascule extends Component{
    constructor(props){
            super(props);
            this.state = {
                etat  : 1 , 
                msg : "Allumé"
            }
    }
    change = () => {
            this.setState({etat:!this.state.etat,msg : this.state.etat?"Eteint":"Allumé"}) }
           
      
    render(){
        return <>
        <hr />
        <div className="BtnBascule-div">
            <h1>Bienvenue dans l'application Bouton Bascule</h1>
                <button className={this.state.msg} onClick={this.change}>{this.state.msg}</button>
        </div>
        </>
    }
}
