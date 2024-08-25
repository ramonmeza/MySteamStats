const config = {
    content: [
        "./server/*.py",
        "./server/components/*.py",
        "./server/pages/*.py",
    ],
    theme: {
        extend: {
            colors: {
                "bggradient1": "#818181",
                "bggradient2": "#32292F",
                "bggradient3": "#32292F",
                "bggradient4": "#120F11",

                "button": "#5299D3",
                "button-hover": "#9EC6FF",
                "button-text": "#ffffff",

                "header": "#5299D3",

                "textmain": "#ffffff",
                "textalt": "#0B5563",
                "textlink": "#5299D3",
                "textlinkhover": "#A7C9E4",

                //
                "app-background": "#a",
                "app-button": "#"
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