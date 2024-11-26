const btnLogin = document.getElementById('btn-login');
const modal = document.getElementById('loginModal');
const closeModal = document.querySelector('.close');
btnLogin.onclick = function() {
    modal.style.display = "block";
}
closeModal.onclick = function() {
    modal.style.display = 'none'
}
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
}