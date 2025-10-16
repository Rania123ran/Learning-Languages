import { Component } from "react";

export default class Test1 extends Component {
        constructor(props){
            super(props)
            this.state = {
                modules : [
                {name : "Dev" , intra : this.randomnote(), test: this.randomnote() , final : this.randomnote(),  moyenne : null } , 
                 {name : "IA" , intra : this.randomnote(), test: this.randomnote() , final : this.randomnote() ,  moyenne : null } , 
                {name : "BD" , intra : this.randomnote(), test: this.randomnote() , final : this.randomnote(),  moyenne : null} ]
                
            }
        }
        randomnote = ()=>{return Math.floor(Math.random()*21)}
        moyennne = () => {let newmodules = this.state.modules.map(module=>{return module.moyenne = module.intra*0.3 + module.final*0.5 + module.test*0.2})
    }
        calculer =()=> {this.setState({})}
        render(){
            return <>
            <table className="test1-table">
                <thead>
                    <tr>
                    <td>Module</td>
                    <td>Intra (30%)</td>
                    <td>Test (20%)</td>
                    <td>Final (50%)</td>
                    <td>Moyenne</td>
                </tr>
                </thead>
                <tbody>
                    {this.state.modules.map((e,index) =>{
                        return (<tr key={index}>
                            <td>{e.name}</td>
                            <td>{e.intra}</td>
                            <td>{e.test}</td>
                            <td>{e.final}</td>
                            <td>{e.moyenne}</td>
                        </tr>)
                    
                })}
                </tbody>    
            </table>
            <button onClick={this.calculer}>Calculer Moyenne</button>
            </>
        }
}