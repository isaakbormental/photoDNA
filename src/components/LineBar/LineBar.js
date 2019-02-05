import React, { Component } from 'react';
import './LineBar.scss';


class LineBar extends Component {
    render() {
        const progress = Math.round(this.props.progress)+"%";
        return (
            <div className="linebar">
                <div className="linebar__caption">{this.props.caption} {progress}</div>
                <div className="linebar__line"
                    style={{width: progress}}
                />
            </div>
        );
    }
}

export default LineBar;
