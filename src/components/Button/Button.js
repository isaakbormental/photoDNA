import React, { Component } from 'react';
import './Button.scss';

class Button extends Component {
    render() {
        const {
            onClick,
            notice,
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
                <span className="button__notice">{notice}</span>
            </button>
        );


    }
}

export default Button;