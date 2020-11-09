
arr = ["a","b","c"]
function deleteByIndex(array,i){
    for (let index in array){
        if (index == i){
            array.splice(index, 1);
        };
    };
    document.write(array);
};

deleteByIndex(arr, 1)
