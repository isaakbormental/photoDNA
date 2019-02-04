import React, { Component } from 'react';
import './PageLoading.scss';

import iconLoading from './img/loading.svg'

class PageLoading extends Component {
    render() {
        const bg = {
            backgroundImage: `url(${this.props.img})`
        };
        return (
            <div className="page page_loading" style={bg}>
                <div className="page_loading__inner">
                    <img className="page_loading__icon" src={iconLoading} alt=""/>
                    <h1 className="page_loading__heading">Defining your second and third dominant nationality</h1>
                    <h2 className="page_loading__subheading">Doing science magic</h2>
                </div>
            </div>
        );

    }
}

export default PageLoading;
