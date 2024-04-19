document.addEventListener('DOMContentLoaded', function() {
    var loader = document.querySelector('.loader');
    var loaderWidth = 0; // Начальная ширина полосы загрузки

    // Функция для увеличения ширины полосы загрузки
    function increaseWidth() {
        loaderWidth++; // Увеличиваем ширину на 1
        loader.style.width = loaderWidth + '%'; // Обновляем ширину полосы загрузки
        // Проверяем, достигла ли ширина 100%
        if (loaderWidth >= 195) {
            // Если да, выполняем переадресацию

            clearInterval(interval); // Останавливаем интервал
            window.location.href = "Privacy_Policy.html"; // Используем абсолютный путь
        }
    }

    // Увеличиваем ширину полосы загрузки каждые 50 миллисекунд
    var interval = setInterval(increaseWidth, 50);
});