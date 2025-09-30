import React from "react";

class Range extends React.Component{
    state = {val: 0}

    range = (event) => {
        this.setState({val: event.target.value})
    }

    render(){
        return(
            <>
            <hr />
            <input type="range" onChange={this.range} min='-100' max='100' step='10' />
            <p>{this.state.val}</p>
            </>
        )
    }
}

export default Range;