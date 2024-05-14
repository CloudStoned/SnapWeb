document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('fileInput');
    fileInput.addEventListener('change', view_preview);
});

function view_preview(event) {
    const fileInput = event.target;
    const file = fileInput.files[0];
    const imagePreview = document.getElementById('imagePreview');

    console.log("initial");

    if (file) {
        const reader = new FileReader();
        console.log("if");

        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            imagePreview.classList.remove('hidden');
        };

        reader.readAsDataURL(file);
    } else {
        console.log("else");
        imagePreview.src = '#';
        imagePreview.classList.add('hidden');
    }
}
