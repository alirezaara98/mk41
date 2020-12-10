var value = ""

function main(){
    $("#button").click(function () { 
        value = $("#content").val();
        get_url(value).then((resault) => {
            $("#page").append(`
                <div class="mt-4 pt-4 alert alert-warning">
                    <p>your url is: ${resault["result_url"]}</p>
                </div>
                <div class="btn bg-success">
                    <a href="${resault["result_url"]}" class="text-white">your_link</a></div>
                </div>
                `);
        })
        .catch((err) => {
            console.log(err)
        })
    })
}

function get_url(url){
    let promise = new Promise((resolve, reject) => {
        $.ajax({
            type: "post",
            url: "https://cleanuri.com/api/v1/shorten",
            data: {"url": url},
            success: function (response) {
                let resault = response
                resolve(resault)
            },
            fail: function(){
                reject("error accured")
            }
        });
    })
    return promise
}

main()