<template>
  <div class="d-flex">
    <!-- <Sidebar :open="sidebarOpen" @toggle="toggleSidebar" /> -->
    <div class="flex-grow-1">
      <Header :open="sidebarOpen" @toggle="toggleSidebar" />
      <main class="container mt-3">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script>
import Header from '../components/AppHeader.vue';
// import Sidebar from '../components/AppSidebar.vue';

export default {
  components: {
    Header,
  },
  data() {
    return {
      sidebarOpen: true,
    };
  },
  methods: {
    toggleSidebar() {
      this.sidebarOpen = !this.sidebarOpen;
    },
  },
};
</script>

<style>
/* Adjust layout styling as needed */
</style>
