import React, { Component } from 'react';
import './Switcher.scss';


class Switcher extends Component {

    render() {
        let className = this.props.active ? 'switcher switcher_active' : 'switcher';
        return (
            <div
                className={className}
                onClick={this.props.onClick}
            />
        );
    }
}

export default Switcher;
