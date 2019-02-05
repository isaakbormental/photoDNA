import React, { Component } from 'react';
import './Chart.scss';


class Chart extends Component {
    render() {
        let dashArray = 385*(this.props.data.confidence/100) + ", 385";
        return (
            <div className="chart">
                <svg className="chart__img" version="1.1" x="0px" y="0px" viewBox="0 0 127.6 127.6">
                    <defs>
                        <linearGradient
                            id="gradient"
                            x1="-749.5452"
                            y1="135.6067"
                            x2="-621.9452"
                            gradientUnits="userSpaceOnUse"
                            gradientTransform="matrix(6.123234e-17 -1 -1 -6.123234e-17 199.4067 -621.9452)"
                        >
                            <stop  offset="0" stopColor="#EE2A7B"/>
                            <stop  offset="1" stopColor="#92278F"/>
                        </linearGradient>
                    </defs>
                    <circle className="chart__bg-circle" cx="63.8" cy="63.8" r="61.3"/>
                    <circle
                        className="chart__color-circle"
                        cx="63.8"
                        cy="63.8"
                        r="61.3"
                        stroke="url(#gradient)"
                        strokeDasharray={dashArray}
                    />
                </svg>

                <div className="chart__inner">
                    <span className="chart__percent">{this.props.data.confidence}</span>
                    <span className="chart__name">{this.props.data.name}</span>
                </div>
            </div>
        );
    }
}

export default Chart;
