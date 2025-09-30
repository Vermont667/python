import './Search.css';
import React from 'react';

class Search extends React.Component {
    state = {
        search: ''
    }

    render() {
        return (
            <>
                <div className="search">
                    <input
                        type="search"
                        placeholder='search'
                        value={this.state.search}
                        onChange={(e) => this.setState({search: e.target.value})}
                    />
                </div>
            </>
        )
    }
}

export default Search;