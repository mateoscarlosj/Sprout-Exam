<template>
  <div class="container mt-4">
    <table class="table">
      <thead>
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Email</th>
          <th>Position</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(employee, index) in employees" :key="employee.id">
          <td>{{ index + 1 }}</td>
          <td>{{ employee.first_name + ' ' + employee.last_name }}</td>
          <td>{{ employee.email }}</td>
          <td>{{ employee.position }}</td>
          <td>
            <button class="btn btn-view" @click="view(employee.id)">View</button>
            <button class="btn btn-edit" @click="edit(employee.id)">Edit</button>
            <button class="btn btn-delete" @click="openDeleteModal(employee.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Confirmation Modal -->
    <ConfirmationModal
      v-if="showDeleteModal"
      :isVisible="showDeleteModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this employee?"
      @confirm="deleteEmployee"
      @close="closeDeleteModal"
    />
  </div>
</template>

<script>
import ConfirmationModal from '@/components/ConfirmationModal.vue';

export default {
  name: 'EmployeeList',
  components: { ConfirmationModal },
  props: {
    employees: Array
  },
  data() {
    return {
      employeeToDelete: null,
      showDeleteModal: false
    };
  },
  methods: {
    view(id) {
      this.$emit('view', id);
    },
    edit(id) {
      this.$emit('edit', id);
    },
    openDeleteModal(id) {
      this.employeeToDelete = id;
      this.showDeleteModal = true;
    },
    closeDeleteModal() {
      this.showDeleteModal = false;
      this.employeeToDelete = null;
    },
    deleteEmployee() {
      this.$emit('delete', this.employeeToDelete);
      this.closeDeleteModal();
    }
  }
};
</script>

<style scoped>
.table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 2em;
}

.table th, .table td {
  padding: 1em;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.table th {
  background-color: #007bff;
  color: #fff;
}

.table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.table tr:hover {
  background-color: #f1f1f1;
}

.table td button {
  margin-right: 0.5em;
}

.btn {
  border: none;
  border-radius: 4px;
  padding: 0.5em 1em;
  cursor: pointer;
  font-size: 0.875em;
  color: #fff;
}

.btn-view {
  background-color: #17a2b8;
}

.btn-edit {
  background-color: #ffc107;
}

.btn-delete {
  background-color: #dc3545;
}

.btn-view:hover {
  background-color: #138496;
}

.btn-edit:hover {
  background-color: #e0a800;
}

.btn-delete:hover {
  background-color: #c82333;
}
</style>
