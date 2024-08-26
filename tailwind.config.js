const config = {
    content: [
        "./server/*.py",
        "./server/components/*.py",
        "./server/pages/*.py",
        "./public/js/*.js"
    ],
    theme: {
        extend: {
            colors: {
                "app-background": "#121212",
                "app-layer-background": "#444444",
                "app-layer-background-hover": "#666666",

                "app-accent": "#DC6ACF",
                "app-accent-hover": "#ECACE4",

                "app-text-main": "#ffffff",

                "app-input-background": "#444444",
                "app-input-text": "#bababa",
            }
        }
    },
    plugins: [],
};

try {
    tailwind.config = config;
} catch {
    module.exports = config;
}