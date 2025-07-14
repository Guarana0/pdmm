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
      colors: {
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
  },
}  },
  plugins: [],
}