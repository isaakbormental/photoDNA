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
            console.log(response);
        }
    });
}

document.querySelector('.form__img-input').addEventListener('change', getImg);
document.querySelector('.form').addEventListener('submit', function (e) {
    e.preventDefault();
    sendImg(e.target);
});