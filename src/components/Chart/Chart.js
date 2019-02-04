import React, { Component } from 'react';
import './Chart.scss';


class Chart extends Component {
    constructor(props) {
        super(props);
        this.state = {
            color: this.props.color ? this.props.color : '#fff'
        };
    }


    render() {
        return (
            <div>
{/*                <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"
                     xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                     viewBox="0 0 127.6 127.6" style="enable-background:new 0 0 127.6 127.6;" xml:space="preserve">
<style type="text/css">
	.st0{fill:none;stroke:#E0E0E0;stroke-width:5;stroke-miterlimit:10;}
    .st1{fill:none;stroke:url(#SVGID_1_);stroke-width:5;stroke-linecap:round;stroke-dasharray:192,385;}
</style>
                    <circle className="st0" cx="63.8" cy="63.8" r="61.3"/>
                    <linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="-749.5452" y1="135.6067"
                                    x2="-621.9452" y2="135.6067"
                                    gradientTransform="matrix(6.123234e-17 -1 -1 -6.123234e-17 199.4067 -621.9452)">
	<stop offset="0" style="stop-color:#EE2A7B"/>
                        <stop offset="1" style="stop-color:#92278F"/>
</linearGradient>
                    <circle className="st1" cx="63.8" cy="63.8" r="61.3"/>
</svg>*/}

                {this.props.data.name}
                {this.props.data.confidence}
            </div>
        );
    }
}

export default Chart;
