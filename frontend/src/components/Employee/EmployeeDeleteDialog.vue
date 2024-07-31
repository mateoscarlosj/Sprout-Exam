<template>
  <b-modal
    :visible="open"
    @hide="onClose"
    title="Delete"
    size="sm"
    ok-title="Yes"
    cancel-title="No"
    ok-variant="danger"
    @ok="handleDelete"
    @cancel="onClose"
  >
    <p>
      Are you sure you want to delete <strong>{{ data?.first_name }} {{ data?.last_name }}</strong>?
    </p>
  </b-modal>
</template>

<script>
export default {
  name: "EmployeeDeleteDialog",
  props: {
    open: {
      type: Boolean,
      required: true
    },
    data: {
      type: Object,
      required: true
    }
  },
  methods: {
    onClose() {
      this.$emit('close');
    },
    handleDelete() {
      this.$emit('submit', this.data?.id);
    }
  }
}
</script>
