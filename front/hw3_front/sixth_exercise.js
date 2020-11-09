str = "Ihave 2 apples and 3 pineapples";


function checker(string){
    our_str = string.split(' ');
    result = our_str.filter((item) => item >= '0' && item <= '9');
    document.write(result);
}


checker(str);