<template>
    <div>
        <h1>{{ msg }}</h1>

        <el-button @click="visible = true">Button</el-button>
    <el-dialog :visible.sync="visible" title="Hello world">
      <p>Try Element</p>
    </el-dialog>
<!-- <picker set="emojione" /> -->
<picker @select="addEmoji" />
<!-- <picker title="Pick your emoji…" emoji="point_up" /> -->
<!-- <picker :style="{ position: 'absolute', bottom: '20px', right: '20px' }" /> -->
<!-- <picker :i18n="{ search: 'Recherche', categories: { search: 'Résultats de recherche', recent: 'Récents' } }" /> -->

    </div>
</template>

<script>
import { Picker } from 'emoji-mart-vue'
export default {
  name: 'HelloWorld',
  components:{
      Picker
  },
  props: {
    msg: String
  },
  data: function() {
        return { visible: false }
      }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
