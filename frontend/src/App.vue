<script>
import { ref, onMounted } from 'vue';
import api from './services/api';

const backend_status = ref("Checking ....")
const backend_message = ref("Connecting to CollecBuy backend server...")

onMounted(async () => {
    try {
        const response = await api.get('/health');

        backend_status.value = response.data.status;
        backend_message.value = response.data.service;
    } catch (error) {
        backend_status.value = "Error";
        backend_message.value = "Failed to connect to CollecBuy backend server.";

    }
});

</script>

<template>
    <main class="app">
        <h1>CollecBuy</h1>

        <p class="tagline">Buy Together. Pay Less.</p>

        <section class="status-card">
            <h2>Backend Connection</h2>

            <p>
                Status: <strong>{{ backend_status }}</strong>
            </p>

            <p>{{ backend_message }}</p>
        </section>
    </main>
</template>

<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f5f7fb;
}

.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 24px;
}

h1 {
  color: #155eef;
  font-size: 48px;
  margin-bottom: 5px;
}

.tagline {
  color: #667085;
  font-size: 18px;
}

.status-card {
  margin-top: 30px;
  padding: 28px;
  width: 100%;
  max-width: 420px;
  background: white;
  border-radius: 14px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
}

.status-card h2 {
  color: #202939;
}

.status-card p {
  color: #475467;
}
</style>