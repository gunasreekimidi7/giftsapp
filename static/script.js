function getGift(number){

    fetch('/get_gift', {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({number:number})
    })

    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText =
            "Your Gift: " + data.gift;
    });
}
