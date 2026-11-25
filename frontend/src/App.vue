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