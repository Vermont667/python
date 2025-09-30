import React from "react";

class Dz extends React.Component{
    state = {val: 270}


    range = (event) => {
        this.setState({val: event.target.value})
    }


    render(){
        return(
            <>
            <input type="range" onChange={this.range} min='50' max='500' step='10' />
            <p>{this.state.val} x {this.state.val}</p>
             
            <div style={{width: this.state.val + 'px', height: this.state.val + 'px', background: 'blue'}}></div>
        
            </>
        )
    }
}

export default Dz;