import { Component } from "react";

export default class App1Tp3 extends Component {
    constructor(props){
        super(props)
        this.state = {
                langues : ["Python","JS","Java","C++","Ruby","PHP","C#","TypeScript","Swift","Go"] ,
                langue : ""
        }
    }
    handleInput = (event)=>{
            this.setState({langue : event.target.value})
    
    }
    render(){
        const filtred = this.state.langues.filter(e=>e.toLowerCase().includes(this.state.langue.toLowerCase()))
        return <>
        
        <div className="languages">
            <h1>Liste des Langages</h1>
            <h3>Recherche :</h3>
            
            <input type="text" placeholder="Recherchez un langages"  onChange={this.handleInput}/>
            <div>
            {filtred.map(e=>{return <p>{e}</p>})}
            </div>
           
        </div>
        </>
    }




}