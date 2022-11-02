$("#closeNews").click(function (e)
{
    $("#myModal").hide();
    e.preventDefault();
    sessionStorage["PopupShown"] = 'yes'; //Save in the sessionStorage if the modal has been shown
});

$("#allowCookies").click(function (e)
{
    $("#cookie").hide();
    e.preventDefault();
    sessionStorage["PopupCookie"] = 'yes'; //Save in the sessionStorage if the modal has been shown
})

document.addEventListener('DOMContentLoaded', function() {
    // ...
    // console.log('aaaaaaaa')
    // console.log(sessionStorage["PopupShown"])
    // console.log(sessionStorage["PopupCookie"])

    if(sessionStorage["PopupShown"] != 'yes'){ 
        $("#myModal").modal('show');
        e.preventDefault();
    }

    if(sessionStorage["PopupCookie"] != 'yes'){
        $("#cookie").show();
        e.preventDefault();
    }
    else {
        $("#cookie").hide();
    }
 });


// Create cookie
function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    let expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

// Delete cookie
function deleteCookie(cname) {
    const d = new Date();
    d.setTime(d.getTime() + (24*60*60*1000));
    let expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=;" + expires + ";path=/";
}

// Read cookie
function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

// Set cookie consent
function acceptCookieConsent(){
    deleteCookie('user_cookie_consent');
    setCookie('user_cookie_consent', 1, 30);
    document.getElementById("cookieNotice").style.display = "none";
}

let cookie_consent = getCookie("user_cookie_consent");
if(cookie_consent != ""){
    document.getElementById("cookieNotice").style.display = "none";
}else{
    document.getElementById("cookieNotice").style.display = "block";
}