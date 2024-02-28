const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  devServer: {

    proxy: {
      '/api': {
        target: 'https://a721-89-178-124-63.ngrok-free.app',
        ws: true,
        changeOrigin: true
      },
      'create_post': {
        target: 'https://a721-89-178-124-63.ngrok-free.app',
        ws: true,
        changeOrigin: true
      },
      '/auth/login': {
        target: 'https://a721-89-178-124-63.ngrok-free.app',
        ws: true,
        changeOrigin: true
      },
      '/auth/logout': {
        target: 'https://a721-89-178-124-63.ngrok-free.app',
        ws: true,
        changeOrigin: true
      },
      '/auth/registration': {
        target: 'https://a721-89-178-124-63.ngrok-free.app',
        ws: true,
        changeOrigin: true
      },
      '/auth/check_auth': {
        target: 'https://a721-89-178-124-63.ngrok-free.app',
        ws: true,
        changeOrigin: true
      }
    }

  }
}