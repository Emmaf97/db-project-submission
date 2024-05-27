document.addEventListener("DOMContentLoaded", init);

function init() {
    let form = document.getElementById("contact-form");
    form.addEventListener("submit", submitEvent);
    let nameBox = document.getElementById("fName");
    nameBox.addEventListener("focusout", invalidFName);
    let lastNameBox = document.getElementById("lName");
    lastNameBox.addEventListener("focusout", invalidLName);
    let emailBox = document.getElementById("clientEmail");
    emailBox.addEventListener("focusout", invalidEmail);
    let telephoneBox = document.getElementById("clientTel");
    telephoneBox.addEventListener("focusout", invalidTel);
}
// this submit event is checking thst the required fields for inputs in a number of use cases e.g all inputs empty, 2 inputs empty etc.
// It does this by calling the isEmpty function this returns true or false.
// If isEmpty is true it creates the error message and displays them under the corresponding elements that are required, using the createError method.
// If isEmpty returns false it removes the errormessage and prevents multiple of them from displaying each time the button is clicked.
function submitEvent(event) {
    event.preventDefault();
    let { nameInput, nameLastInput, emailInput, telephoneInput } = getFormElements();
    let errorMsg = document.getElementById("error");
    if (isEmpty() === true) {
        if (!errorMsg) {
            if (!nameInput.value && !nameLastInput.value && !emailInput.value && !telephoneInput.value) {
                createError(nameInput);
                createError(nameLastInput);
                createError(emailInput);
                createError(telephoneInput);
            }
            else if (!nameInput.value && !nameLastInput.value) {
                createError(nameInput);
                createError(nameLastInput);
            }
            else if (!emailInput.value && !telephoneInput.value) {
                createError(emailInput);
                createError(telephoneInput);
            }
            else if (!nameInput.value) {
                createError(nameInput);
            }
            else if (!nameLastInput.value) {
                createError(nameLastInput);
            }
            else if (!emailInput.value) {
                createError(emailInput);
            }
            else if (!telephoneInput.value) {
                createError(telephoneInput);
            }
        }
    } else if (isEmpty() === false) {
        if (nameInput.value && nameLastInput.value && emailInput.value && telephoneInput.value) {
            removeError(errorMsg);
            removeError(errorMsg);
            removeError(errorMsg);
            removeError(errorMsg);
            removeError(errorMsg);
        }
        else if (nameInput.value && nameLastInput.value) {
            removeError(errorMsg);
            removeError(errorMsg);
        }
        else if (emailInput.value && telephoneInput.value) {
            removeError(errorMsg);
            removeError(errorMsg);
        }
        else if (nameInput.value) {
            removeError(errorMsg);
        }
        else if (nameLastInput.value) {
            removeError(errorMsg);
        }
        else if (emailInput.value) {
            removeError(errorMsg);
        }
        else if (telephoneInput.value) {
            removeError(errorMsg);
        }
    }
}

function isEmpty() {
    let { nameInput, nameLastInput, emailInput, telephoneInput } = getFormElements();
    if (nameInput.value && nameLastInput.value && emailInput.value && telephoneInput.value) {
        // console.log("value detected for all inputs");
        return false;
    } else if (nameInput.value && nameLastInput.value) {
        // console.log("value detected for first and last name");
        return false;
    } else if (emailInput.value && telephoneInput.value) {
        // console.log("value detected for email and mobile");
        return false;
    }
    else if (!nameInput.value && !nameLastInput.value && !emailInput.value && !telephoneInput.value) {
        // console.log(" no value detected for all inputs");
        return true;
    } else if (!nameInput.value && !nameLastInput.value) {
        // console.log("no value detected for first and last name");
        return true;
    } else if (!emailInput.value && !telephoneInput.value) {
        // console.log("no value detected for email and mobile");
        return true;
    }
}
function createError(nameInput, nameLastInput, emailInput, telephoneInput) {
    let errorMsg = document.createElement("p");
    errorMsg.innerText = "This Field is Required";
    errorMsg.classList.add("alert");
    errorMsg.classList.add("alert-danger")
    errorMsg.id = "error";
    if (nameInput) {
        nameInput.parentNode.insertBefore(errorMsg, nameInput.nextElementSibling);
    }
    if (nameLastInput) {
        nameLastInput.parentNode.insertBefore(errorMsg, nameLastInput.nextElementSibling);
    }
    if (emailInput) {
        emailInput.parentNode.insertBefore(errorMsg, emailInput.nextElementSibling);
    }
    if (telephoneInput) {
        telephoneInput.parentNode.insertBefore(errorMsg, telephoneInput.nextElementSibling);
    }
}
function removeError(errorMsg) {
    errorMsg.remove();
}

