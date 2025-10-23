
function P({ id, name, onClick, isInvited }) {
    return (
        <div className="a" style={{width: '200px', margin: '0 auto'}}>
            <div className="b" style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                width: '100%'
            }}>
                <label htmlFor={id} style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }}>
                    <input 
                        type="checkbox" 
                        id={id} 
                        onClick={() => onClick(id)} 
                    />
                    <span>{name}</span>
                </label>
                <div className="button">
                    <b>{isInvited ? '+' : '-'}</b>
                </div>
            </div>
        </div>
    )
}

export default P;