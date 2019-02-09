import React, { Component } from 'react';
import './Post.scss';
import domtoimage from 'dom-to-image';

import photolabIcon from './img/photolab.jpg'


import Chart from "../../components/Chart/Chart";
import Flag from "../Flag/Flag";


class Post extends Component {

    makeImg() {
        const node = document.querySelector('.post__inner');

        domtoimage.toJpeg(node)
            .then((dataUrl) => {
                this.props.switchTestImg(dataUrl);
                console.log(dataUrl);
                this.props.shareThroughApi();
            })
            .catch(function (error) {
                console.error('oops, something went wrong!', error);
            });
    }

    componentDidUpdate(prevProps, prevState) {
        /*if(this.props.generateImg) {
            this.makeImg();
        }*/
        /*if (prevProps.shareCountry !== this.props.shareCountry || prevProps.shareOrientation !== this.props.shareOrientation) {
            this.makeImg();
        }*/
    }

    render() {
        let additionalList = this.props.data.nationality.filter((item) => {
            return item.name !== this.props.shareCountry.name;
        });
        additionalList.sort((a, b) => b.confidence - a.confidence);
        additionalList[0].relativePercent = 100;
        additionalList[1].relativePercent = (additionalList[1].confidence / additionalList[0].confidence * 100).toFixed(2);

        const publishingType = this.props.shareOrientation ? 'post__databox' : 'post__databox no-orientation';
        const sexClass = "post__databox-accent post__sex post__sex_"+this.props.data.gender;


        return (
            <div className="post">
                <div className="post__inner">
                    <div className="post__left" style={{backgroundImage:`URL("${this.props.imgUrl}")`}}>
                        <Flag shareCountry={this.props.shareCountry} className="post__flag"/>
                    </div>
                    <div className="post__right">
                        <img className="post__photolab-icon" src={photolabIcon} alt=""/>
                        <Chart data={this.props.shareCountry}/>
                        <div className="post__heading">DNA test by&nbsp;selfie</div>
                        <div className="post__linebars">
                            <div className="post__linebar">
                                {additionalList.map((item) => {
                                    return (
                                        <div className="post__line" key={item.name} style={{width:item.relativePercent+"%"}}>
                                            <div className="post__nationality">{item.name}</div>
                                            <div className="post__percent">{item.confidence.toFixed(0)+"%"}</div>
                                        </div>
                                    )
                                })}
                            </div>
                        </div>
                        <div className={publishingType}>
                            <div className="post__databox-accent post__straight">
                                <div className="post__databox-caption">Straight:</div>
                                {this.props.data.straight+"%"}
                            </div>
                            <div className="post__databox-accent post__gay">
                                <div className="post__databox-caption">Gay:</div>
                                {this.props.data.gay+"%"}
                            </div>
                            <div className="post__databox-accent post__age">
                                <div className="post__databox-caption">Age</div>
                                {this.props.data.age}
                            </div>
                            <div className={sexClass}>
                                <div className="post__databox-accent post__databox-caption">Sex</div>
                            </div>
                        </div>

                        <div className="post__button">Free now</div>

                    </div>
                </div>
            </div>
        );

    }
}

export default Post;
