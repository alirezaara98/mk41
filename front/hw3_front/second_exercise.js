arr1 = [1,2,3]
arr2 = [4,5,6]
arr3 = [9,8,7,0]

function combinner(first, second, ...rest){
    new_arr = first.concat(second, ...rest);
    new_arr.sort((a,b)=> (a - b));
    document.write(new_arr);
};

combinner(arr1, arr2, arr3)