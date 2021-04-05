$('body').on('click', '.b-cust', function (event) {
    alert('Сообщение отправленно!');
});

$('body').on('click', '.for-delete_message', function (event) {
    if (confirm('Вы уверены?')) {
        alert('Сообщение удалено!');
    } else {
        alert('Сообщение не удалено!');
        return false;
    }
});

$('body').on('click', '.b-comment', function (event) {
    alert('Комментарий добавлен!');
});

$('body').on('click', '.comment-custom', function (event) {
    if (confirm('Вы уверены?')) {
        alert('Комментарий удалён!');
    } else {
        alert('Комментарий не удалён!');
        return false;
    }
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

