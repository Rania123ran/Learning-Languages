
export default function Tache(props){
    return <>
    <hr />
    <div className="Taches-div" >
        <h1>Liste des Tâches</h1>
        {props.tab.map((e,index)=> 
        <p key={index.toString()}>{e}</p>)}
    </div>
    </>
} 