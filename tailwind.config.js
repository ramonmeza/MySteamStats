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
      /* https://materialtheme.arcsine.dev/ */
      colors: {
        /* dark- prefix used for dark mode */
        /* text colors */
        dark: "#121212",
        light: "#ededed",

        primary: "#b317d6",
        "primary-hover": "#e8b9f3",
        "primary-active": "#9a0dc6",

        /* menu colors */
        "menu-item": "#ffffff",
        "dark-menu-item": "#1f1f1f",
        "menu-item-hover": "#dbdbdb",
        "dark-menu-item-hover": "#262626",
        "menu-item-active": "#bdbdbd",
        "dark-menu-item-active": "#303030",
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
