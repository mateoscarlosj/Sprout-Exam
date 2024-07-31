<template>
  <nav class="sidebar">
    <div class="d-flex justify-content-between align-items-center p-3">
      <h5>Employee Management</h5>
    </div>
    <ul class="list-group">
      <li class="list-group-item"><router-link to="/employees">Employees</router-link></li>
    </ul>
  </nav>
</template>

<style scoped>
.sidebar {
  width: 240px;
  background-color: #f8f9fa;
  height: 100vh;
}
</style>
