document.addEventListener('DOMContentLoaded', function () {
  const eventCard = document.getElementById('event-card');
  const timeline = document.getElementById('timeline');

  const events = {
    1: { year: '1922', title: 'Semana de Arte Moderna', description: 'Início do Modernismo no Brasil com eventos culturais inovadores.' },
    2: { year: '1930', title: 'Revolução de 1930', description: 'Mudança política importante que influenciou a cultura e as artes.' },
    3: { year: '1942', title: 'Publicação de obras modernistas', description: 'Lançamento de livros e revistas importantes do modernismo mineiro.' },
    4: { year: '1950', title: 'Consolidação do Modernismo', description: 'Modernismo torna-se dominante na cultura mineira e nacional.' },
    5: { year: '1964', title: 'Golpe Militar', description: 'Período de censura e repressão, afetando profundamente a produção cultural.' },
    6: { year: '1985', title: 'Retorno à Democracia', description: 'Renascimento cultural e abertura para novas expressões artísticas.' },
    7: { year: '2000', title: 'Era Digital', description: 'Novas mídias e formas de expressão revolucionam a arte contemporânea.' },
    8: { year: '2022', title: 'Centenário da Semana de Arte Moderna', description: 'Reflexões sobre o legado modernista e sua influência atual.' }
  };

  timeline.querySelectorAll('.timeline-dot').forEach(dot => {
    dot.addEventListener('click', (e) => {
      e.stopPropagation();
      const eventId = dot.getAttribute('data-event');
      const eventData = events[eventId];

      eventCard.innerHTML = `
        <strong class="block text-lg font-semibold mb-1 text-blue-900 dark:text-blue-200">
          ${eventData.year} - ${eventData.title}
        </strong>
        <p class="text-gray-700 dark:text-gray-300">${eventData.description}</p>
      `;

      eventCard.classList.add('active');

      // Posicionamento com limite lateral
      const dotRect = dot.getBoundingClientRect();
      const timelineRect = timeline.getBoundingClientRect();

      let leftPos = dotRect.left - timelineRect.left + dotRect.width / 2 - eventCard.offsetWidth / 2;
      const topPos = dotRect.top - timelineRect.top + 40;

      // Impede que o card ultrapasse os limites laterais
      if (leftPos < 0) {
        leftPos = 0;
      }
      const maxLeft = timeline.offsetWidth - eventCard.offsetWidth;
      if (leftPos > maxLeft) {
        leftPos = maxLeft;
      }

      eventCard.style.left = `${leftPos}px`;
      eventCard.style.top = `${topPos}px`;
    });
  });

  document.addEventListener('click', (e) => {
    if (!e.target.classList.contains('timeline-dot')) {
      eventCard.classList.remove('active');
    }
  });
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

    document.addEventListener('DOMContentLoaded', () => {
        const themeToggle = document.getElementById('theme-toggle')
        const themeToggleDot = document.getElementById('theme-toggle-dot')
        const htmlElement = document.documentElement
        const mainContent = document.getElementById('main-content') // Pega o elemento <main>
      
        // Função para aplicar o tema
        const applyTheme = (theme) => {
          // Aplica o tema geral ao HTML (para sidebar, footer, etc.)
          if (theme === 'dark') {
            htmlElement.classList.add('dark')
            themeToggleDot.style.transform = 'translateX(32px)'
          } else {
            htmlElement.classList.remove('dark')
            themeToggleDot.style.transform = 'translateX(0px)'
          }
      
          // Força a cor de fundo do conteúdo principal (<main>)
          // Cor de fundo para o modo escuro: #111827 (cor de 'bg-gray-900' do Tailwind)
          // Cor de fundo para o modo claro: #ffffff (cor de 'bg-white')
          if (mainContent) {
            mainContent.style.backgroundColor = theme === 'dark' ? '#111827' : '#ffffff'
            mainContent.style.color = theme === 'dark' ? '#f3f4f6' : '#111827' // Cor do texto
          }
        }
      
        // Verifica o tema salvo ou preferência do sistema ao carregar a página
        const currentTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')
        applyTheme(currentTheme)
      
        // Adiciona o evento de clique no botão para trocar o tema
        themeToggle.addEventListener('click', () => {
          const newTheme = htmlElement.classList.contains('dark') ? 'light' : 'dark'
          localStorage.setItem('theme', newTheme)
          applyTheme(newTheme)
        })
      })