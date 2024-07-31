<template>
  <div v-if="isVisible" class="confirm-modal-overlay" @click.self="close">
    <div class="confirm-modal-content">
      <button class="confirm-modal-close" @click="close">&times;</button>
      <div class="confirm-modal-header">
        <h2>{{ title }}</h2>
      </div>
      <div class="confirm-modal-body">
        <p>{{ message }}</p>
      </div>
      <div class="confirm-modal-footer">
        <button class="btn btn-primary" @click="confirm">Confirm</button>
        <button class="btn btn-outline-secondary" @click="close">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ConfirmationModal',
  props: {
    isVisible: Boolean,
    title: {
      type: String,
      default: 'Confirm'
    },
    message: {
      type: String,
      default: 'Are you sure you want to proceed?'
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
    confirm() {
      this.$emit('confirm');
    }
  }
};
</script>
<style scoped>
.confirm-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  justify-content: center;
  align-items: center;
}

.confirm-modal-content {
  background: #fff;
  border-radius: 8px;
  max-width: 500px;
  width: 90%;
  padding: 1.5em;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  position: relative;
}

.confirm-modal-header {
  font-size: 1.5em;
  color: #333;
  margin-bottom: 1em;
}

.confirm-modal-close {
  position: absolute;
  top: 1em;
  right: 1em;
  background: none;
  border: none;
  font-size: 1.5em;
  color: #666;
  cursor: pointer;
}

.confirm-modal-close:hover {
  color: #000;
}

.confirm-modal-body {
  margin-bottom: 1.5em;
}

.confirm-modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 0.5em;
}

.btn {
  border: none;
  border-radius: 4px;
  padding: 0.75em 1.5em;
  cursor: pointer;
  font-size: 1em;
  font-weight: 600;
  transition: background-color 0.3s, color 0.3s;
}

.btn-confirm {
  background-color: #28a745;
  color: #fff;
}

.btn-confirm:hover {
  background-color: #218838;
}

.btn-cancel {
  background-color: #dc3545;
  color: #fff;
}

.btn-cancel:hover {
  background-color: #c82333;
}
</style>
