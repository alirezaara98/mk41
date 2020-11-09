arr = ['a','b','c','d','e','f'];

function replaceByItem(array, currentItem, newItem){
    let index = array.indexOf(currentItem);
    array.splice(index,1,newItem);
    document.write(array);
}

replaceByItem(arr, 'e', 't');