// this returns the common elements of the form so that I can all them easily without repeating the same code on multiple lines.
function getFormElements() {
    let nameInput = document.getElementById("fName");
    let nameLastInput = document.getElementById("lName");
    let emailInput = document.getElementById("clientEmail");
    let telephoneInput = document.getElementById("clientTel");

    return { nameInput, nameLastInput, emailInput, telephoneInput };
}
// In invalidFName I check to see if the user entered a digit into the field. If so an error message will be displayed.
function invalidFName() {
    let nameInput = document.getElementById("fName");
    let errorMsg = nameInput.nextElementSibling;
    if (/\d/.test(nameInput.value)) {
        if (!errorMsg) {
            errorMsg = document.createElement("p");
            errorMsg.classList.add("invalid-Form-Input");
            nameInput.parentNode.insertBefore(errorMsg, nameInput.nextElementSibling);
        }
        errorMsg.innerText = "This field does not accept numeric values";
    } else {
        if (errorMsg) {
            console.log("Error Message already created");
            nameInput.nextElementSibling.remove();
        }
    }
}
// In invalidLName I check to see if the user entered a digit into the field. If so an error message will be displayed.
function invalidLName() {
    let nameLastInput = document.getElementById("lName");
    let errorMsg = nameLastInput.nextElementSibling;
    if (/\d/.test(nameLastInput.value)) {
        if (!errorMsg) {
            errorMsg = document.createElement("p");
            errorMsg.classList.add("invalid-Form-Input");
            nameLastInput.parentNode.insertBefore(errorMsg, nameLastInput.nextElementSibling);
        }
        errorMsg.innerText = "This field does not accept numeric values";
    } else {
        if (errorMsg) {
            console.log("Error Message already created");
            nameLastInput.nextElementSibling.remove();
        }
    }
}
// In invalidEmail I check to see if the user entered an @ format for the email and I also check if they have a gmail.com format.
// If the user does not enter an @ symbol the @ symbol error will appear.
// If the user does not enter gmail.com the gmail format error will appear.
function invalidEmail() {
    let emailInput = document.getElementById("clientEmail");
    let errorMsg = emailInput.nextElementSibling;
    if (!emailInput.value.includes("@")) {
        if (!errorMsg) {
            errorMsg = document.createElement("p");
            errorMsg.classList.add("invalid-Form-Input");
            emailInput.parentNode.insertBefore(errorMsg, emailInput.nextElementSibling);
        }
        errorMsg.innerText = "This field requires an @ email address format";
    } else if (!emailInput.value.includes("@gmail.com")) {
        if (!errorMsg) {
            errorMsg = document.createElement("p");
            errorMsg.classList.add("invalid-Form-Input");
            emailInput.parentNode.insertBefore(errorMsg, emailInput.nextElementSibling);
        }
        errorMsg.innerText = "This field requires a gmail address format";
    }
    else {
        if (errorMsg) {
            emailInput.nextElementSibling.remove();
        }
    }
}

// In invalidTel I check to see if the user entered any character other than a digit. If so an error message will be displayed.
// I also check to see that the length of the number entered is not less than 10 digits.
function invalidTel() {
    let telephoneInput = document.getElementById("clientTel");
    let errorMsg = telephoneInput.nextElementSibling;
    if (!/\d/.test(telephoneInput.value)) {
        if (!errorMsg) {
            errorMsg = document.createElement("p");
            errorMsg.classList.add("invalid-Form-Input");
            telephoneInput.parentNode.insertBefore(errorMsg, telephoneInput.nextElementSibling);
        }
        errorMsg.innerText = "This field requires numeric input";
    } else if (telephoneInput.value.length < 10) {
        if (!errorMsg) {
            errorMsg = document.createElement("p");
            errorMsg.classList.add("invalid-Form-Input");
            telephoneInput.parentNode.insertBefore(errorMsg, telephoneInput.nextElementSibling);
        }
        errorMsg.innerText = "Mobile number cannot be less than 10";
    } else {
        if (errorMsg) {
            telephoneInput.nextElementSibling.remove();
        }
    }
}
