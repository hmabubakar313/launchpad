const colorCustom = document.getElementById('color-5');
const colorCustom_2 = document.getElementById('color-11');
const colorCustom_3 = document.getElementById('color-15');

const inputForSelectCustomColor = document.getElementById('inputForSelectCustomColor');

const inputForSelectCustomColor_2 = document.getElementById('inputForSelectCustomColor-2');

const inputForSelectCustomColor_3 = document.getElementById('inputForSelectCustomColor-3');

colorCustom.addEventListener('click', function (e) {
    inputForSelectCustomColor.classList.add('visiableInput')
})

colorCustom_2.addEventListener('click', function (e) {
    inputForSelectCustomColor_2.classList.add('visiableInput')
})

colorCustom_3.addEventListener('click', function (e) {
    inputForSelectCustomColor_3.classList.add('visiableInput')
})