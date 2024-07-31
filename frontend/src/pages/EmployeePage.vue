<template>
  <div class="container mt-4">
    <div class="d-flex justify-content-end mb-2">
      <button @click="showAddModal = true" class="btn btn-primary">
        Add Employee
      </button>
    </div>
    <div class="mt-2">
      <EmployeeList
        :employees="employees"
        @view="viewEmployee"
        @edit="editEmployee"
        @delete="handleDelete"
      />
    </div>

    <EmployeeModal
      :isVisible="showModal"
      :employee="selectedEmployee"
      @close="closeModal"
    />

    <EmployeeAddModal
      :isVisible="showAddModal"
      :error="showError"
      @close="closeModal"
      @submit="handleAddEmployee"
    />

    <EmployeeEditModal
      :isVisible="showEditModal"
      :employeeData="employeeForEdit"
      :error="showError"
      @close="closeModal"
      @submit="handleEditEmployee"
    />
  </div>
</template>

<script>
import { computed, onMounted, ref } from 'vue';
import { useStore } from 'vuex';
import EmployeeList from '@/components/Employee/EmployeeList.vue';
import EmployeeModal from '@/components/Employee/EmployeeModal.vue';
import EmployeeAddModal from '@/components/Employee/EmployeeAddModal.vue';
import EmployeeEditModal from '@/components/Employee/EmployeeEditModal.vue';
import { postApi, putApi } from '../api/employee';

export default {
  name: 'EmployeePage',
  components: {
    EmployeeList,
    EmployeeModal,
    EmployeeAddModal,
    EmployeeEditModal
  },
  setup() {
    const store = useStore();
    const showModal = ref(false);
    const showAddModal = ref(false);
    const showEditModal = ref(false);
    const showError = ref(false);
    const selectedEmployee = ref(null);
    const employeeForEdit = ref(null);

    const employees = computed(() => store.getters['employees/allEmployees']);
    onMounted(() => {
      store.dispatch('employees/fetchEmployees');
    });

    const viewEmployee = (id) => {
      const employee = employees.value.find(emp => emp.id === id);
      selectedEmployee.value = employee;
      showModal.value = true;
    };

    const editEmployee = (id) => {
      const employee = employees.value.find(emp => emp.id === id);
      employeeForEdit.value = employee;
      console.log(employeeForEdit.value)
      showEditModal.value = true;
    };

    const handleAddEmployee = async (data) => {
      try {

        await postApi('employees', data);
        showAddModal.value = false;
        store.dispatch('employees/fetchEmployees');
      } catch (error) {
        console.error('Failed to add employee:', error.message);
        showError.value = true;
      }
    };

    const handleEditEmployee = async (data) => {
      try {
        await putApi(`employees/${employeeForEdit.value.id}`, data);
        showEditModal.value = false;
        store.dispatch('employees/fetchEmployees'); // Refresh employee list
      } catch (error) {
        console.error('Failed to edit employee:', error.message);
        showError.value = true;
      }
    };

    const handleDelete = async (id) => {
      try {
        await store.dispatch('employees/deleteEmployee', id);
        store.dispatch('employees/fetchEmployees'); // Refresh employee list
      } catch (error) {
        console.error('Failed to delete employee:', error.message);
      }
    };

    const closeModal = () => {
      showModal.value = false;
      selectedEmployee.value = null;
      showEditModal.value = false;
      showAddModal.value = false;
      employeeForEdit.value = null;
    };

    return {
      employees,
      viewEmployee,
      editEmployee,
      handleDelete,
      showModal,
      showAddModal,
      showEditModal,
      selectedEmployee,
      employeeForEdit,
      handleAddEmployee,
      handleEditEmployee,
      closeModal,
      showError
    };
  }
};
</script>
