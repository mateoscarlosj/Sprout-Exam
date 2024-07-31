<template>
  <div id="app">
    <main :class="['main-content', { 'sidebar-open': sidebarOpen }]">
      <router-view />
    </main>
  </div>
</template>

<style scoped>
#app {
  display: flex;
  height: 100vh;
}

.main-content {
  flex-grow: 1;
  transition: margin-left 0.3s;
}

.sidebar-open .main-content {
  margin-left: 240px; /* Adjust according to sidebar width */
}
</style>
