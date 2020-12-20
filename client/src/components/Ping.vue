<template>
  <div class="container">
    <p>Listed in the follow are all the current references</p>
    <button type="button" class="btn btn-primary">pong</button>
    {{msg}}
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/api/v1/references';
      axios.get(path)
        .then((res) => {
          this.msg = res.data.items;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
