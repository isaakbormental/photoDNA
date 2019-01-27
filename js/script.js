let sampleJSON = {
    data: [
        {
            nation: 'chineese',
            occuracy: 57
        },
        {
            nation: 'british',
            occuracy: 45
        },
        {
            nation: 'scotch',
            occuracy: 99
        },
        {
            nation: 'scotch',
            occuracy: 99
        }
    ]
};

function getImg() {
    let img = document.querySelector('.form__img-input');

    if (img.files && img.files[0]) {
        let reader  = new FileReader();
        reader.onloadend = function () {
            let form = document.querySelector('.form'),
                photo = form.querySelector('.form__photo'),
                submitBtn = form.querySelector('.form__submit-btn');
            form.imgForSend = reader.result;

            photo.style.background = 'url("'+reader.result+'") no-repeat center center / cover';
            photo.classList.add('form__photo_filled');
            submitBtn.removeAttribute('disabled');
        };

        reader.readAsDataURL(img.files[0]);
    }

}

function sendImg(form) {
    let data = {
      img: form.imgForSend
    };

    $.ajax({
        type:"POST",
        url:form.getAttribute("action"),
        contentType: 'application/json',
        dataType : "json",
        data:JSON.stringify(data),
        success: function(response){
            switchPage(2);
            addDiag(response.data)
        },
        error: function (error) {
            switchPage(2);
            addDiag(sampleJSON.data)
        }
    });
}

function addDiag(data) {
    let template = $('.block6__template .block6__graphic');
    let diagContainer = $('.block6__graphics');

    data.forEach(function (dataItem, index) {
        if (index > 2) return;
        let graphic = template.clone();

        graphic.find('.block6__graphic-sign').html(dataItem.nation);
        graphic.find('.block6__graphic-percentage').html(dataItem.occuracy);
        graphic.attr('data-percent', dataItem.occuracy);

        diagContainer.append(graphic);
        fillDiag();
    })

}

function switchPage(number) {
    $('[data-page]').each(function () {
        let pageNum = $(this).attr('data-page');
        if(+pageNum === number) {
            $(this).show();
        } else {
            $(this).hide();
        }
    })
}

function fillDiag() {
    let duration = 1000;
    let circleLength = 471;
    let percent = circleLength/100;
    let graphics = $('.block6__graphic');
    for (let i = 0; i < graphics.length; i++) {
        (function(i) {
            let $percentageDigit = $(graphics[i]).find('.block6__graphic-percentage');
            let fillPercent = parseInt($(graphics[i]).attr('data-percent'));
            $(graphics[i]).find('.block6__diag-circle').attr('stroke-dasharray', percent*fillPercent + " " + circleLength);
            let percentCounter = 0;
            let interval = null;
            let frequency = duration/fillPercent;
            function addingPercent () {
                percentCounter++;
                if (percentCounter < fillPercent + 1) {
                    $percentageDigit.text(percentCounter);
                }
                else {
                    clearInterval(interval);
                }
            }
            interval = setInterval(addingPercent, frequency);
        })(i);
    }
}



document.querySelector('.form__img-input').addEventListener('change', getImg);
document.querySelector('.form').addEventListener('submit', function (e) {
    e.preventDefault();
    sendImg(e.target);
});