<!-- src/components/MetricsViewer.vue -->
<template>
  <div class="mb-4">
    <h2 class="mb-3">Metrics</h2>
    <div v-if="metrics" class="row">
      <div class="col-md-4 mb-3" v-for="(value, key) in metrics" :key="key">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{{ formatKey(key) }}</h5>
            <p class="card-text">{{ value }}</p>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <p>No metrics available. Click "Refresh Metrics" to fetch the latest data.</p>
    </div>
    <div class="d-flex justify-content-end">
      <button @click="fetchMetrics" class="btn btn-secondary float-end">Refresh Metrics</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      metrics: null
    };
  },
  methods: {
    async fetchMetrics() {
      console.log("this.http", this.$http);
      try {
        const response = await this.$http.get('/monitoring');
        this.metrics = response.data;
      } catch (error) {
        alert('Error fetching metrics!');
        console.error(error);
      }
    },
    formatKey(key) {
      // Convert snake_case to Title Case for display
      return key.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
    }
  },
  mounted() {
    this.fetchMetrics();
  }
};
</script>

<style scoped>
.card {
  /* You may add additional styling for the cards here if desired */
}
</style>

