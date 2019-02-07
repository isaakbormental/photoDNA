import React, { Component } from 'react';
import './Preview.scss';
import Flag from "../Flag/Flag";


class Preview extends Component {
    render() {
        let {
            imgUrl,
            gender,
            age,
            shareCountry,
            children
        } = this.props;
        let bg = imgUrl ? {backgroundImage: `url(${imgUrl})`} : {};
        let ageEl = age ? <span className="preview__age">Age <span className="preview__age-num">{age}</span></span> : '';
        let genderEl = gender ? <span className={"preview__gender preview__gender_"+gender}>Sex</span> : '';
        let flag = shareCountry ? <Flag className="preview__flag" shareCountry={shareCountry}/> : '';

        return (
            <div className="preview" style={bg}>
                <div className="preview__inner">
                    {children}
                    {genderEl}
                    {ageEl}
                    {flag}
                </div>
            </div>
        );
    }
}

export default Preview;
