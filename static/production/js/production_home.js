$(document).ready(function() { // Вызвать функцию при загрузке страницы
    load_types(); // Вызвать функцию загрузки типов
});
// Обработать событие изменения значения виджета выбора категории
function load_types() { 
var url = $("#productForm").attr("data-types-url"); // Получить URL-адрес представления для загрузки типов
var categoryId = $("#id_category").val(); // Получить выбранное значение категории
var typeId = $("#id_type").val();

$.ajax({ // Отправить AJAX-запрос на сервер
    url: url,
    data: {
    'category': categoryId // Передать параметр категории
    },
    dataType: 'json',
    success: function (data) { // Получить ответ от сервера в виде JSON-данных
    $("#id_type").html(""); // Очистить виджет выбора типа
    $("#id_type").append('<option value="">Типы</option>'); // Добавить пустую опцию по умолчанию
    data.forEach(function(item) { // Для каждого элемента в данных (списке типов)
        var option = new Option(item.title, item.id); // Создать новую опцию с именем и идентификатором типа
        if (item.id == typeId) { // Если идентификатор типа равен выбранному значению
            option.selected = true; // Добавить атрибут selected к опции
        }
        $("#id_type").append(option); // Добавить опцию к виджету выбора типа
    });
    }
});
}

$("#id_category").on('input', function () {
    load_types();
});