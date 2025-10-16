import { Component } from "react";
import "./style.css"
export default class Counter extends Component {
        constructor(props){
            super(props); 
            this.state = {count : 0}
        }
        inct = () => {
            this.setState({count : this.state.count +1})
        }
        render(){
            return <>
            <hr />
            <h1 className="Cnt-h1">Compteur :</h1>
                <div className="Cnt-div">
                    <p>{this.state.count}</p>
                    <button onClick={this.inct}>+</button>
                    </div>
            
            </>
        }
}