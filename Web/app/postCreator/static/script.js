document.addEventListener('DOMContentLoaded', function() {
    var loader = document.querySelector('.loader');
    var loaderWidth = 0;

    function increaseWidth() {
        loaderWidth++;
        loader.style.width = loaderWidth + '%';
        if (loaderWidth >= 195) {
            clearInterval(interval);
            // Изменяем URL на нужный, без расширения
            window.location.href = "/Privacy_Policy/";
        }
    }

    var interval = setInterval(increaseWidth, 50);
});
