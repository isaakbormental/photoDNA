import React, { Component } from 'react';
import './Button.scss';

class Button extends Component {
    render() {
        const {
            onClick,
            className = 'button',
            children,
        } = this.props;

        return (
            <button
                onClick={onClick}
                className={className}
                type="button"
            >
                {children}
            </button>
        );


    }
}

export default Button;