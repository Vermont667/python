import { useState } from "react";
import Purch from "./Purch";


function Home(){

    let per = [{'id': 1, 'name': 'Apple'}, {'id': 2, 'name': 'Banana'}, {'id': 3, 'name': 'Tea'}, {'id': 4, 'name': 'Coffee'}];

    let [invites, setInvites] = useState([])

    let onClick = (id) => {
        if(invites.includes(id)){
            setInvites(prev => prev.filter(ch => ch !== id))
        } else {
            setInvites(prev => [...prev, id])
        }
    }

    return(
        <div>
           <h2>Home Page</h2> 

           <h3>Shopping list:</h3>
           <Purch per={per} invites={invites} onClick={onClick} />
            <hr />
            <h3>Total completed: {invites.length}</h3>
        </div>
    )
}

export default Home;
