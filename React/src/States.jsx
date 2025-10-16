import { useState } from "react";
export default function States (){
const [age,setAge] = useState(0);
const [input,setinput] = useState("")
const [text,setText] = useState(true)
const increaseAge = () => {
   setAge(age+1)
}
const decreaseAge = () => {
    setAge(age-1)
}
const handleinput  = (event) => {
    setinput(event.target.value)
}
const ShowHide = () => {
    setText(!text)
}
return <>
<hr />
<h3>HOOK 1</h3>
{age>0 && <button onClick={decreaseAge}>Decrease Age</button>}
{age}
<button onClick={increaseAge}>Increase Age</button><br />
<h3>HOOK 2</h3>
<h4>{input}</h4>
<input type="Text" onChange={handleinput}></input>(function)
<h3>HOOK 3</h3>
<button onClick={ShowHide}>Show / Hide </button>
    {text ? "My name is Rania" : ""}
</>
}
