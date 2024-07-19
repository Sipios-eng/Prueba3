$(document).ready(function() {
    $('#submitBtn').on('click', function(e) {
        e.preventDefault();
        var isValid = true;

        function validateField(field, pattern) {
            var value = $(field).val();
            if (!pattern.test(value)) {
                $(field).addClass('is-invalid');
                isValid = false;
            } else {
                $(field).removeClass('is-invalid');
            }
        }

        validateField('#username', /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/);
        validateField('#password', /^[a-zA-Z0-9@#$_]{8,20}$/);

        // Si todas las validaciones son exitosas
        if (isValid) {
            $('#formulario').off('submit').submit();  // Envía el formulario al servidor
        }
    });
});
