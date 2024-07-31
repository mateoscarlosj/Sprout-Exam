<template>
  <div class="modal-overlay" v-if="isVisible" @click.self="close">
    <div class="modal-content">
      <button class="modal-close" @click="close">&times;</button>
      <div class="modal-header">
        <h2>Employee Information</h2>
      </div>
      <div class="modal-body">
        <div v-if="employee">
          <p><strong>First Name:</strong> {{ employee.first_name }}</p>
          <p><strong>Last Name:</strong> {{ employee.last_name }}</p>
          <p><strong>Email:</strong> {{ employee.email }}</p>
          <p><strong>Employee Type:</strong> {{ employee.employee_type }}</p>
          <p v-if="employee.employee_type === 'regular'">
            <strong>Number of Leaves:</strong> {{ employee.number_of_leaves }}
          </p>
          <p v-if="employee.employee_type === 'contractual'">
            <strong>Contract End Date:</strong> {{ employee.contract_end_date }}
          </p>
        </div>
      </div>
      <div class="modal-footer">
        <button @click="close" class="btn btn-primary">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EmployeeModal',
  props: {
    isVisible: Boolean,
    employee: Object
  },
  methods: {
    close() {
      this.$emit('close');
    }
  }
};
</script>
