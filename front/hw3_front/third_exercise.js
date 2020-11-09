arr = [[2, 3], 5, [[[2, 9], 4], 4], 1, 0];

function flatter(array){
    new_array = array.flat(3);
    new_array.reverse();
    //new_array.sort((a,b) => (a-b));
    document.write(new_array);
};

flatter(arr);