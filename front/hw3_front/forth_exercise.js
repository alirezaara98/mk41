arr = [2,3,4]

function findByItem(array, item){
   let index = array.indexOf(item);
   document.write(`index: ${index}, item: ${item}`);
}

findByItem(arr, 3);