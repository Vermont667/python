import './Albom.css'

function Albom(props) {
    let { music } = props;
    return (
        <div className="a">

            {
                Object.keys(music).map((elem, index) => {
                    return (
                        <div key={index} className='c'>
                            <div>
                                {music[elem].name}
                            </div>
                        </div>
                    )
                })
            }
        </div>
    )
}

export default Albom;