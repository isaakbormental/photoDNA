import React, { Component } from 'react';
import './Preview.scss';
import Flag from "../Flag/Flag";


class Preview extends Component {
    render() {
        const {
            img,
            gender,
            age,
            shareCountry,
            children
        } = this.props;
        const bg = img ? {backgroundImage: `url(${img})`} : {};
        const ageEl = age ? <span className="preview__age">Age <span className="preview__age-num">{age}</span></span> : '';
        const genderEl = gender ? <span className={"preview__gender preview__gender_"+gender}>Sex</span> : '';
        const flag = shareCountry ? <Flag className="preview__flag" shareCountry={shareCountry}/> : '';

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
