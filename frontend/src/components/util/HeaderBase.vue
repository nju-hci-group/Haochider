<template>
  <v-flex xs12 style="margin-bottom: 60px">
    <v-toolbar dark color="blue" app height="60">
      <v-toolbar-items>
        <v-btn flat style="padding: 0">
          <v-img
            :src="require('../../assets/logo.png')"
            max-height="100"
            max-width="100"
          ></v-img>
        </v-btn>
        <slot name="left-part"></slot>
      </v-toolbar-items>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <slot></slot>
      </v-toolbar-items>
    </v-toolbar>
  </v-flex>
</template>

<script>
export default {
  name: 'HeaderBase',
  data: function () {
    return {
    }
  }
}
</script>

<style scoped>

</style>
