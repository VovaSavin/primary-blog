$('body').on('click', '.b-cust', function (event) {
    alert('Сообщение отправленно!');
});

$('body').on('click', '.for-delete_message', function (event) {
    event.preventDefault();
    if (confirm('Вы уверены?')) {
        var url = $(this).attr('data-url')
        var tag_span = $(this).parent()
        console.log(url)
    }

    popup.classList.add('show');
});