<template>
  <div>
    <div class="form-box">
      <h2 class="text-center mb-4">{{ formTitle }}</h2>
      <form @submit.prevent="handlerSubmit">
        <div class="form-group">
          <label for="first_name">First Name</label>
          <input
            id="first_name"
            v-model="form.first_name"
            placeholder="First Name"
            type="text"
            :disabled="disabled"
          />
        </div>
        <div class="form-group">
          <label for="last_name">Last Name</label>
          <input
            id="last_name"
            v-model="form.last_name"
            placeholder="Last Name"
            type="text"
            :disabled="disabled"
          />
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input
            id="email"
            v-model="form.email"
            placeholder="Email"
            type="email"
            :disabled="disabled"
          />
        </div>
        <div class="form-group">
          <label for="employee_type">Employee Type</label>
          <select
            id="employee_type"
            v-model="form.employee_type"
            :disabled="disabled"
          >
            <option value="regular">Regular</option>
            <option value="contractual">Contractual</option>
          </select>
        </div>
        <div class="form-group" v-if="form.employee_type === 'regular'">
          <label for="number_of_leaves">Number of Leaves</label>
          <input
            id="number_of_leaves" 
            v-model.number="form.number_of_leaves" 
            type="number" 
            :disabled="disabled" 
          />
        </div>
        <div class="form-group" v-if="form.employee_type === 'regular'">
          <label for="benefits">Benefits</label>
          <select 
            id="benefits" 
            v-model="form.benefits" 
            multiple 
            :disabled="disabled"
          >
            <option value="Health Insurance">Health Insurance</option>
            <option value="13th Month Pay">13th Month Pay</option>
            <option value="Paid Leave">Paid Leave</option>
            <option value="Gym Membership">Gym Membership</option>
          </select>
        </div>
        <div class="form-group" v-if="form.employee_type === 'contractual'">
          <label for="contract_end_date">Contract End Date</label>
          <input
            id="contract_end_date"
            v-model="form.contract_end_date"
            type="date"
            :disabled="disabled"
          />
        </div>
        <div class="form-group" v-if="form.employee_type === 'contractual'">
          <label for="project">Project</label>
          <input 
            id="project" 
            v-model="form.project" 
            placeholder="Project" 
            type="text" 
            :disabled="disabled" 
          />
        </div>
        <div class="form-footer">
          <button class="btn btn-primary" type="submit" :disabled="disabled">Submit</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "EmployeeForm",
  props: {
     data: {
      type: Object,
      default: () => ({
        first_name: '',
        last_name: '',
        email: '',
        employee_type: 'regular',
        number_of_leaves: 0,
        benefits: [],
        contract_end_date: null,
        project: ''
      })
    },
    disabled: {
      type: Boolean,
      default: false
    },
    isVisible: {
      type: Boolean,
      default: false
    },
    formTitle: {
      type: String,
      default: 'Employee Form'
    }
  },
  data() {
    return {
      form: { ...this.data }
    };
  },
  watch: {
    data: {
    //   handler(newData) {
    //     this.form = { ...newData };
    //   },
      deep: true
    }
  },
  methods: {
    handlerSubmit() {
      this.$emit('submit', { ...this.form });
    }
  }
};
</script>
<style scoped>
.form-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f2f5;
}

.form-box {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  width: 100%;
  max-width: 600px;
}

h2 {
  font-size: 1.75rem;
  color: #333;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-size: 0.875rem;
  margin-bottom: 0.5rem;
  color: #555;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 0.75rem;
  border-radius: 4px;
  border: 1px solid #ddd;
  box-sizing: border-box;
}

.form-group input:focus,
.form-group select:focus {
  border-color: #007bff;
  outline: none;
}

.form-footer {
  margin-top: 1.5rem;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  color: #fff;
  padding: 0.75rem;
  font-size: 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
  width: 100%;
  text-align: center;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #004085;
}
</style>
