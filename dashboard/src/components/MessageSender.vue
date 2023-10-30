<!-- src/components/MessageManager.vue -->
<template>
  <div>
    <h2>Messages</h2>
    
    <!-- Send Message Form -->
    <div class="mb-4">
      <form @submit.prevent="sendMessage">
        <div class="row mb-3">
          <div class="col">
            <div class="input-group">
              <label for="topic" class="input-group-text">Topic</label>
              <input type="text" class="form-control" v-model="topic" id="topic" required />
            </div>
          </div>
        </div>
        <div class="row mb-3">
          <div class="col">
            <div class="input-group">
              <label for="message" class="input-group-text">Send Message</label>
              <input type="text" class="form-control" v-model="message" id="message" required />
              <button type="submit" class="btn btn-primary">Send</button>
            </div>
          </div>
        </div>
      </form>
    </div>
    
    <!-- Received Messages Table -->
    <div>
      <button @click="receiveMessages" class="btn btn-link mb-2">Update Messages</button>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col" class="w-75">Message</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(message, index) in messages" :key="index">
            <th scope="row">{{ index + 1 }}</th>
            <td>{{ message }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      topic: '',
      message: '',
      messages: []
    };
  },
  methods: {
    async sendMessage() {
      try {
        await this.$http.post(`/send/${this.topic}`, { message: this.message });
        alert('Message sent successfully!');
        this.message = ''; // Clear the message input after sending
      } catch (error) {
        alert('Error sending message!');
        console.error(error);
      }
    },
    async receiveMessages() {
      try {
        console.log("topic " + this.topic);
        const response = await this.$http.get(`/receive/${this.topic}`);
        this.messages = response.data.messages;
      } catch (error) {
        alert('Error receiving messages!');
        console.error(error);
      }
    }
  }
};
</script>

