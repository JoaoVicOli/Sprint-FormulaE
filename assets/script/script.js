document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const usuario = document.getElementById('usuario').value;
    const senha = document.getElementById('senha').value;
    
    if (usuario === "solution" && senha === "12345"){
        alert('Sucesso liberando seções');
        document.getElementById('dropdownContainer').style.display = 'flex'; 
        document.querySelector('.header-login').addEventListener('submit', function(){
            this.classList.add('fade-out');
            this.addEventListener('animationend', () => {
            this.style.display = 'none';
              });
        })
    } else {
        alert('Senha e/ou usuário incorretos');
    }
});

let imagens1 = ["./assets/img/acidflask.png", "./assets/img/thermometer.png", "./assets/img/pollution_7925306.png"];
let index1 = 0;
let time1 = 2000;

function slideShow1() {
    document.getElementById("imgbanner1").src = imagens1[index1];
    index1++;
    
    if (index1 === imagens1.length) {
        index1 = 0;
    }
    setTimeout(slideShow1, time1);
}

slideShow1();