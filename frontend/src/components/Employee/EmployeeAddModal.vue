<template>
  <div class="modal-overlay" v-if="isVisible" @click.self="close">
    <div class="modal-content">
      <button class="modal-close" @click="close">&times;</button>
      <div class="modal-header">
        <h2> <br/></h2>
      </div>
      <div class="modal-body">
      <div class="alert alert-danger" role="alert"  v-if="error">
        An error occurred while processing your request. Please check the information you entered and try again.
      </div>
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
import EmployeeForm from '@/components/Employee/EmployeeForm.vue';

export default {
  name: 'EmployeeAddModal',
  components: { EmployeeForm },
  props: {
    isVisible: Boolean,
    disabled: Boolean,
    error: Boolean,
  },
  data() {
    return {
      employee: {
        first_name: '',
        last_name: '',
        email: '',
        employee_type: 'regular',
        number_of_leaves: 0,
        benefits: [],
        contract_end_date: null,
        project: ''
      }
    };
  },
  methods: {
    close() {
      this.$emit('close');
    },
    async submit(data) {
      this.$emit('submit', data);
    }
  }
};
</script>
