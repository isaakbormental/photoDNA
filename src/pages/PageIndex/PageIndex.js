import React, { Component } from 'react';
import './PageIndex.scss';

import iconNations from './img/icon-nations.svg'
import iconChart from './img/icon-chart.svg'
import iconPeople from './img/icon-people.png'
import Button from "../../components/Button/Button";


class PageIndex extends Component {
    constructor(props) {
        super(props);
        this.state = {
            list: [
                {
                    icon: iconNations,
                    text: <span>3&nbsp;dominant nationalities</span>
                },
                {
                    icon: iconChart,
                    text: <span>44&nbsp;facial features, it&rsquo;s national origin</span>
                },
                {
                    icon: iconPeople,
                    text: <span>Sex, age and sexual orientation</span>
                },
                {
                    text: <span className="page_index__link" onClick={() => this.props.switchPage('readme')} >Read more</span>
                }
            ]
        };
    }
    render() {
        return (
            <div className="page page_index">
                <h1 className="page_index__heading">DNA test by&nbsp;selfie</h1>
                <h2 className="page_index__subheading">Send a&nbsp;selfie and get result:</h2>
                <ul className="page_index__list">
                    {this.state.list.map((item, index) => {
                        return(
                            <li className="page_index__list-item" key={index}>
                                <span className="page_index__list-icon">{item.icon ? <img src={item.icon} alt=""/> : ''}</span>
                                <span className="page_index__list-text">{item.text}</span>
                            </li>
                        )
                    })}
                </ul>
                <Button
                    className="button page_index__button"
                    onClick={() => this.props.chooseImgFromApi()}
                >Try now</Button>
            </div>
        );

    }
}

export default PageIndex;
