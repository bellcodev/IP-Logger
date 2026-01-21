async function getUserIP() {
    try {
        const response = await fetch('https://api.ipify.org?format=json');
        const data = await response.json();

        fetch("/getIp", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({ i: data.ip })
        })
    } catch (error) {
        return
    }
}

window.addEventListener('load', function() {
    getUserIP().then(ip => {
        return 'sucess'
    });
});

let path = window.location.pathname;

if (path === '/f/script.js' || path === '/main.py') {
    window.location.href('/');
}
