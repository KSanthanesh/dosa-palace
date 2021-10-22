function sendMail(contactForm) {
    emailjs.send("gmail","dosa_palace", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            window.location.href = "https://8000-emerald-louse-dimxccil.ws-eu17.gitpod.io/meals/contact_reply/"
            console.log("Success", response)
        },
        function(error) {
            console.log("Failed", error)
        });
        return false
}

