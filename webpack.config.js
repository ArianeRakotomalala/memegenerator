const path = require('path');

module.exports = {
    entry: './src/index.js', // Point d'entrée dans src/
    output: {
        filename: 'bundle.js', // Nom du fichier de sortie
        path: path.resolve(__dirname, 'dist'), // Dossier de sortie
        publicPath: '/static/dist/', // Chemin public pour les assets
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                type: 'asset/resource',
                generator: {
                    filename: 'images/[name][ext]', // Dossier images dans dist/
                },
            },
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                    },
                },
            },
        ],
    },
    mode: 'development', // Mode de développement
};