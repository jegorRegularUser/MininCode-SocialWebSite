<template>
  <router-view/>
</template>

<style>
@font-face {
  font-family: "OpenSans-Regular";
  src: url("https://netology-code.github.io/html-2-diploma/sources/fonts/OpenSans-Regular.woff")
    format("woff");
  font-weight: 400;
  font-style: normal;
}
@font-face {
  font-family: "OpenSans-Bold";
  src: url("https://netology-code.github.io/html-2-diploma/sources/fonts/OpenSans-Bold.woff")
    format("woff");
  font-weight: 700;
  font-style: normal;
}
#app {
  font-family: "OpenSans-Bold";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
*{
    margin: 0;
}
a {
  color: black;
  text-decoration: none;
}
</style>
