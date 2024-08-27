const config = {
  darkMode: "selector",
  content: [
    "./server/*.py",
    "./server/components/*.py",
    "./server/pages/*.py",
    "./public/js/*.js",
  ],
  theme: {
    extend: {
      colors: {
        "app-bg": "#ffffff",
        "app-dark-bg": "#000000",

        "app-bg-hover": "#555555",
        "app-dark-bg-hover": "#aaaaaa",

        "app-accent": "#00A7E1",
        "app-dark-accent": "#8300E0",

        "app-accent-hover": "#8300E0",
        "app-dark-accent-hover": "#00A7E1",

        "app-text": "#000000",
        "app-dark-text": "#ffffff",

        "app-input": "#dadada",
        "app-dark-input": "#222222",

        "app-input-text": "#000000",
        "app-dark-input-text": "#ffffff",
      },
      textShadow: {
        sm: "0 1px 2px var(--tw-shadow-color)",
        DEFAULT: "0 2px 4px var(--tw-shadow-color)",
        lg: "0 8px 16px var(--tw-shadow-color)",
      },
    },
  },
  plugins: [
    function ({ matchUtilities, theme }) {
      matchUtilities(
        {
          "text-shadow": (value) => ({
            textShadow: value,
          }),
        },
        {
          values: theme("textShadow"),
        }
      );
    },
  ],
};

try {
  tailwind.config = config;
} catch {
  module.exports = config;
}
