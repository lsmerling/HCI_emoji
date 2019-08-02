<template>
    <div>
        <h1>{{ msg }}</h1>


<el-row :gutter="20">
  <el-col :span="16">
      
      <div>
          <div id="showing-box1">
               
                <span v-html="message1"></span>
          </div>
          <div id="input-box1">

            <el-col :span="24"> 
                <el-input
                type="input"
                :rows="2"
                placeholder="Input Here..."
                resize = "none"
                v-model="user1textarea">
                <template slot="prepend">User1:</template>
                <template slot="append"><el-button type="success" @click="submitTextUser1">Go</el-button></template>
                </el-input>
            </el-col>


</div></div>

          
      
      </el-col>
  <el-col :span="8"><div class="grid-content bg-purple">
    <picker @select="addEmojiUser1" title="Group1-User1" />
<nimble-picker set="messenger" :data="data" @select="addEmojiUser1" />

<!-- <picker title="Pick your emoji…" emoji="point_up" /> -->
    
    </div></el-col>
</el-row>

<el-row :gutter="20">
  <el-col :span="16"><div class="grid-content bg-purple"></div></el-col>
  <el-col :span="8"><div class="grid-content bg-purple">
    <!-- <picker @select="addEmoji" title="Gropu1-User2" /> -->
    
    </div></el-col>
</el-row>





    </div>





</template>

<script>

import data from 'emoji-mart-vue/data/messenger.json'
import { NimblePicker } from 'emoji-mart-vue'



import { Picker } from 'emoji-mart-vue'
export default {
  name: 'HelloWorld',
  components:{
      Picker,
      NimblePicker,
      // data
  },
  props: {
    msg: String
  },
  data: function() {
        return {
            data,
            text1:'hello', 
            visible: false,
            user1_e_m: false,
            message1:'',
            user1textarea:'',
            // data:"{  id: 'santa',  name: 'Father Christmas',  colons: ':santa::skin-tone-3:',  text: '',  emoticons: [],  skin: 3,  native: '🎅🏼'}"
        }
  },
  methods: {
      addEmojiUser1(e){
          this.user1textarea = this.user1textarea + e.native;
      },
      submitTextUser1(){
          if(this.user1textarea == "" || this.user1textarea == null){
            return;
          }
          this.message1 = this.handelsentmessage("User1", this.message1, this.user1textarea);
          this.user1textarea = "";
      },
      handelsentmessage(username, preValue, addValue){
        var myDate = new Date();
        var time_date = myDate.toLocaleString( );        //获取日期与时间
        var rawHTML = "";
        rawHTML = preValue;
        rawHTML += "<div class=sender_><span class=username_time_date>"
        rawHTML += username + "    " + time_date + ":</span><br/>";
        // rawHTML += "<div class=\'sender_\'><span class=\'username_time_date\'>"
        // rawHTML += username + "    " + time_date + ":</span><br/>";
        rawHTML += addValue;
        rawHTML += "</div>";
        return rawHTML;

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
  .sender_ {
    text-align: right;
  }
  .reciver_ {
    text-align: left;
  }
  .username_time_date {
    color: #67C23A; 
  }
</style>