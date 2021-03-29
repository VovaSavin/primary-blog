$('body').on('click', '.b-cust', function (event) {
    alert('Сообщение отправленно!');
});

$('body').on('click', '.for-delete_message', function (event) {
    alert(confirm('Вы уверены?'));
});

$('body').on('click', '.b-comment', function (event) {
    alert('Комментарий добавлен!');
});

$('body').on('click', '.comment-custom', function (event) {
    alert(confirm('Вы уверены?'));
});