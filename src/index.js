import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import * as serviceWorker from './serviceWorker';

window.getDataUri = async function(imageUrl) {
    let res = await fetch(imageUrl);
    let blob = await res.blob();

    return new Promise((resolve, reject) => {
        let reader  = new FileReader();
        reader.addEventListener("load", function () {
            resolve(reader.result);
        }, false);

        reader.onerror = () => {
            return reject(this);
        };
        reader.readAsDataURL(blob);
    })
};

window.appUploaded = function(obj) {
    // remove obj test declaration
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
        .then(result => console.log(result))
        .catch(err => console.error(err));
};

ReactDOM.render(<App />, document.getElementById('root'));

if (module.hot) {
    module.hot.accept();
}

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
