import React from "react";

class Test extends React.Component{

    constructor(props){
        console.clear();
        super(props);
        console.log('Constructor');
        this.state = {
            s1: 0
        }
        
    }


    buttonHandel = () => {
        console.log('Work');
        let val = this.state.s1;
        val++;
        this.setState({s1:val})
        
    }


    render(){
        console.log('Render');
        
        return(
            <>
                {
                    console.log('return')
                }
                <div>
                    <button onClick={this.buttonHandel}>Push</button>
                </div>
                <div>
                    {
                        this.state.s1
                    }
                </div>
            </>
        )
    }
}

export default Test;