import React, { Component } from 'react';
import './App.scss';
import PageIndex from "./pages/PageIndex/PageIndex";
import PageReadme from "./pages/PageReadme/PageReadme";
import PageError from "./pages/PageError/PageError";
import PageLoading from "./pages/PageLoading/PageLoading";
import PageResult from "./pages/PageResult/PageResult";
import PageReport from "./pages/PageReport/PageReport";


const getVersion = () => {
    const versions = [
        'one',
        'two'
    ];
    const random = Math.floor(Math.random() * versions.length);
    return versions[random];
};

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            appEnv: !'production',
            version: getVersion(),
            page: 'default',
            backPage: '',
            imgUrl: '',
            loadingStatus: '',
            shareCountry: '',
            shareOrientation: true,
            testImg: '',
            shareImg: '',
            shareTitle: 'Learn more about yourself',
            shareDescription: 'Machine leaning will tell your origin',
            shareLpTitle: 'One more step to learn about yourself',
            shareLpDescription: 'Our technology is integrated into Photo Lab app. Download it to learn your dominant nationalities and try out numerous photo filters and effects'
        };
    }

    chooseImgFromApi() {
        // TODO: pick right method (see callback API)
        if (this.state.appEnv === 'production') {
            window.location.href = "callback:nativePhotoSelect?func=appUploaded";
        } else {
            window.appUploaded(false);
        }
    }
    shareThroughApi() {
        // TODO: pick right method (see callback API)
        if (this.state.appEnv === 'production') {
            this.setState({loadingStatus:'sharing'});
            this.switchPage("loading");
            fetch('/amazgen',{
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    imgUrl: this.state.imgUrl,
                    testImg: this.state.testImg,
                    data: this.state.data,
                    shareOrientation: this.state.shareOrientation,
                    shareCountry: this.state.shareCountry
                })
            }).then((response) => {
                if (!response.ok) {
                    throw Error(response.statusText);
                }
                return response.json();
            }).then((response) => {
                this.switchPage('report');
                this.setState({shareImg:response.link});
                window.location.href = `callback:nativeShare?og_image=${encodeURIComponent(this.state.shareImg)}&og_title=${encodeURIComponent(this.state.shareTitle)}&og_description=${encodeURIComponent(this.state.shareDescription)}&lp_title=${encodeURIComponent(this.state.shareLpTitle)}&lp_description=${encodeURIComponent(this.state.shareLpDescription)}&func=appShare`;
            }).catch(() => {
                this.switchPage('error')
            });
        } else {
            this.switchPage("loading");
            console.log(`callback:nativeShare?og_image=${encodeURIComponent(this.state.shareImg)}&og_title=${encodeURIComponent(this.state.shareTitle)}&og_description=${encodeURIComponent(this.state.shareDescription)}&lp_title=${encodeURIComponent(this.state.shareLpTitle)}&lp_description=${encodeURIComponent(this.state.shareLpDescription)}&func=appShare`)
        }
    }

    switchPage(page, backPage) {
        let pageGA = page === 'loading' ? `${page}_${this.state.loadingStatus}` : page;
        window.history.pushState(
            {
                url: `${window.location.hostname}/${pageGA}`
            },
            pageGA,
            `/${pageGA}`
        );
        window.ga('set', 'page', pageGA);
        window.ga('send', 'pageview');

        backPage = backPage ? backPage : false;
        this.setState({page,backPage});
    }
    switchShareCountry(shareCountry) {
        this.setState({shareCountry})
    }
    switchShareOrientation() {
        this.setState({shareOrientation: !this.state.shareOrientation});
    }
    switchTestImg(testImg) {
        this.setState({testImg})
    }

    componentWillMount(){
        window.appUploaded = (obj) => {
            // TODO: remove obj test declaration
            if (this.state.appEnv !== 'production') {
                obj = {
                    "photos": [
                        {
                            "image_url":"https://sun1-8.userapi.com/c852136/v852136706/857e6/p9Eg7bMKxhc.jpg",
                            "crop":[0.17292,0.00000,0.83958,1.00000],
                            "rotation":0,
                            "flip":0
                        }
                    ]
                };
            }

            this.setState({
                imgUrl:obj.photos[0].image_url,
                loadingStatus:'betaface'
            },() => {
                this.switchPage('loading');
                this.sendImg();
            });
        };

        window.appShare = (boolean) => {
            if (boolean) {
                // this.switchPage('report');
            }
        };

    }

    sendImg() {

        // TODO: delete fake json and pick true request
        if (this.state.appEnv === 'production') {
            fetch('/handler',{
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    imgUrl: this.state.imgUrl
                })
            }).then((response) => {
                if (!response.ok) {
                    throw Error(response.statusText);
                }
                return response.json();
            }).then((data) => {
                if (typeof data.faces !== "undefined" && data.faces === 0){
                    console.log('error');
                    this.switchPage('error');
                }
                this.setState({
                    data,
                    shareCountry: data.nationality[0]
                });
                this.switchPage('results')
            }).catch(() => {
                this.switchPage('error')
            });
        } else {
            const fakeResponse = {
                "nationality": [
                    {
                        "name": "Russian",
                        "confidence": 76
                    },
                    {
                        "name": "Latvian",
                        "confidence": 57
                    },
                    {
                        "name": "Uzbek",
                        "confidence": 41
                    }
                ],
                "facial features": [
                    {
                        "lips": {
                            "confidence": 100.0,
                            "nation": "Israeli"
                        }
                    },
                    {
                        "nose": {
                            "confidence": 100.0,
                            "nation": "Japanese"
                        }
                    },
                    {
                        "eyes": {
                            "confidence": 100.0,
                            "nation": "Iranian"
                        }
                    }
                ],
                "gay": 13,
                "age": 12,
                "straight": 87,
                "gender": "female"
            };
            fetch('http://www.betafaceapi.com/api/v2/media',{
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "api_key": "d45fd466-51e2-4701-8da8-04351c872236",
                    "file_uri": this.state.imgUrl,
                    "detection_flags": "basicpoints,propoints,classifiers,content",
                    "recognize_targets": [
                        "all@mynamespace"
                    ],
                    "original_filename": "sample.png"
                })
            }).then((response) => {
                if (!response.ok) {
                    throw Error(response.statusText);
                }
                return response.json();
            }).then((data) => {
                if (typeof fakeResponse.faces !== "undefined" && fakeResponse.faces === 0){
                    this.switchPage('error');
                }
                this.setState({
                    data:fakeResponse,
                    shareCountry: fakeResponse.nationality[0]
                });
                this.switchPage('results')
            }).catch((error) => {
                this.switchPage('error')
            });
        }
    }

    render() {
        switch (this.state.page) {
            case 'report':
                return <PageReport
                    data={this.state.data}

                    switchPage={(page, backPage) => this.switchPage(page, backPage)}
                    chooseImgFromApi={() => this.chooseImgFromApi()}
                />;
            case 'results':
                return <PageResult
                    imgUrl={this.state.imgUrl}
                    data={this.state.data}
                    shareCountry={this.state.shareCountry}
                    shareOrientation={this.state.shareOrientation}

                    switchTestImg={(testImg) => this.switchTestImg(testImg)}
                    switchPage={(page) => this.switchPage(page)}
                    shareThroughApi={() => this.shareThroughApi()}
                    switchShareOrientation={() => this.switchShareOrientation()}
                    switchShareCountry={(shareCountry) => this.switchShareCountry(shareCountry)}
                />;
            case 'loading':
                return <PageLoading
                    imgUrl={this.state.imgUrl}
                    status={this.state.loadingStatus}
                />;
            case 'error':
                return <PageError
                    imgUrl={this.state.imgUrl}
                    switchPage={(page) => this.switchPage(page)}
                    chooseImgFromApi={() => this.chooseImgFromApi()}
                />;
            case 'readme':
                return <PageReadme
                    backPage={this.state.backPage}
                    switchPage={(page) => this.switchPage(page)}
                    chooseImgFromApi={() => this.chooseImgFromApi()}
                />;
            default:
                return <PageIndex
                    version={this.state.version}
                    switchPage={(page) => this.switchPage(page)}
                    chooseImgFromApi={() => this.chooseImgFromApi()}
                />;
        }
    }
}

export default App;