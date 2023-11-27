<template>
  <table class="table table-hover">  
    <thead>
    </thead>
    <tbody>
      <tr class="tr">
        <h4 class="h4"><RouterLink :to="{ name: 'DetailView', params: { id: article.id } }">{{ article.title }}</RouterLink></h4>
      </tr>
        <hr>
    </tbody>
  </table>  
</template>

<script setup>
import { RouterLink } from "vue-router";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
defineProps({
  article: Object,
});
</script>


<style scoped>
.h4 > a{
  text-decoration: none;
  text-decoration-line: none;
  color: black;
}
</style>
