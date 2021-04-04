$('body').on('click', '.b-cust', function (event) {
    alert('Сообщение отправленно!');
});

$('body').on('click', '.for-delete_message', function (event) {
    if (confirm('Вы уверены?')) {
        alert('Сообщение удалено!');
    } else {
        alert('Не удалено!');
        return false;
    }
});

$('body').on('click', '.b-comment', function (event) {
    alert('Комментарий добавлен!');
});

$('body').on('click', '.comment-custom', function (event) {
    alert(confirm('Вы уверены?'));
});


myphoto.onclick = function () {
    var big = document.getElementById('myphoto').offsetWidth;
    if (big < 200) {
        myphoto.classList.add('growing');
    }
    else {
        myphoto.classList.add('small_grow');
    }
};

$(document).ready(function () {
    $(".dropdown-toggle").dropdown();
});

