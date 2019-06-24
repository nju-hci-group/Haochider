<template>
  <div class="num-div">
    <button class="minus" @click="minus">-</button>
    <input
      class="quantity"
      min="1"
      v-model="innerValue"
      @input="$emit('input', innerValue ? parseInt(innerValue) : 0)"
    >
    <button class="plus" @click="plus">+</button>
  </div>
</template>

<script>
export default {
  name: 'NumInput',
  props: {
    'value': Number
  },
  data: function () {
    return {
      innerValue: this.value
    }
  },
  watch: {
    value: function (newValue, oldValue) {
      this.innerValue = newValue
    }
  },
  methods: {
    plus: function () {
      let value = parseInt(this.innerValue) + 1
      this.$emit('input', value)
    },
    minus: function () {
      let value = parseInt(this.innerValue) - 1
      if (value >= 0) {
        this.$emit('input', value)
      }
    }
  }
}
</script>

<style scoped>
  .minus {
    width: 25px;
    height: 24px;
    border-radius: 20px 0 0 20px;
    border-right: 1px solid #b6b8bf;
    background-color: #d7d6d6;
    color: #2070ef;
    outline: 0;
  }
  .quantity {
    width: 25px;
    height: 24px;
    border: 0;
    text-align: center;
    outline: 0;
  }
  .plus {
    width: 25px;
    height: 24px;
    border-radius: 0 20px 20px 0;
    border-left: 1px solid #b6b8bf;
    background-color: #d7d6d6;
    color: #2070ef;
    outline: 0;
  }
  .num-div {
    height: 26px;
    border: 1px solid #b6b8bf;
    border-radius: 20px 20px;
    outline: 0;
    vertical-align: center;
    align-content: center;
  }
</style>
