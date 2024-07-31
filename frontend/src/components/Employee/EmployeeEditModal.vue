<template>
  <div class="modal-overlay" v-if="isVisible" @click.self="close">
    <div class="modal-content">
      <button class="modal-close" @click="close">&times;</button>
      <div class="modal-header">
        <h2><br/></h2>
      </div>
      <div class="modal-body">
        <EmployeeForm
          :data="employee"
          @submit="submit"
          :disabled="disabled"
        />
      </div>
    </div>
  </div>
</template>

<script>
import EmployeeForm from '@/components/Employee/EmployeeForm.vue'; // Adjust path if necessary
import { ref, watch } from 'vue';

export default {
  name: 'EmployeeEditModal',
  components: { EmployeeForm },
  props: {
    isVisible: Boolean,
    employeeData: Object,
    disabled: Boolean
  },
  methods: {
    close() {
      this.$emit('close');
    },
    async submit(data) {
      this.$emit('submit', data);
    }
  },
  setup(props) {
    console.log("panigt", props);
    const employee = ref(props.employeeData);
    watch(() => props.employeeData, (newData) => {
      employee.value = { ...newData };
    }, { deep: true });

    return {
      employee,
    };
  }
};
</script>