function printError(Id, Msg) {
    document.getElementById(Id).innerHTML = Msg;
}

function validateForm() {

    var name = document.Form.name.value;
    var email = document.Form.email.value;
    var sid = document.Form.sid.value;
    var proffession = document.Form.proffession.value;
    var gender = document.Form.gender.value;
    

    var nameErr = emailErr = sidErr = proffessionErr = genderErr = true;
    

    if(name == "") {
        printError("nameErr", "Please enter your name");
        var elem = document.getElementById("name");
            elem.classList.add("input-2");
            elem.classList.remove("input-1");
    } else {
        var regex = /^[a-zA-Z\s]+$/;                
        if(regex.test(name) === false) {
            printError("nameErr", "Please enter a valid name");
            var elem = document.getElementById("name");
            elem.classList.add("input-2");
            elem.classList.remove("input-1");
        } else {
            printError("nameErr", "");
            nameErr = false;
            var elem = document.getElementById("name");
            elem.classList.add("input-1");
            elem.classList.remove("input-2");

            
        }
    }
    

    if(email == "") {
        printError("emailErr", "Please enter your email address");
         var elem = document.getElementById("email");
            elem.classList.add("input-2");
            elem.classList.remove("input-1");
    } else {
        
        var regex = /^\S+@\S+\.\S+$/;
        if(regex.test(email) === false) {
            printError("emailErr", "Please enter a valid email address");
            var elem = document.getElementById("email");
            elem.classList.add("input-2");
            elem.classList.remove("input-1");
        } else{
            printError("emailErr", "");
            emailErr = false;
             var elem = document.getElementById("email");
            elem.classList.add("input-1");
            elem.classList.remove("input-2");

        }
    }
    
 
    if(sid == "") {
        printError("sidErr", "Please enter your SID");
        var elem = document.getElementById("sid");
            elem.classList.add("input-2");
            elem.classList.remove("input-1");
    } else {
        var regex = /^[1-9]\d{9}$/;
        if(regex.test(sid) === false) {
            printError("sidErr", "Please enter a valid  sid");
            var elem = document.getElementById("sid");
            elem.classList.add("input-2");
            elem.classList.remove("input-1");
        } else{
            printError("sidErr", "");
            sidErr = false;
            var elem = document.getElementById("sid");
            elem.classList.add("input-1");
            elem.classList.remove("input-2");
        }
    }
    

    if(proffession == "Select") {
        printError("proffessionErr", "Please select your Proffession");
        var elem = document.getElementById("proffession");
            elem.classList.add("input-4");
            elem.classList.remove("input-3");
    } else {
        printError("proffessionErr", "");
        proffessionErr = false;
        var elem = document.getElementById("proffession");
            elem.classList.add("input-3");
            elem.classList.remove("input-4");
    }
    

    if(gender == "") {
        printError("genderErr", "Please select your gender");
        var elem = document.getElementById("gender");
            elem.classList.add("input-4");
            elem.classList.remove("input-3");
    } else {
        printError("genderErr", "");
        genderErr = false;
        var elem = document.getElementById("gender");
            elem.classList.add("input-3");
            elem.classList.remove("input-4");
    }
    
    
    if((nameErr || emailErr || sidErr || proffessionErr || genderErr) == true) {
       return false;
    } 

    const passwordInput = document.getElementById('passwordErr');
    const passwordError = document.getElementById('passwordErr');

    passwordInput.addEventListener('submit', validatePassword);
    
    function validatePassword() {
        const password = passwordInput.value;

        if (password.length < 8) {
            passwordError.textContent = 'Password should be at least 8 characters long.';
        } else {
            passwordError.textContent = '';
        }
    }

    
};