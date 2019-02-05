import React, { Component } from 'react';
import './App.scss';
import PageIndex from "./pages/PageIndex/PageIndex";
import PageReadme from "./pages/PageReadme/PageReadme";
import PageError from "./pages/PageError/PageError";
import PageLoading from "./pages/PageLoading/PageLoading";
import PageResult from "./pages/PageResult/PageResult";



class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            appEnv: !'production',
            page: 'default',
            img: false,
            shareCountry: '',
            shareOrientation: false,
            shareImg: 'https://sun1-8.userapi.com/c852136/v852136706/857e6/p9Eg7bMKxhc.jpg',
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

            fetch('/amazgen',{
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    img: this.state.img,
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
                this.setState({shareImg:response.link});
                window.location.href = `callback:nativeShare?og_image=${this.state.shareImg}&og_title=${this.state.shareTitle}&og_description=${this.state.shareDescription}&lp_title=${this.state.shareLpTitle}&lp_description=${this.state.shareLpDescription}&func=appShare`;
            }).catch(() => {
                this.switchPage('error')
            });
        } else {
            console.log(window.location.href = `callback:nativeShare?og_image=${this.state.shareImg}&og_title=${this.state.shareTitle}&og_description=${this.state.shareDescription}&lp_title=${this.state.shareLpTitle}&lp_description=${this.state.shareLpDescription}&func=appShare`);
        }
    }

    switchPage(page) {
        this.setState({page})
    }
    switchShareCountry(shareCountry) {
        this.setState({shareCountry})
    }
    switchShareOrientation() {
        console.log('shaaaaaaar');
        this.setState({shareOrientation: !this.state.shareOrientation});
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
            let imgUrl = obj.photos[0].image_url;

            window.getDataUri(imgUrl)
                .then(result => {
                    this.setState({img: result});
                    this.sendImg();
                })
                .catch(err => this.switchPage('error'));
        };

        window.appShare = (boolean) => {
            if (boolean) {
                this.switchPage('report');
            } else {
                this.switchPage('default');
            }
        };

    }

    sendImg() {
        this.switchPage("loading");

        // TODO: delete fake json and pick true request
        if (this.state.appEnv === 'production') {
            fetch('/handler',{
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    img: this.state.img
                })
            }).then((response) => {
                if (!response.ok) {
                    throw Error(response.statusText);
                }
                return response.json();
            }).then((data) => {
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
                    "file_base64": this.state.img.split(',')[1],
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
            case 'results':
                return <PageResult
                    img={this.state.img}
                    data={this.state.data}
                    shareCountry={this.state.shareCountry}
                    shareOrientation={this.state.shareOrientation}

                    switchPage={(page) => this.switchPage(page)}
                    shareThroughApi={() => this.shareThroughApi()}
                    switchShareOrientation={() => this.switchShareOrientation()}
                    switchShareCountry={(shareCountry) => this.switchShareCountry(shareCountry)}
                />;
            case 'loading':
                return <PageLoading
                    img={this.state.img}
                />;
            case 'error':
                return <PageError
                    chooseImgFromApi={() => this.chooseImgFromApi()}
                />;
            case 'readme':
                return <PageReadme
                    switchPage={(page) => this.switchPage(page)}
                    chooseImgFromApi={() => this.chooseImgFromApi()}
                />;
            default:
                return <PageIndex
                    switchPage={(page) => this.switchPage(page)}
                    chooseImgFromApi={() => this.chooseImgFromApi()}
                />;
        }
    }
}

export default App;