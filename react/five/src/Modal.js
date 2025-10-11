import {useState} from 'react';
import './Modal.css';


function Modal(){
    let [open, setOpen] = useState(false)

    let image = 'https://i2.epscape.com/images/render/person%2F5ba061b52ae1d4488edcacb4d8bbebe8.jpg?width=400'

    return(
        <div>
            <img src={image} className='small' alt="" onClick={() => setOpen(true)} style={{display: open ? 'none' : 'block'}} />

            {open && (<div>
                <div>
                    <img src={image} className='big' alt="" onClick={() => setOpen(false)} />
                </div>
            </div>)}
            

        </div>
    )
}

export default Modal;