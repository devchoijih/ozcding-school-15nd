(function () {
  // DOM 준비될 때 실행되도록 변경
  document.addEventListener('DOMContentLoaded', function () {

    const form = document.querySelector('.needs-validation');
    const pw1 = document.getElementById('password');
    const pw2 = document.getElementById('password2');

    function checkPwMatch() {
      if (pw2.value && pw1.value !== pw2.value) {
        pw2.setCustomValidity('비밀번호 불일치');
      } else {
        pw2.setCustomValidity('');
      }
    }

    pw1.addEventListener('input', checkPwMatch);
    pw2.addEventListener('input', checkPwMatch);

    form.addEventListener('submit', function (e) {
      checkPwMatch();

      if (!form.checkValidity()) {
        e.preventDefault();
        e.stopPropagation();
      } else {
        e.preventDefault();
        alert("회원가입이 완료되었습니다!");
        window.location.href = "./main.html";
      }

      form.classList.add('was-validated');
    });

  });
})();