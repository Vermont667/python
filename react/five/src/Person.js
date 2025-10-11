import {useState} from 'react';

function Person(){
    let [person, setPerson] = useState({
        'firstname': 'Igor',
        'lastname': 'Petrov'
    });

    function rename(){
        // setPerson({firstname: 'Sergey', lastname: person.lastname});
        setPerson({...person, firstname: 'Sergey'});
    }


    return(
        <div>
            <p>{person.firstname} {person.lastname}</p>
            <button onClick={rename}>Rename</button>
        </div>
    )
}


export default Person;