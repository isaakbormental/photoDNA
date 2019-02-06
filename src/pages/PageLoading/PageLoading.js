import React, { Component } from 'react';
import './PageLoading.scss';

import iconLoading from './img/loading.svg'

class PageLoading extends Component {
    constructor(props) {
        super(props);
        this.state = {
            status: {
                betaface: {
                    headings: [
                        'Analyzing your photo',
                        'Defining your features',
                        'Comparing your features to nationaly database',
                        'Defining your second and third dominant nationality',
                        'Preparing a report...'
                    ],
                    subheading: 'Doing science magic'
                },
                sharing: {
                    headings: [
                        'Posting your genes'
                    ],
                    subheading: 'please wait'
                },
            },
            statusSlide: -1
        };
    }

    componentDidMount() {
        this.tick();
    }

    componentWillUnmount() {
        clearTimeout(this.timer);
    }

    tick() {
        if(this.state.statusSlide+1 < this.state.status[this.props.status].headings.length) {
            this.setState({
                statusSlide: this.state.statusSlide+1
            });
            this.timer = setTimeout(() => this.tick(), 2000)
        }

    }

    render() {
        const bg = {
            backgroundImage: `url(${this.props.img}), linear-gradient(153.87deg, #6C23C8 -2.21%, #0D40C5 -2.2%, #EF59B3 106.38%)`
        },
            headings = this.state.status[this.props.status].headings;
        return (
            <div className="page page_loading" style={bg}>
                <img className="page_loading__icon" src={iconLoading} alt=""/>
                <div className="page_loading__heading-wrapper">
                    <h1
                        className="page_loading__heading"
                        style={{
                            width:headings.length*100+'%',
                            right:this.state.statusSlide*100+'vw'
                        }}>
                        {headings.map((item, index) => {
                            return(
                                <span className="page_loading__heading-item" key={index}>
                                    <span className="page_loading__heading-inner">{item}</span>
                                </span>
                            )
                        })}
                    </h1>
                </div>
                <h2 className="page_loading__subheading">{this.state.status[this.props.status].subheading}</h2>
            </div>
        );

    }
}

export default PageLoading;
