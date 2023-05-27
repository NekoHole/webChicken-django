/*
const searchButton = document.getElementById('search-button');
const searchInput = document.getElementById('search-input');
searchButton.addEventListener('click', () => {
  const inputValue = searchInput.value;
  alert(inputValue);
});
*/

// Получаем элементы строки поиска и кнопки
var searchInput = document.getElementById("search-input");
var searchButton = document.getElementById("search-button");
var menuNavigation = document.getElementById("nav-main");
var searchNavigation = document.getElementById("nav-search");

// Создаем функцию для показа строки поиска при клике на кнопку
function showSearchInput() {
    menuNavigation.style.opacity = "0";
    
    setTimeout(function() { 
        menuNavigation.style.display = "none";
        searchNavigation.style.display = "inline-block";
    }, 1000);
    setTimeout(function() { 
        searchNavigation.style.opacity = "1"; 
        searchInput.style.width = "100%";
    }, 1010);

}

// Создаем функцию для скрытия строки поиска при потере фокуса
function hideSearchInput() {
    searchNavigation.style.opacity = "0"; 
    setTimeout(function() { 
        searchNavigation.style.display = "none";
        menuNavigation.style.display = "inline-block";
    }, 1000);
    setTimeout(function() { 
        menuNavigation.style.opacity = "1"; 
        searchInput.style.width = "0px";
    }, 1060);
}

// Добавляем обработчики событий для кнопки и строки поиска
searchButton.addEventListener("click", showSearchInput);
searchInput.addEventListener("blur", hideSearchInput);