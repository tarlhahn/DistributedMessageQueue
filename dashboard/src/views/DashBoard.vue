<!-- src/views/DashBoard.vue -->
<template>
  <div id="app" class="container mt-5">
    <h1 class="mb-4">Dashboard</h1>
    <div class="row">
      <MetricsViewer />
      <MessageSender />
    </div>
  </div>
</template>

<script>
import MessageSender from '../components/MessageSender.vue';
import MetricsViewer from '../components/MetricsViewer.vue';

export default {
  components: {
    MessageSender,
    MetricsViewer
  }
};
</script>

<style scoped>
h1, h2 {
  color: #495057;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
