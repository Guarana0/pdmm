document.addEventListener('DOMContentLoaded', function () {
    // Linha do Tempo
    const eventCard = document.getElementById('event-card');
    const timeline = document.getElementById('timeline');
    const events = {
      1: { year: '1922', title: 'Semana de Arte Moderna', description: 'Início do Modernismo no Brasil com eventos culturais inovadores.' },
      2: { year: '1930', title: 'Revolução de 1930', description: 'Mudança política importante que influenciou a cultura e as artes.' },
      3: { year: '1942', title: 'Publicação de obras modernistas', description: 'Lançamento de livros e revistas importantes do modernismo mineiro.' },
      4: { year: '1950', title: 'Consolidação do Modernismo', description: 'Modernismo torna-se dominante na cultura mineira e nacional.' }
    };
    timeline.querySelectorAll('.timeline-dot').forEach(dot => {
      dot.addEventListener('click', (e) => {
        e.stopPropagation();
        const eventId = dot.getAttribute('data-event');
        const eventData = events[eventId];
        eventCard.innerHTML = `<strong class="block text-blue-900">${eventData.year} - ${eventData.title}</strong><p class="mt-1 text-gray-700">${eventData.description}</p>`;
        eventCard.classList.add('active');
        const dotRect = dot.getBoundingClientRect();
        const timelineRect = timeline.getBoundingClientRect();
        const leftPos = dotRect.left - timelineRect.left + dotRect.width / 2 - eventCard.offsetWidth / 2;
        const topPos = dotRect.top - timelineRect.top + 40;
        eventCard.style.left = `${leftPos}px`;
        eventCard.style.top = `${topPos}px`;
      });
    });
    document.addEventListener('click', (e) => {
      if (!e.target.classList.contains('timeline-dot')) {
        eventCard.classList.remove('active');
      }
    });

    // Carrossel
    const container = document.getElementById('carousel-container');
    const slides = container.querySelectorAll('.carousel-slide');
    let currentIndex = 0;
    const totalSlides = slides.length;
    function nextSlide() {
      currentIndex = (currentIndex + 1) % totalSlides;
      updateSlide();
    }
    function updateSlide() {
      const translateX = -currentIndex * 100;
      container.style.transform = `translateX(${translateX}%)`;
    }
    setInterval(nextSlide, 5000);
  });

// Fecha menu mobile ao clicar
    document.querySelectorAll('aside nav a').forEach(link => {
      link.addEventListener('click', () => {
        const menuToggle = document.getElementById('menu-toggle');
        if(menuToggle.checked) menuToggle.checked = false;
      });
    });

    // Submenu "Revistas"
    const revistasLink = document.getElementById('revistas-link');
    const submenu = document.getElementById('submenu');

    revistasLink.addEventListener('click', () => {
      submenu.style.display = submenu.style.display === 'flex' ? 'none' : 'flex';
    });