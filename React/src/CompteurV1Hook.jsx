import { useState } from "react";
export default function CompteurV1Hook (){
        const [cnt,setCnt] = useState(0) 
        const Increase = () => {
            setCnt(cnt+1)
        }
        const Decrease = ()=>{
            setCnt(cnt-1)
        }
        const Setzero =() => {
            setCnt(0)
        }
        let clr 
            if (cnt>0) {clr = "green"}
            else if (cnt<0) {clr  = "red"}
            else { clr = "black"}
        return (
            
            <div className="cntv1-div" >
                <hr />
                <h3 style={{color:clr}}>{cnt}</h3>
                <button onClick={Increase}>+</button>
                <button onClick={Decrease}>-</button>
                <button onClick={Setzero}>Set</button>
            </div>
        )
}