
const hireMeButton = document.getElementById('hireMeButton');
const hireMeModal = document.getElementById('hireMeModal');
const closeModalButton = document.getElementById('closeModalButton');

const certificateCards = document.querySelectorAll('.certificate-card');
const imageModal = document.getElementById('imageModal');
const closeImageModalButton = document.getElementById('closeImageModalButton');
const modalImage = document.getElementById('modalImage');
const modalTitle = document.getElementById('modalTitle');
const modalDescription = document.getElementById('modalDescription');
const modalDate = document.getElementById('modalDate');

// Function to open the 'Hire Me' modal
function openHireMeModal() {
    hireMeModal.classList.remove('hidden');
            hireMeModal.classList.add('flex');
            const modalContent = hireMeModal.querySelector('div');
            modalContent.classList.remove('fade-out');
            modalContent.classList.add('fade-in');
        }

        // Function to close the 'Hire Me' modal
        function closeHireMeModal() {
            const modalContent = hireMeModal.querySelector('div');
            modalContent.classList.remove('fade-in');
            modalContent.classList.add('fade-out');
            modalContent.addEventListener('animationend', function handler() {
                hireMeModal.classList.add('hidden');
                hireMeModal.classList.remove('flex');
                modalContent.removeEventListener('animationend', handler);
            }, { once: true });
        }

        // Event listeners for 'Hire Me' modal
        hireMeButton.addEventListener('click', openHireMeModal);
        closeModalButton.addEventListener('click', closeHireMeModal);
        hireMeModal.addEventListener('click', (event) => {
            if (event.target === hireMeModal) {
                closeHireMeModal();
            }
        });

        // Function to open the Image modal
        function openImageModal(imgSrc, title, description, date) {
            modalImage.src = imgSrc;
            modalTitle.textContent = title;
            modalDescription.textContent = description;
            modalDate.textContent = `Issued: ${date}`;
            imageModal.classList.remove('hidden');
            imageModal.classList.add('flex');
            const modalContent = imageModal.querySelector('div');
            modalContent.classList.remove('fade-out');
            modalContent.classList.add('fade-in');
        }

        // Function to close the Image modal
        function closeImageModal() {
            const modalContent = imageModal.querySelector('div');
            modalContent.classList.remove('fade-in');
            modalContent.classList.add('fade-out');
            modalContent.addEventListener('animationend', function handler() {
                imageModal.classList.add('hidden');
                imageModal.classList.remove('flex');
                modalImage.src = ""; // Clear image src
                modalTitle.textContent = ""; // Clear title
                modalDescription.textContent = ""; // Clear description
                modalDate.textContent = ""; // Clear date
                modalContent.removeEventListener('animationend', handler);
            }, { once: true });
        }

        // Event listeners for Certificate Image modal
        certificateCards.forEach(card => {
            card.addEventListener('click', () => {
                const imgSrc = card.dataset.imgSrc;
                const title = card.dataset.title;
                const description = card.dataset.description;
                const date = card.dataset.date;
                openImageModal(imgSrc, title, description, date);
            });
        });

        closeImageModalButton.addEventListener('click', closeImageModal);
        imageModal.addEventListener('click', (event) => {
            if (event.target === imageModal) {
                closeImageModal();
            }
        });