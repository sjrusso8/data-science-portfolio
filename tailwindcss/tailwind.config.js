module.exports = {
    purge: {
        enabled: true,
        content: ['../django-website/**/templates/*.html'],
    },
    darkMode: false, // or 'media' or 'class'
    theme: {
        colors: {
            black: "#000",
            white: "#fff",
            gray: {
                100: "f5f5f5",
                500: "e5e5e5",
                700: "e0e0e0",
                900: "b8b8b8"
            },
            red: "#df2e01",
            orange: {
                100: "#FDB849",
                300: "#FDA821",
                500: "#F29602",
                700: "#CA7D02",
                900: "#A26402"
            },
            metal: {
                500: "#002E3d",
                700: "#001F29"
            }
        },
        extend: {},
    },
    variants: {
        extend: {},
    },
    plugins: [],
}