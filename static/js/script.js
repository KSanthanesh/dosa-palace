var emailjs;
// date pick for add reserve
function dt() {
    var dtToday = new Date();

    var month = dtToday.getMonth() + 1;
    var day = dtToday.getDate();
    var year = dtToday.getFullYear();
    if (month < 10)
        month = '0' + month.toString();
    if (day < 10)
        day = '0' + day.toString();

    var maxDate = year + '-' + month + '-' + day;
    $('#date').attr('min', maxDate);
}

// Delete Modal box
function myid(a) {

    document.getElementById("my_id").value = a;
}
function deleteBooking() {
    window.location.href = "/delete/" + document.getElementById('my_id').value;
}

//  Contact Page-Send mail
function sendMail(contactForm) {
    emailjs.send("gmail", "dosa_palace", {
            "from_name": contactForm.name.value,
            "from_email": contactForm.email.value,
            "message": contactForm.message.value
        })
        .then(
            function (response) {
                window.location.href = "/contact_reply/";
                console.log("Success", response);
            },
            function (error) {
                console.log("Failed", error);
            });
    return false;
}
