/* JS for expandable payload details */
document.addEventListener('DOMContentLoaded', function() {
    const payloadItems = document.querySelectorAll('.payload-item');

    payloadItems.forEach((item) => {
        const header = item.querySelector('.payload-header');
        header.addEventListener('click', () => {
            item.classList.toggle('expanded');
        });
    });
});
