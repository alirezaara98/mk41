



function get_data(){
    let promise = new Promise((resolve, reject) => {
        $.ajax({
            type: "get",
            url: "https://currency.jafari.li/json",
            success: function (response) {
                let resault = JSON.parse(response)
                resolve(resault)
            },
            fail: function(){
                reject("an error accured")
            }
        });
    })
    return promise
}


function main(){
    get_data().then((resault) => {
        console.log(resault)
        let str1 = ""
        let str2 = ""
        for(indx in resault["Gold"]){
            for (sub_item in resault["Gold"][indx]){
                str1 += `<li>${sub_item}: ${resault["Gold"][indx][sub_item]}</li>`
            }
        }
        for(indx in resault["Currency"]){
            for (sub_item in resault["Currency"][indx]){
                str2 += `<li>${sub_item}: ${resault["Currency"][indx][sub_item]}</li>`
            }
        }
        $("#page").append(`
            <div>
                <p><b>GOLD</b></p>
                <ul>
                    ${str1}
                </ul>
            </div>
            <div>
                <p><b>CURRENCY</b></p>
                <ul>
                    ${str2}
                </ul>
            </div>
        `);
    })
    .catch((err) => {
        console.log(err)
    })
}

main()
setInterval(main, 500)