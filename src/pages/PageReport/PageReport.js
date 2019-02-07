import React, { Component } from 'react';
import './PageReport.scss';

import Button from "../../components/Button/Button";
import BackArrow from "../../components/BackArrow/BackArrow";
import Chart from "../../components/Chart/Chart";
import LineBar from "../../components/LineBar/LineBar";
import Feature from "../../components/Feature/Feature";


class PageReport extends Component {
    render() {
        let age = this.props.data.age;
        let gender = this.props.data.gender;
        let ageEl = age ? <span className="page_report__age">Age <span className="page_report__age-num">{age}</span></span> : '';
        let genderEl = gender ? <span className={"page_report__gender page_report__gender_"+gender}>Sex</span> : '';
        const getColor = (i) => {
            const colors = [
                '#EE74AC',
                '#828282',
                '#85A7D9'
            ];
            i = i - Math.floor(i/colors.length)*colors.length;
            return colors[i];
        };

        return (
            <div className="page page_report">
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

                <div className="page_report__read-more" onClick={() => {this.props.switchPage('readme', 'report')}}>Read more</div>

                <BackArrow
                    switchPage={() => this.props.switchPage('results')}
                    color="#828282"
                />
                <Button
                    className="button button_with-gradient page_report__button"
                    onClick={() => this.props.chooseImgFromApi()}
                >Share</Button>
            </div>
        );

    }
}

export default PageReport;
