function toggleForm(formId) {
    var form = document.getElementById(formId);

    if (form) {
        form.classList.toggle("hidden");
        console.log(`Toggled visibility for: ${formId}`);
    } else {
        console.error(`Element with ID '${formId}' not found!`);
    }
}
