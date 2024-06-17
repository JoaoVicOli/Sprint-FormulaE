document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const usuario = document.getElementById('usuario').value;
    const senha = document.getElementById('senha').value;
    
    if (usuario === "sprint" && senha === "12345"){
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

let imagens = ["./assets/img/slideshow1.png", "./assets/img/slideshow2.png", "./assets/img/slideshow3.png"];
let index = 0;
let time = 2000;

function slideShow() {
    document.getElementById("imgbanner").src = imagens[index];
    index++;
    
    if (index === imagens.length) {
        index = 0;
    }
    setTimeout(slideShow, time);
}

slideShow();
