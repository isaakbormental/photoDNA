import React, { Component } from 'react';
import './PageError.scss';

import Button from "../../components/Button/Button";
import Preview from "../../components/Preview/Preview";


class PageError extends Component {
    render() {
        return (
            <div className="page page_error">
                <Preview imgUrl={this.props.imgUrl}/>
                <div className="page_error__inner">
                    <div className="page_error__emotion">:-(</div>
                    <div className="page_error__text">We&nbsp;didn&rsquo;t find a&nbsp;face on&nbsp;this photo</div>
                    <Button
                        className="button page_error__button"
                        onClick={() => this.props.chooseImgFromApi()}
                    >Try again</Button>
                </div>
            </div>
        );

    }
}

export default PageError;
