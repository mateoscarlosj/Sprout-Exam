<template>
  <header class="header">
    <div class="header-content">
      <h4 class="header-title">Employees</h4>
      <button class="btn btn-logout" @click="logout">Logout</button>
    </div>
  </header>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  methods: {
    ...mapActions('auth', ['logout']),
    async handleLogout() {
      try {
        await this.logout();
        this.$router.push('/login'); // if using Vue Router
      } catch (error) {
        console.error('Logout error:', error);
      }
    }
  }
};
</script>

<style scoped>
.header {
  background-color: #343a40;
  color: #fff;
  padding: 0.75em 1.5em;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-title {
  font-size: 1.5em;
  margin: 0;
}

.btn-logout {
  background-color: #dc3545;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 0.5em 1em;
  cursor: pointer;
  font-size: 1em;
  font-weight: 600;
  transition: background-color 0.3s, color 0.3s;
}

.btn-logout:hover {
  background-color: #c82333;
}
</style>
