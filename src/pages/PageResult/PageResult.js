import React, { Component } from 'react';
import './PageResult.scss';

import Button from "../../components/Button/Button";
import Preview from "../../components/Preview/Preview";
import BackArrow from "../../components/BackArrow/BackArrow";
import Chart from "../../components/Chart/Chart";
import Switcher from "../../components/Switcher/Switcher";
import LineBar from "../../components/LineBar/LineBar";


class PageResult extends Component {
    render() {

        let linebars;
        if (this.props.shareOrientation) {
            linebars = <div className="page_result__linebars">
                <LineBar
                    progress={this.props.data.gay}
                    caption="Gay"
                />
                <LineBar
                    progress={this.props.data.straight}
                    caption="Straight"
                />
            </div>;
        }
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
                            let className = item.name === this.props.shareCountry.name ? 'page_result__chart page_result__chart_active' : 'page_result__chart';
                            return(
                                <div
                                    className={className} key={item.name}
                                    onClick={() => this.props.switchShareCountry(item)}
                                >
                                    <Chart data={item}/>
                                </div>
                            )
                        })}
                    </div>
                    <div className="page_result__orientation">
                        <Switcher
                            active={this.props.shareOrientation}
                            onClick={() => this.props.switchShareOrientation()}
                        />
                        <span
                            onClick={() => this.props.switchShareOrientation()}
                            className="page_result__orientation-text"
                        >Show sexual orientation</span>
                        {linebars}
                    </div>
                </div>
                <div className="page_result__bottom">
                    <div className="page_result__text">To get a full report</div>
                    <Button
                        className="button button_bottom page_result__button"
                        onClick={() => this.props.shareThroughApi()}
                    >Share</Button>
                </div>
            </div>
        );

    }
}

export default PageResult;
