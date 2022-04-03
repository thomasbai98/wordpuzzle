function check_connection() {
    document.body.style.display = "inline";
}
async function buypuzzle() {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const account = accounts[0];
    const puzzle = window.ethereum.eth.Contract(ERCABI, 0x485b373fC201832b123Ee63AA3101885fa28Fef7);
    const senderAddress = account;
    purchase = document.getElementById("purchase").value;
    await puzzle.methods.buy(senderAddress).call(function (err, res) {
       
        if (err) {
            console.log("An error occured", err)
            await sleep(30000);
            return false
        }
        //await sleep(30000);

        console.log("The balance is: ", res)
        return true
    })

}
async function connect() {
    if (typeof window.ethereum == 'undefined') {
        console.log('MetaMask is not installed!');
        return
    }
    await ethereum.request({ method: 'eth_requestAccounts' });
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const account = accounts[0];



    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/");
    xhttp.setRequestHeader("Content-Type", account);
    xhttp.send();
    window.location.href = '../game';

}


async function check_account(data) {
    document.body.style.display = "inline";

    console.log(data);
    if (data.status==-1) {
        document.getElementById("solving").innerHTML = "";
    } else {
        document.getElementById("buying").innerHTML = "";
    }
}




