import P from "./P";


function Purch({ per, onClick, invites }) {
    return (
        <>
            <div className="a">
                {per.map(a => (
                    <div key={a.id}>
                    <P  {...a} onClick={onClick} isInvited={invites.includes(a.id)} /></div>
                ))}
            </div>
        </>
    )
}

export default Purch;
