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

        validateField('#id_nombre', /^[a-zA-Z\s]+$/);

        validateField('#id_apellido', /^[a-zA-Z\s]+$/);

        validateField('#id_fecha_nacimiento', /^\d{4}-\d{2}-\d{2}$/);

        validateField('#id_telefono', /^\d{11}$/);

        var direccion = $('#id_direccion').val();
        if (direccion === "") {
            $('#id_direccion').addClass('is-invalid');
            isValid = false;
        } else {
            $('#id_direccion').removeClass('is-invalid');
        }

        validateField('#id_codigo_postal', /^\d{7}$/);

        validateField('#id_correo', /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/);

        validateField('#id_password1', /^[a-zA-Z0-9@#$_]{8,20}$/);

        if (isValid) {
            $('#formulario').off('submit').submit();
        }
    });
});
