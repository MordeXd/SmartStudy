document.addEventListener('DOMContentLoaded', function() {
    // GSAP animations
    gsap.from(".animate-in", {
        duration: 0.8,
        y: 50,
        opacity: 0,
        stagger: 0.1,
        ease: "back.out(1.2)"
    });

    // Form validation feedback
    document.querySelectorAll('.form-control').forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value.trim() !== '') {
                this.classList.add('filled');
            } else {
                this.classList.remove('filled');
            }
        });
    });

    // Add role badge to username in navbar
    const usernameDisplay = document.querySelector('.navbar .dropdown-toggle');
    if (usernameDisplay) {
        const role = usernameDisplay.textContent.match(/\((\w+)\)/)[1].toLowerCase();
        usernameDisplay.innerHTML = usernameDisplay.textContent.replace(
            /\((\w+)\)/, 
            `<span class="role-badge role-${role}">$1</span>`
        );
    }
});