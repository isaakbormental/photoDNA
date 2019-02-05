import React, { Component } from 'react';
import './PageLoading.scss';

import iconLoading from './img/loading.svg'

class PageLoading extends Component {
    constructor(props) {
        super(props);
        this.state = {
            status: {
                betaface: {
                    heading: 'Defining your second and third dominant nationality',
                    subheading: 'Doing science magic'
                },
                sharing: {
                    heading: 'DNA is being processed',
                    subheading: 'please wait'
                },
            }
        };
    }

    render() {
        const bg = {
            backgroundImage: `url(${this.props.img})`
        };
        return (
            <div className="page page_loading" style={bg}>
                <div className="page_loading__inner">
                    <img className="page_loading__icon" src={iconLoading} alt=""/>
                    <h1 className="page_loading__heading">{this.state.status[this.props.status].heading}</h1>
                    <h2 className="page_loading__subheading">{this.state.status[this.props.status].subheading}</h2>
                </div>
            </div>
        );

    }
}

export default PageLoading;
