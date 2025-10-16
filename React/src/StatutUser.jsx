export default function StatutUser (props){
    let msg = "123"
    function f1 (){
        return msg ;
    }
    return <>
    <div className="StatutUser-div">
        <h1>Tableau de Statut Utilisateur</h1>
        <p>{msg = f1()}</p>
        <div className="StatutUser_btns">
            <button onChange={f1()}>Administrateur</button>
            <button>Modérateur</button>
            <button>Utilisateur</button>
            <button>Visiteur</button>
        </div>
        
    </div>


    </>
}