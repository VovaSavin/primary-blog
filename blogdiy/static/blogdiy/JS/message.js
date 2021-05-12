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


function darK(darkSite) {
    document.body.style.backgroundColor = "#020305";
    document.body.style.color = "#d8f2f5";
    document.getElementById("dark").style.display = "none";
    document.getElementById("light").style.display = "flex";
    document.getElementById('customsblog').style.background = "rgb(63, 58, 58)";
};

function lighT(lightSite) {
    document.body.style.backgroundColor = "#ecfffe";
    document.body.style.color = "#000";
    document.getElementById("light").style.display = "none";
    document.getElementById("dark").style.display = "flex";
    document.getElementById('customsblog').style.background = "#d7f3f8";
};

function showInfo(info) {
    document.getElementById("aboutme").style.display = "block";
    document.getElementById("openinfo").style.display = "none";
};

function hiddenInfo(infohidden) {
    document.getElementById("aboutme").style.display = "none";
    document.getElementById("openinfo").style.display = "block";
};

function showBlog(blog) {
    document.getElementById("showmeblog").style.display = "block";
    document.getElementById("show").style.display = "none";
    document.getElementById("hide").style.display = "block";
};

function hiddenBlog(bloghidden) {
    document.getElementById("showmeblog").style.display = "none";
    document.getElementById("show").style.display = "block";
    document.getElementById("hide").style.display = "none";
};

function hideFilter(filtersClose) {
    document.getElementById("all_filter").style.display = "none";
    document.getElementById("open-filter").style.display = "flex";
    document.getElementById("hide-filter").style.display = "none";
};

function showFilter(filtersOpen) {
    document.getElementById("all_filter").style.display = "flex";
    document.getElementById("open-filter").style.display = "none";
    document.getElementById("hide-filter").style.display = "flex";
};
