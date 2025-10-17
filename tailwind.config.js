/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./core/templates/**/*.html",
    "./**/templates/**/*.html", // Se você tiver templates em outros apps
    "./*.html",
    "./**/forms.py",
    "./**/views.py",
  ],
  theme: {
    extend: {
      fontFamily: {
        montserrat: ["Montserrat", "Arial", "sans-serif"],
        ptsans: ["PT Sans", "Arial", "sans-serif"],
      },
      colors: {
        gray: {
          900: '#1a1a1a'
        },
        'dark-bg': '#2C2C2C',
        green: {
          1000: '#1B5144',
          550: '#667C3D',
    },
        bege: {
          900: '#D9BF9E',
          800: '#E6CFC0',
          700: '#F2E0D3',
          600: '#FDF4E7',
        },
        cafe: {
          900: '#3B2A20',
          800: '#4D3B2C',
          700: '#6A4F3A',
          600: '#8A6B4C',
        },
        // Brand palette aligned with theme.css variables
        brand: {
          primary: {
            600: '#14532D',
            700: '#0F3F24',
            800: '#0B3B1E',
          },
          accent: {
            500: '#2563EB',
            600: '#1D4ED8',
            700: '#073B73',
          },
          gold: {
            400: '#C2A349',
          },
        },
        paper: '#FAFAF7',
        surface: '#FFFFFF',
        ink: '#111827',
  },
}  },
  plugins: [],
}