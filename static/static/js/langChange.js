function getLang_en(){
    if(window.location.href !== ''){
        var data = window.location.href;
        data = data.replace("/ru/","/en/");
        console.log(data)
        return function wow(){return window.location.href = data}()
 } else {
     pass;
 }
}

function getLang_ru(){
    if(window.location.href !== ''){
        var data = window.location.href;
        data = data.replace("/en/", "/ru/")
        console.log(data);
        return function wow(){return window.location.href = data}()
 } else {
     pass;
 }
}
