import React, { Component } from 'react';
import './PageResult.scss';

import Button from "../../components/Button/Button";
import Preview from "../../components/Preview/Preview";
import BackArrow from "../../components/BackArrow/BackArrow";
import Chart from "../../components/Chart/Chart";


class PageResult extends Component {
    render() {
        return (
            <div className="page page_result">
                <Preview
                    img={this.props.img}
                    gender={this.props.data.gender}
                    age={this.props.data.age}
                    shareCountry={this.props.shareCountry}
                >
                    <BackArrow switchPage={(page) => this.props.switchPage(page)}/>
                </Preview>
                <div className="page_result__body">
                    <div className="page_result__charts">
                        {this.props.data.nationality.map((item) => {
                            return(
                                <div key={item.name}>
                                    <Chart data={item}/>
                                </div>
                            )
                        })}
                    </div>
                </div>
                <div className="page_result__bottom">
                    <div className="page_result__text">To get a full report</div>
                    <Button
                        className="button button_bottom page_result__button"
                        onClick={() => console.log('share')}
                    >Share</Button>
                </div>
            </div>
        );

    }
}

export default PageResult;
