import { Component } from "react"

export default class CompteurV2Class extends Component{
        constructor(props){
            super(props)
           this.state = {
            cnt : 0 , 
            liste : [0]
           }
        }
       
        render(){
            return <>
            <div>
                <button onClick={this.inc}>+</button>
               
            </div>
            </>
        }



}