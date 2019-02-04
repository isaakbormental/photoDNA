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
            page: 'default',
            img: false,
            shareCountry: '',
            shareOrientation: false
        };
    }

    chooseImgFromApi() {
        // TODO: pick right method (see callback API)
        /*const http = new XMLHttpRequest();
        http.open("GET", "callback:nativePhotoSelect?func=appUploaded");
        http.send();*/
        window.appUploaded('test');
    }
    shareThroughApi() {
        // TODO: pick right method (see callback API)
        /*const http = new XMLHttpRequest();
        http.open("GET", "callback:nativeShare?og_image=https://bipbap.ru/wp-content/uploads/2017/04/priroda_kartinki_foto_03.jpg&og_title=Мега%20Фото&og_d
escription=Расшарьте%20пожалуйста%21&func=appShare");
        http.send();*/
        console.log('share-share');
    }

    switchPage(page) {
        this.setState({page})
    }

    componentWillMount(){
        window.appUploaded = (obj) => {
            // TODO: remove obj test declaration
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
            let imgUrl = obj.photos[0].image_url;

            window.getDataUri(imgUrl)
                .then(result => {
                    this.setState({img: result});
                    this.sendImg();
                })
                .catch(err => this.switchPage('error'));
        };
        window.updatePage = (page) => {
            this.switchPage(page)
        };
    }

    sendImg() {
        this.switchPage("loading");

        const fakeResponse = {
            "nationality": [
                {
                    "name": "Saudi Arabian",
                    "confidence": 80
                },
                {
                    "name": "Russian",
                    "confidence": 80
                },
                {
                    "name": "Ethiopian",
                    "confidence": 47
                }
            ],
            "straight": 90,
            "gay": 10,
            "gender": "male",
            "facial features": {
                "lips": {
                    "nation": "Czech",
                    "confidence": 97.0
                },
                "nose": {
                    "nation": "Samoan",
                    "confidence": 55.0
                },
                "eyes": {
                    "nation": "Romanian",
                    "confidence": 64.0
                }
            },
            "age": 37
        };

        // TODO: delete fake json and pick true request
        /*fetch('/handler',{
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
            this.setState({data});
            this.switchPage('results')
        }).catch(() => {
            this.switchPage('error')
        });*/

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

    render() {
        switch (this.state.page) {
            case 'results':
                return <PageResult
                    img={this.state.img}
                    data={this.state.data}
                    shareCountry={this.state.shareCountry}
                    switchPage={(page) => this.switchPage(page)}
                    shareThroughApi={() => this.shareThroughApi()}
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