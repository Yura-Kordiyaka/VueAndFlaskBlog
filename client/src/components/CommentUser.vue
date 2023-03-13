<template>
  <div>
      <ul>
      <li v-for="(item, index) in all_post" :key="index">
        <ul v-for="(items,index) in all_comments_get" :key="index">
          <div v-if="item.id===items.post_id">
            {{items}}
          </div>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "CommentUser",
  props: {
    all_comments_get: {
      type: Array,
    },
    all_post:{
      type:Array,
    }
  }
}
</script>

<style scoped>
li{
  list-style: none;
}
</style>