import React, { Component } from 'react';
import './PageResult.scss';

import Button from "../../components/Button/Button";
import Preview from "../../components/Preview/Preview";
import BackArrow from "../../components/BackArrow/BackArrow";
import Chart from "../../components/Chart/Chart";
import Switcher from "../../components/Switcher/Switcher";
import LineBar from "../../components/LineBar/LineBar";

import Post from "../../components/Post/Post";


class PageResult extends Component {
    constructor(props) {
        super(props);
        this.state = {
            generateImg: false
        };
    }

    render() {

        let linebars = this.props.shareOrientation ? "page_result__linebars" : "page_result__linebars page_result__linebars_hidden";
        return (
            <div className="page page_result">
                {/*<Post
                    ref={ref => (this.child = ref)}
                    imgUrl={this.props.imgUrl}
                    data={this.props.data}
                    shareOrientation={this.props.shareOrientation}
                    shareCountry={this.props.shareCountry}
                    switchTestImg={(testImg) => this.props.switchTestImg(testImg)}
                    shareThroughApi={() => this.props.shareThroughApi()}
                />*/}
                <Preview
                    imgUrl={this.props.imgUrl}
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
                        <div className={linebars}>
                            <LineBar
                                progress={this.props.data.gay}
                                caption="Gay"
                            />
                            <LineBar
                                progress={this.props.data.straight}
                                caption="Straight"
                            />
                        </div>
                    </div>
                </div>
                <Button
                    className="button button_with-gradient page_result__button"
                    // onClick={() => this.child.makeImg()}
                    onClick={() => this.props.shareThroughApi()}
                    notice="to get a full report"
                >Share</Button>
            </div>
        );

    }
}

export default PageResult;
