// Jednostavne validacije
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Primer: Proveri da li su adrese popunjene
            const inputs = form.querySelectorAll('input[required]');
            let valid = true;
            inputs.forEach(input => {
                if (!input.value.trim()) valid = false;
            });
            if (!valid) {
                e.preventDefault();
                alert('Molimo popunite sva polja.');
            }
        });
    });
});
