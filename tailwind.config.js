/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./core/templates/**/*.html",
    "./**/templates/**/*.html", // Se você tiver templates em outros apps
    "./*.html",
    "./**/forms.py",
    "./**/views.py",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}