document.getElementById("imageInput").addEventListener("change", function (event) {
    const previewContainer = document.getElementById("previewContainer");
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            previewContainer.innerHTML = `<img src="${e.target.result}" alt="Preview">`;
        };
        reader.readAsDataURL(file);
    } else {
        previewContainer.innerHTML = "<p>No image selected.</p>";
    }
});
