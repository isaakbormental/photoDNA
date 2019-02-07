import React, { Component } from 'react';
import './PageReadme.scss';

import Button from "../../components/Button/Button";
import BackArrow from "../../components/BackArrow/BackArrow";


class PageReadme extends Component {
    render() {
        return (
            <div className="page page_readme">
                <BackArrow
                    switchPage={(page) => this.props.switchPage(page)}
                />
                <div className="page_readme__inner">
                    <h1  className="page_readme__heading">How we do it</h1>
                    <h2 className="page_readme__subheading">Machine learning will help to&nbsp;find more about yourself.</h2>
                    <p className="page_readme__text">Our technology will compare your features with a&nbsp;database of&nbsp;43&nbsp; nationalities. Then it&rsquo;ll identify similarities and show which 3&nbsp;nationality you remind the most.</p>
                    <p className="page_readme__bold-text">Unlike a&nbsp;DNA-test it&rsquo;s free</p>
                    <p className="page_readme__bold-text">Which nationalities do&nbsp;you look like?</p>
                </div>
                <Button
                    className="button page_readme__button"
                    onClick={() => this.props.chooseImgFromApi()}
                >Try now</Button>
            </div>
        );

    }
}

export default PageReadme;
