const config = {
    content: [
        "./server/*.py",
        "./server/components/*.py",
        "./server/pages/*.py",
    ],
    theme: {
        extend: {
            colors: {
                "color1": "#9290C3",
                "color2": "#1B1A55",
                "color3": "#535C91",
                "color4": "#070F2B",

                "button": "#00ff00",
                "button-hover": "#0000ff",
                "button-text": "#ffffff",

                "textcolor1": "#ffffff",
                "textcolor2": "#0000ff",
                "textcolor3": "#00ff00",
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