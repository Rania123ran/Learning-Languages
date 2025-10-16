import { Component } from "react";
export default class CompteurV1Class extends Component{
       constructor(props){
        super(props)
        this.state = { cnt : 0 }
       }
        Increase = () => {this.setState({cnt : this.state.cnt +1 })}
        Decrease = ()=>{this.setState({cnt : this.state.cnt -1}) }
        Setzero =() => { this.setState({cnt : 0 ,}) } 
        clr = ()=>{
            if(this.state.cnt <0) return "red"
            else if (this.state.cnt>0) return "green"
            else return "black"
        }
          
           render(){
              return (
                
                
            <div className="cntv1-div" >
                <hr />
                <h3 style={{color:this.clr()}}>{this.state.cnt}</h3>
                <button onClick={this.Increase}>+</button>
                <button onClick={this.Decrease}>-</button>
                <button onClick={this.Setzero}>Set</button>
            </div>
        )
           }
      
}