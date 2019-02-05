import React, { Component } from 'react';
import './BackArrow.scss';


class BackArrow extends Component {
    constructor(props) {
        super(props);
        this.state = {
            color: this.props.color ? this.props.color : '#fff'
        };
    }


    render() {
        return (
            <button className="back-arrow" onClick={() => this.props.switchPage('default')}>
                <svg width="12" height="21" viewBox="0 0 12 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M3.66908 10.3465L11.5623 2.48538C12.1352 1.91488 12.1528 0.96406 11.5682 0.402344C11.0013 -0.141819 10.1024 -0.133042 9.54423 0.422823L0.555247 9.37518C0.508246 9.41028 0.464182 9.44832 0.423056 9.48928C0.138111 9.77306 -0.00289261 10.1475 4.49629e-05 10.5162C-0.00289261 10.8877 0.138111 11.2593 0.423056 11.5431C0.464182 11.584 0.508246 11.622 0.555247 11.6572L9.49723 20.5627C10.0701 21.1332 11.0248 21.1507 11.5888 20.5685C12.1352 20.0039 12.1264 19.1087 11.5682 18.5528L3.66908 10.6888C3.57508 10.5952 3.57508 10.4401 3.66908 10.3465Z" fill={this.state.color}/>
                </svg>
            </button>
        );
    }
}

export default BackArrow;