<template>
<div>
  <div class="copyright">Copyright © 2021–2023 City Blog LLC.</div>
</div>
</template>

<script setup>
</script>

<style scoped>
.footer {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 50px;
  background-color: #f4f7f6;
  text-align: center;
  vertical-align: middle;
  
}

.copyright {
  width: 100%;
  height: 50px;
  display: flex;
  flex-direction: column; 
  align-items: center;
  text-align: center;
  font-size: 13px;
  font-family: 'OpenSans-Bold';
  color: #a1a1a1;
  background-color: #f4f7f6;
  justify-content: center;
}
.hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  border: 0;
  clip: rect(0 0 0 0);
  overflow: hidden;
}

</style>