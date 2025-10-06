document.addEventListener('DOMContentLoaded', function () {
  const eventCard = document.getElementById('event-card');
  const timeline = document.getElementById('timeline');

  const events = {
    1: { year: '1920', title: 'Chegada da Primeira Geração Modernista', description: 'A primeira leva de autores de diversos cantos de Minas Gerais chegam a capital (Belo Horizonte).' },
    2: { year: '1921', title: 'Drummond como pontapé ao Modernismo na capital', description: 'Em 1921, Carlos Drummond de Andrade com influência dos poemas de Manual Bandeira, escreve poemas que viriam a ser os fundamentos a ideia do Modernismo.' },
    3: { year: '1923', title: 'Forma-se o grupo da capital mineira', description: 'Lançamento de livros e revistas importantes do modernismo mineiro.' },
    4: { year: '1924', title: 'Consolidação do Modernismo', description: 'O grupo se consolida na capital mineira.' },
    5: { year: '1925', title: 'criação de "A Revista"', description: 'Com dois anos de duração e três edições, A Revista é o verdadeiro modernismo representado atráves das primeiras publicações da escola literaria aqui em Minas Gerais.' },
    6: { year: '1927', title: 'Surge em Cataguases a revista "Verde"', description: 'Tirando o foco do modernismo da capital, a revista "Verde" surge como uma importante publicação em Cataguases para o modernismo e também como efeito literario na região.' },
    7: { year: '1928', title: 'Publica-se "Poemas Cronologicos" de Enrique Resende', description: 'Esta obra é um marco na poesia modernista mineira, trazendo uma nova perspectiva sobre a identidade e a cultura local.' },
    8: { year: '1929', title: 'O grupo se dispersa', description: 'Os polos como Rio de Janeiro e São Paulo e além de outros motivos fazem com que a primeira geração modernista mineira começasse a se afastar e buscar novos rumos.' }
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