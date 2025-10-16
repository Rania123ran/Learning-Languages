import { useState } from "react"
export default function CrudYT (){
   const [TodoList,setTodoList] = useState([])
   const [newtask,setTask] = useState("")
   const handleInput = (event) => {
         setTask(event.target.value)}
    const addTask = () => {
        const value = {
            id : TodoList.length === 0 ? 1 : TodoList[TodoList.length -1].id +1 ,
            name : newtask, 
            completed : false
        }
        setTodoList([...TodoList,value])
    }
    const deleteTask =(id) => {
        setTodoList(TodoList.filter(val=>val.id !== id))
    }
    const completed = (val) => {
            setTodoList(TodoList.map((e)=> {if(e.id === val) {return {...e, completed : !e.completed}}else {return e} }))
            
    }
    return <>
    <div>
        <input type="text" style={{padding:"10px" ,margin :"10px"}} placeholder="add new task" onChange={handleInput}/>
        <button style={{padding:"10px"}} onClick={addTask}>Add Task</button>
    </div>
    <div >
        {
            TodoList.map((task)=> {return <div style={{ marginLeft: "10px",
                display: "flex",
                alignItems: "center",
                gap: "10px",
                backgroundColor: task.completed  ? "green" : "transparent", width:"400px", borderRadius:"20px"}}><h4>{task.name}</h4> <button style={{backgroundColor:"red" ,
                border : "1px solid red" , padding : "10px" , borderRadius : "10px" ,color:"white"}} onClick={() => deleteTask(task.id)}>X</button>
                <button  style={{backgroundColor:"yellow" ,
                border : "1px solid yellow" , padding : "10px" , borderRadius : "10px" ,color:"black"}} onClick={() => completed(task.id)}>Done</button></div>})
        }
    </div>
    </>
}