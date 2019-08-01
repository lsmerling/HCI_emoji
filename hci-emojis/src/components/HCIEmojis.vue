<template>
    <div>
        <h1>{{ msg }}</h1>

        <!-- <el-button @click="visible = true">Button</el-button> -->
    <el-dialog :visible.sync="visible" title="Hello world">
      <p>SENT!</p>
    </el-dialog>
    <!-- <textarea  v-model="text1"></textarea> -->
<!-- <picker set="emojione" /> -->

<!-- <picker title="Pick your emoji…" emoji="point_up" /> -->
<!-- <picker :style="{ position: 'absolute', bottom: '20px', right: '20px' }" /> -->
<!-- <picker :i18n="{ search: 'Recherche', categories: { search: 'Résultats de recherche', recent: 'Récents' } }" /> -->


<el-row :gutter="20">
  <el-col :span="16">
      
      <div>
          <div id="showing-box1">
                {{message1}}
          </div>
          <div id="input-box1">
            <el-col :span="20"> 
                <el-input
                type="input"
                :rows="2"
                placeholder="请输入内容"
                resize = "none"
                v-model="user1textarea">
                <template slot="append"><el-button type="success" @click="submitTextUser1">Go</el-button></template>
                </el-input>
            </el-col>
            <el-col :span="4">
                
            </el-col>

</div></div>

          
      
      </el-col>
  <el-col :span="8"><div class="grid-content bg-purple"><picker @select="addEmojiUser1" /></div></el-col>
</el-row>

<el-row :gutter="20">
  <el-col :span="16"><div class="grid-content bg-purple"></div></el-col>
  <el-col :span="8"><div class="grid-content bg-purple"><picker @select="addEmoji" /></div></el-col>
</el-row>



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
        return {
            text1:'hello', 
            visible: false,
            message1:'',
            user1textarea:''
        }
  },
  methods: {
      addEmojiUser1(e){
          this.user1textarea = this.user1textarea + e.native;
      },
      submitTextUser1(){
          this.message1 = this.message1 + this.user1textarea;
      }
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
<style>
  .el-row {


  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    /* background: #99a9bf; */
  }
  .bg-purple {
    /* background: #d3dce6; */
  }
  .bg-purple-light {
    /* background: #e5e9f2; */
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    /* background-color: #f9fafc; */
  }
</style>