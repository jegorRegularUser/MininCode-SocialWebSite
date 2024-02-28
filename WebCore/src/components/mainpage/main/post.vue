<template>
<div class="last-posts" v-for="item in props.posts[0]" >
  <article class="last-post">
        <div>
          <header>
            <ul class="last-post-tegs">
              <li v-for="tag in item.tags"> <a class="last-post-teg">{{tag}}</a></li>
            </ul>
            <h4>
              <a class="last-post-title">{{item.title}}</a>
            </h4>
            <div class="time-with-author">
              <time class="last-post-time" datetime="2018-10-01">{{format_date(item.date_of_creation)}}</time>
              <a :href="'/users/' + item.username"><span> {{item.username}}</span></a>
            </div>
          </header>
          <p class="last-post-text">{{item.description}}
          </p>
        </div>
  </article>
</div>
</template>
<script setup>
const props = defineProps({
  posts: []
});

function format_date(date) {
  let now = new Date(date);
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  const hour = String(now.getHours()).padStart(2, '0');
  const minute = String(now.getMinutes()).padStart(2, '0');
  const second = String(now.getSeconds()).padStart(2, '0');

  return `${year}-${month}-${day} ${hour}:${minute}:${second}`
}

</script>


<style scoped>
.last-posts {
  display: flex;
  flex-wrap: wrap;
}

.last-post {
  width: 470px;
  display: flex;
  margin-bottom: 65px;
  text-align: left;
  background: #BDECB6;
  border-radius: 7px;
  padding: 10px;
  
}


.last-post-tegs {
  list-style: none;
  margin-bottom: 15px;
  padding-left: 0;
  display: flex;
  flex-wrap: wrap;
}
.last-post-teg {
  font-family: "OpenSans-Bold";
  text-transform: uppercase;
  color: #b59f5b;
  font-size: 14px;
  margin-right: 20px;
    max-width: 100px;
}
.last-post-teg:hover {
  text-decoration: underline;
}
.last-post-title {
  font-family: "OpenSans-Bold";
  text-transform: uppercase;
  font-size: 20px;
  margin-bottom: 10px;
  
}
.last-post-title:hover {
  color: #b59f5b;
}
.time-with-author {
  display: flex;
  font-family: "OpenSans-Bold";
  font-size: 12px;
  margin-bottom: 15px;
}
.last-post-time {
  font-family: "OpenSans-Regular";
  color: #9c9c9c;
  font-size: 12px;
  margin-right: 15px;
}
.last-post-text {
  font-family: "OpenSans-Regular";
  font-size: 15px;
}
</style>