import React, { Component } from 'react';
import './PageReport.scss';

import Button from "../../components/Button/Button";
import BackArrow from "../../components/BackArrow/BackArrow";
import Chart from "../../components/Chart/Chart";
import LineBar from "../../components/LineBar/LineBar";
import Feature from "../../components/Feature/Feature";

import shareIcon from "./img/share.svg"


class PageReport extends Component {
    constructor(props) {
        super(props);
        this.state = {
            locked: true
        };
    }
    render() {
        const pageClass = "page page_report page_report_" + this.props.version;
        let age = this.props.data.age;
        let gender = this.props.data.gender;
        let ageEl = age ? <span className="page_report__age">Age <span className="page_report__age-num">{age}</span></span> : '';
        let genderEl = gender ? <span className={"page_report__gender page_report__gender_"+gender}>Sex</span> : '';
        const getColor = (i) => {
            const colors = [
                '#fff',
                '#fff',
                '#fff'
            ];
            i = i - Math.floor(i/colors.length)*colors.length;
            return colors[i];
        };

        let blur = !this.state.locked ? '' : <div className="page_report__blur">
            <Button
                className="button  page_report__blur-btn"
                onClick={() => this.setState({locked:false})}
            >SHOW FULL REPORT</Button>
        </div>;

        return (
            <div className="page_report__wrapper">
                <img
                    className="page_report__share-icon"
                    src={shareIcon}
                    onClick={() => this.props.shareThroughApi()}
                    alt=""/>
                {blur}
                <div className={pageClass}>
                    <h1 className="page_report__heading">Full report</h1>
                    <div className="page_report__demography">
                        {genderEl}
                        {ageEl}
                    </div>
                    <div className="page_report__orientation">
                        <LineBar
                            progress={this.props.data.gay}
                            caption="Gay"
                        />
                        <LineBar
                            progress={this.props.data.straight}
                            caption="Straight"
                        />
                    </div>
                    <div className="page_report__features">
                        {this.props.data["facial features"].map((item, index) => {

                            const key = Object.keys(item)[0];
                            let data = item[key];
                            data.type = key;

                            return(<Feature data={data} color={getColor(index)} key={key}/>)
                        })}
                    </div>

                    <div className="page_report__charts">
                        {this.props.data.nationality.map((item) => {
                            return(<div className="page_report__chart" key={item.name}><Chart data={item}/></div>)
                        })}
                    </div>

                    <BackArrow
                        switchPage={() => this.props.switchPage('results')}
                    />
                    <Button
                        className="button button_with-gradient page_report__button"
                        onClick={() => this.props.chooseImgFromApi()}
                    >Try again</Button>
                </div>
            </div>
        );

    }
}

export default PageReport;
