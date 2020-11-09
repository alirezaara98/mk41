arr = [1, 1, 4, 5, 3, 5, 3, 9]

function remover(array){
    result = array.filter((item, index) => array.indexOf(item) == index);
    document.write(result);
}

remover(arr);