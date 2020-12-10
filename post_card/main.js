

function get_post(){
    let promise = new Promise((reverse, reject)=>{
        $.ajax({
            type: "get",
            url: "https://jsonplaceholder.ir/posts",
            success: function (response) {
                post_arr = response
                reverse(post_arr)
            },
            fail: function(){
                reject("error")
            }
        });
    })
    return promise
}

function get_user(){
    let promise = new Promise((resolve, reject)=>{
        $.ajax({
            type: "get",
            url: "https://jsonplaceholder.ir/users",
            success: function (response) {
                user_arr = response
                resolve(user_arr)
            },
            fail: function(){
                reject("error")
            }
        });
    })
    return promise
}

function get_comment(){
    let promise = new Promise((re, reject)=>{
        $.ajax({
            type: "get",
            url: "https://jsonplaceholder.ir/comments",
            success: function (response) {
                user_arr = response
                reverse(user_arr)
            },
            fail: function(){
                reject("error")
            }
        });
    })
    return promise
}

function post_inf(){
    // let str = ""
    // let author = ""
    get_post().then((data)=>{
        for(post of data){
            get_user().then((data)=>{
                for(user of data){
                    if (post['userID']== user['id']){
                        author = user['name']
                    }
                }
            }).catch((err)=>{console.log(err);})
            str += `<div class="card-body">
            <h5 class="card-title">${post['title']}</h5>
            <small class="card-text">${author}</small>
            <p class="card-text">${post['body']}</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>`
        }
        $("#card_box").append(`${str}`);
    }).catch((err)=>{console.log(err)})
}

function main(){
    get_post().then((data)=>{
        console.log(data)
    }).catch((err)=>{console.log(err)})

    get_user().then((data)=>{
        console.log(data)
    }).catch((err)=>{console.log(err);})

    get_comment().then((data)=>{
        console.log(data);
    }).catch((err)=>{console.log(err);})
}

main()

post_inf()
