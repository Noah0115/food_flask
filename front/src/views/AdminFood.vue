<template>
  <div class="food">
    <div class="breadcrumb">
      <!-- 面包屑导航 -->
      <el-breadcrumb>
        <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>美食管理</el-breadcrumb-item>
        <el-breadcrumb-item>美食列表</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <el-card class="box-card">
      <div>
        <!-- 分栏间隔 -->
        <el-row :gutter="20">
          <el-col :span="6"
            ><div class="grid-content bg-purple">
              <!-- 搜索框 -->
              <el-input
                placeholder="请输入内容"
                v-model="queryInfo.query"
                clearable
                @clear="getFood"
              >
                <el-button
                  slot="append"
                  icon="el-icon-search"
                  @click="searchFoodList"
                ></el-button>
              </el-input></div
          ></el-col>
          <el-col :span="6"
            ><div class="grid-content bg-purple">
              <el-button type="primary" @click="showAddDialog"
                >添加美食</el-button
              >
            </div></el-col
          >
        </el-row>

        <el-table stripe border :data="foodlist" style="width: 100%">
          <el-table-column
            type="index"
            label="索引"
            width="90"
          ></el-table-column>
          <el-table-column prop="name" label="美食名称"> </el-table-column>
          <el-table-column prop="cost_time" label="烹饪时间"> </el-table-column>
          <!-- <el-table-column prop="cover" label="公告详情"> </el-table-column
          > -->
          <el-table-column prop="craft" label="工艺"> </el-table-column
          ><el-table-column prop="cover" label="图片">
            <template slot-scope="{ row }">
              <img
                :src="row.cover"
                alt="Food Cover"
                style="max-width: 100%; max-height: 100px"
              />
            </template>
          </el-table-column>
          <el-table-column prop="difficult" label="烹饪难度"> </el-table-column>
          <el-table-column prop="flavour" label="口味"> </el-table-column>
          <el-table-column prop="food_type" label="美食种类">
            <template slot-scope="{ row }">
              {{ mapFoodType(row.food_type) }}
            </template>
          </el-table-column>
          <el-table-column prop="ingredients" label="主料"> </el-table-column>
          <el-table-column prop="accessories" label="辅料" width="280px">
          </el-table-column>
          <el-table-column prop="step" label="做法步骤" width="280px">
            <template slot-scope="{ row }">
              {{ truncateText(row.step, 20) }}
            </template>
          </el-table-column>
          <el-table-column label="操作" width="80px">
            <template v-slot="scope">
              <!-- 查 -->
              <el-button
                type="primary"
                icon="el-icon-edit"
                size="small"
                @click="showEditDialog(scope.row.id)"
              ></el-button>
            </template>
          </el-table-column>
          <el-table-column label="状态" width="180px">
            <template v-slot="scope">
              <!-- 删除按钮 -->
              <el-switch
                v-model="scope.row.status"
                @change="StateChanged(scope.row.id)"
                active-text="激活"
                inactive-text="禁用"
              >
              </el-switch>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <!-- 查窗口 -->

      <!-- 改窗口 -->
      <el-dialog
        title="修改美食信息"
        :visible.sync="editDialogVisible"
        width="50%"
        @close="editDialogClosed"
      >
        <el-form
          :model="editForm"
          :rules="editFormRules"
          ref="editFormRef"
          label-width="120px"
        >
          <el-form-item label="美食名称" prop="name">
            <el-input v-model="editForm.name"></el-input>
          </el-form-item>
          <el-form-item label="烹饪时间" prop="cost_time">
            <el-input v-model="editForm.cost_time"></el-input>
          </el-form-item>

          <el-form-item label="工艺" prop="craft">
            <el-input v-model="editForm.craft"></el-input>
          </el-form-item>
          <el-form-item label="烹饪难度" prop="difficult">
            <el-input v-model="editForm.difficult"></el-input>
          </el-form-item>
          <el-form-item label="口味" prop="flavour">
            <el-input v-model="editForm.flavour"></el-input>
          </el-form-item>
          <el-form-item label="美食种类" prop="food_type">
            <el-select v-model="editForm.food_type" placeholder="请选择省">
              <el-option
                v-for="category in catelist"
                :key="category.id"
                :label="category.type_name"
                :value="category.id"
              ></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="主料" prop="ingredients">
            <el-input v-model="editForm.ingredients"></el-input>
          </el-form-item>
          <el-form-item label="辅料" prop="accessories">
            <el-input v-model="editForm.accessories"></el-input>
          </el-form-item>
          <el-form-item
            v-for="(step, index) in editForm.steps"
            :label="'步骤step' + (index + 1)"
            :key="step.key"
            :prop="'steps.' + index + '.value'"
            :rules="{
              required: true,
              message: '步骤不能为空',
              trigger: 'blur',
            }"
          >
            <div>
              <el-input
                v-model="step.value"
                class="step-input"
                style="width: 60%"
              ></el-input
              ><el-button
                v-if="editForm.steps.length > 1"
                @click.prevent="removeStepedit(step)"
                class="remove-button"
                type="danger"
                >删除</el-button
              >
            </div>
          </el-form-item>
          <el-form-item>
            <el-button @click="addStepedit">新增步骤</el-button>
          </el-form-item>
          <el-form-item label="上传商品图片" prop="cover">
            <el-upload
              :file-list="coverfilelist"
              action="uploadAction"
              list-type="picture-card"
              :on-preview="handlePictureCardPreview"
              :on-remove="handleRemove"
              :limit="1"
              :show-file-list="true"
              name="img"
              ref="upload"
              :data="editForm"
              accept="image/png,image/gif,image/jpg,image/jpeg"
              :on-exceed="handleExceed"
              :auto-upload="false"
              :on-error="uploadError"
              :before-upload="handleBeforeUpload"
              :on-change="changeFile"
            >
              <i class="el-icon-plus"></i>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="" />
            </el-dialog>
          </el-form-item>
          <el-form-item label="上传步骤图片" prop="pic_path">
            <el-upload
              :file-list="manyfilelist"
              action="uploadAction"
              list-type="picture-card"
              :on-preview="handlePictureCardPreview"
              :on-remove="editRemovemany"
              multiple
              :limit="20"
              :show-file-list="true"
              name="img"
              ref="uploadmany"
              :data="editForm"
              accept="image/png,image/gif,image/jpg,image/jpeg"
              :on-exceed="handleExceed"
              :auto-upload="false"
              :on-error="uploadError"
              :before-upload="handleBeforeUpload"
              :on-change="changeFileMany"
            >
              <i class="el-icon-plus"></i>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="" />
            </el-dialog>
          </el-form-item>
          <el-form-item class="btns">
            <el-button type="primary" @click="editInfo">保存</el-button>
          </el-form-item>
        </el-form>
      </el-dialog>
      <!-- 增窗口 -->
      <el-dialog
        title="增加美食信息"
        :visible.sync="showAddDialogVisible"
        width="50%"
        @close="showAddDialogClosed"
      >
        <el-form
          :model="addForm"
          :rules="addFormRules"
          ref="addFormRef"
          label-width="120px"
        >
          <el-form-item label="美食名称" prop="name">
            <el-input v-model="addForm.name"></el-input>
          </el-form-item>
          <el-form-item label="烹饪时间" prop="cost_time">
            <el-input v-model="addForm.cost_time"></el-input>
          </el-form-item>

          <el-form-item label="工艺" prop="craft">
            <el-input v-model="addForm.craft"></el-input>
          </el-form-item>
          <el-form-item label="烹饪难度" prop="difficult">
            <el-input v-model="addForm.difficult"></el-input>
          </el-form-item>
          <el-form-item label="口味" prop="flavour">
            <el-input v-model="addForm.flavour"></el-input>
          </el-form-item>
          <el-form-item label="美食种类" prop="food_type">
            <el-select v-model="addForm.food_type">
              <el-option
                v-for="category in catelist"
                :key="category.id"
                :label="category.type_name"
                :value="category.id"
              ></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="主料" prop="ingredients">
            <el-input v-model="addForm.ingredients"></el-input>
          </el-form-item>
          <el-form-item label="辅料" prop="accessories">
            <el-input v-model="addForm.accessories"></el-input>
          </el-form-item>
          <!-- <el-form-item label="做法步骤" prop="step">
            <el-input v-model="addForm.step"></el-input>
          </el-form-item> -->
          <el-form-item
            v-for="(step, index) in addForm.steps"
            :label="'步骤step' + (index + 1)"
            :key="step.key"
            :prop="'steps.' + index + '.value'"
            :rules="{
              required: true,
              message: '步骤不能为空',
              trigger: 'blur',
            }"
          >
            <div>
              <el-input
                v-model="step.value"
                class="step-input"
                style="width: 60%"
              ></el-input
              ><el-button
                v-if="addForm.steps.length > 1"
                @click.prevent="removeStep(step)"
                class="remove-button"
                type="danger"
                >删除</el-button
              >
            </div>
          </el-form-item>
          <el-form-item>
            <el-button @click="addStep">新增步骤</el-button>
          </el-form-item>
          <!-- 新增上传图片的部分 -->
          <el-form-item label="上传商品图片" prop="cover">
            <el-upload
              action="uploadAction"
              list-type="picture-card"
              :on-preview="handlePictureCardPreview"
              :on-remove="handleRemove"
              :limit="1"
              :show-file-list="true"
              name="img"
              ref="upload"
              :data="addForm"
              accept="image/png,image/gif,image/jpg,image/jpeg"
              :on-exceed="handleExceed"
              :auto-upload="false"
              :on-error="uploadError"
              :before-upload="handleBeforeUpload"
              :on-change="changeFile"
            >
              <i class="el-icon-plus"></i>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="" />
            </el-dialog>
          </el-form-item>
          <el-form-item label="上传步骤图片" prop="pic_path">
            <el-upload
              action="uploadAction"
              list-type="picture-card"
              :on-preview="handlePictureCardPreview"
              :on-remove="handleRemovemany"
              multiple
              :limit="20"
              :show-file-list="true"
              name="img"
              ref="uploadmany"
              :data="addForm"
              accept="image/png,image/gif,image/jpg,image/jpeg"
              :on-exceed="handleExceed"
              :auto-upload="false"
              :on-error="uploadError"
              :before-upload="handleBeforeUpload"
              :on-change="changeFileMany"
            >
              <i class="el-icon-plus"></i>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="" />
            </el-dialog>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="showAddDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="uploadFileFun()">确 定</el-button>
        </span>
      </el-dialog>
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="currentChange"
        :current-page="currentPage"
        :page-sizes="[1, 2, 5, 10]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination>
    </el-card>
  </div>
</template>

<script>

export default {
  data() {
    return {
      foodlist: [],
      catelist: [],
      showAddDialogVisible: false,
      addForm: {
        name: '',
        cost_time: '',
        craft: '',
        difficult: '',
        flavour: '',
        ingredients: '',
        accessories: '',
        steps: [{
          value: ''
        }],
      },
      addFormPic: {},
      addFormRules: {
        name: [
          { required: true, message: "请输入美食名称", trigger: "blur" },
        ],
        cost_time: [
          { required: true, message: "请输入烹饪时间", trigger: "blur" },
        ],
        craft: [
          { required: true, message: "请输入工艺", trigger: "blur" },

        ],
        difficult: [
          { required: true, message: "请输入烹饪难度", trigger: "blur" },
        ],
        flavour: [
          { required: true, message: "请输入口味", trigger: "blur" },
        ],
        food_type: [
          { required: true, message: "请输入美食种类", trigger: "blur" },
        ],
        ingredients: [
          { required: true, message: "请输入主料", trigger: "blur" },
        ],
        accessories: [
          { required: true, message: "请输入辅料", trigger: "blur" },
        ],
        step: [
          { required: true, message: "请输入做法步骤", trigger: "blur" },
        ],
      },
      editDialogVisible: false,
      editForm: {
        steps: [{
          value: ''
        }],
      },

      editFormRules: {
        name: [
          { required: true, message: "请输入美食名称", trigger: "blur" },
        ],
        cost_time: [
          { required: true, message: "请输入烹饪时间", trigger: "blur" },
        ],
        craft: [
          { required: true, message: "请输入工艺", trigger: "blur" },

        ],
        difficult: [
          { required: true, message: "请输入烹饪难度", trigger: "blur" },
        ],
        flavour: [
          { required: true, message: "请输入口味", trigger: "blur" },
        ],
        food_type: [
          { required: true, message: "请输入美食种类", trigger: "blur" },
        ],
        ingredients: [
          { required: true, message: "请输入主料", trigger: "blur" },
        ],
        accessories: [
          { required: true, message: "请输入辅料", trigger: "blur" },
        ],
        step: [
          { required: true, message: "请输入做法步骤", trigger: "blur" },
        ],
      },
      total: 0, // 商品总量
      pageSize: 10, // 每页显示的商品数量
      currentPage: 1, //当前页码
      foodlistall: [],
      type_name: '',
      dialogImageUrl: '',
      dialogVisible: false,
      uploadFiles: '', //formData img 文件
      uploadFilesMany: [],
      steps: "",
      //封面图预加载
      coverfilelist: [],
      //步骤图加载
      manyfilelist: [],
      queryInfo: {
        query: "",
      },

    };
  },

  created() {
    this.getCate();
    this.getFood();
  },

  methods: {
    async getCate() {
      //调用请求，第一个参数是请求地址
      const { data: res } = await this.$http.get("/goods/alltypes");
      if (res.code !== 200) {

        return this.$message.error(res.msg);
      }
      // this.$message.success(res.msg)
      this.catelist = res.data;
      // console.log(typeof this.catelist[0].id)

    },
    async getFood() {
      //调用请求，第一个参数是请求地址
      const { data: res } = await this.$http.get("/back/get_all_food");
      if (res.code !== 200) {

        return this.$message.error(res.msg);
      }
      this.$message.success(res.msg)
      console.log(res.data[0])
      this.total = res.data.length;
      this.foodlistall = res.data;
      this.foodlistall = this.foodlistall.map(item => ({
        ...item,
        status: item.status === 1
      }));

      /* console.log(typeof this.foodlistall[0].food_type) */
      /* this.foodlistall[0].food_type = parseInt(this.foodlistall[0].food_type);
      console.log(typeof this.foodlistall[0].food_type) */
      this.fenye();
    },
    fenye() {

      // 计算起始索引
      const startIndex = (this.currentPage - 1) * this.pageSize;
      // 计算结束索引
      const endIndex = startIndex + this.pageSize;
      this.foodlist = this.foodlistall.slice(startIndex, endIndex);;
    },
    //监听Pagesize改变的事件
    handleSizeChange(newSize) {

      this.pageSize = newSize;

      this.fenye();
    },
    //监听页码值改变的事件
    currentChange(newPage) {
      this.currentPage = newPage;
      this.fenye();

    },
    truncateText(text, maxLength) {
      if (text.length > maxLength) {
        return text.substring(0, maxLength) + '...';
      }
      return text;
    },
    mapFoodType(foodType) {
      const category = this.catelist.find(category => category.id === parseInt(foodType));
      return category ? category.type_name : '';
    },
    showAddDialog() {
      this.showAddDialogVisible = true

    },
    showAddDialogClosed() {
      this.$refs.addFormRef.resetFields();
      this.uploadFilesMany = []
    },
    //显示修改信息
    async showEditDialog(id) {
      this.uploadFiles = ''
      this.editDialogVisible = true;
      const { data: res } = await this.$http.post("/goods/goods_info", { id: id });
      this.editForm = {
        ...this.editForm,  // 保留原有属性
        ...res.data[0],     // 将 res.data[0] 的属性合并到 editForm 中
      };

      this.editForm.food_type = parseInt(this.editForm.food_type);

      // 假设 this.editForm.step 是一个包含字符串的数组
      this.editForm.steps = [];
      console.log('aaa', this.editForm)
      let now = Date.now();
      this.editForm.step.forEach((step, index) => {
        // 去掉 "Step+index"
        step = step.replace(new RegExp(`步骤Step${index + 1}`, 'gi'), '');
        if (step.trim() !== '') {
          this.editForm.steps.push({ value: step, key: now++ });
        }
      });
      this.coverfilelist.push({ name: 'image.jpg', url: this.editForm.cover });

      // console.log(this.editForm.steps)
      //图片相关操作
      fetch(this.editForm.cover)
        .then(response => response.blob())
        .then(blob => {
          // 创建 File 对象，第二个参数是文件名，可以根据实际情况修改
          const file = new File([blob], 'image.jpg', { type: 'image/jpeg', uid: 'id' },);
          file.uid = Date.now();
          // 现在你可以将这个 File 对象用于表单数据或其他需要文件的地方

          this.uploadFiles = file
          // console.log('file999', this.uploadFiles);
        })
        .catch(error => {
          console.error('Error fetching image:', error);
        });

      this.convertURLsToFiles()

    },
    //多图转化为文件
    async convertURLsToFiles() {
      const filePromises = this.editForm.pic_path.map(async (url) => {
        try {
          const response = await fetch(url);
          const blob = await response.blob();
          const timestamp = Date.now();
          const randomSuffix = Math.floor(Math.random() * 1000);
          // 创建 File 对象，uid 可以根据实际情况设置
          const file = new File([blob], `image_${timestamp}_${randomSuffix}.jpg`, { type: 'image/jpeg' });
          // console.log('file', file)
          // file.uid = timestamp + randomSuffix
          this.manyfilelist.push({ name: file.name, url: url });


          return file;
        } catch (error) {
          console.error('Error fetching image:', error);
          return null;
        }
      });


      // 等待所有文件转换完成
      const files = await Promise.all(filePromises);

      // 将文件列表存储在组件数据中
      this.uploadFilesMany = files.filter(file => file !== null);

      for (let i = 0; i < this.manyfilelist.length; i++) {
        // console.log('aaaaa',this.manyfilelist[i].uid)
        this.uploadFilesMany[i].uid = this.manyfilelist[i].uid;

      }
      console.log('文件列表', this.uploadFilesMany)
    },

    editDialogClosed() {
      this.$refs.editFormRef.resetFields();
      this.coverfilelist = []
      this.manyfilelist = []
      this.manyfilelist = []

    },
    //修改表单提交
    editInfo() {
      this.$refs.editFormRef.validate(async (valid) => {
        /* console.log(valid) */
        if (!valid) return;
        // console.log(this.editForm)
        let config
        let fd = new FormData();
        fd.append('id', this.editForm.id);
        fd.append('name', this.editForm.name);
        fd.append('cost_time', this.editForm.cost_time);
        fd.append('craft', this.editForm.craft);
        fd.append('difficult', this.editForm.difficult);
        fd.append('flavour', this.editForm.flavour);
        fd.append('food_type', this.editForm.food_type);
        fd.append('ingredients', this.editForm.ingredients);
        fd.append('accessories', this.editForm.accessories);
        console.log('editform', this.editForm.steps)
        this.editForm.steps.forEach((step, index) => {
          this.steps += `步骤step${index + 1}${step.value}\n`;
        });
        console.log(this.steps)
        fd.append('step', this.steps);
        this.steps = ''
        // fd.append('cover', undefined);
        // fd.append('pic_path', undefined);
        fd.append('status', 1);
        if (this.$refs.upload.uploadFiles.length === 0) {
          fd.append('cover', undefined);
        } else {
          console.log(this.uploadFiles)
          fd.append('cover', this.uploadFiles);

          config = {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
        }
        if (this.$refs.uploadmany.uploadFiles.length === 0) {
          fd.append('pic_path', undefined);

        } else {

          // fd.append('pic_path', this.uploadFilesMany);
          this.uploadFilesMany.forEach(file => {
            // 第一个参数可改，看后台接口接收什么就改成什么。
            // 第二个参数，是没一个文件的文件流，有时候是file，有时候是file.raw
            // 打印出来，根据时间情况来传入。我也不知道为什么，可能是elm版本封装的json格式不一样
            fd.append('pic_path', file)

          })
          config = {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
        }
        fd.forEach((value, key) => {
          console.log(key, value);
        })
        /* console.log(config) */
        //可以发起添加用户的网络请求
        const { data: res } = await this.$http.post(
          "/back/update_food", fd, config
        )


        if (res.code !== 200) {
          // console.log(res)
          return this.$message.error("更新美食信息失败");
        }
        this.$message.success("更新美食信息成功");
        window.location.reload();
        this.getFood();
        this.editDialogVisible = false;



      });
    },
    //滑块改变
    async StateChanged(id) {
      const selectedItem = this.foodlist.find(item => item.id === id);
      /* console.log(selectedItem.status) */
      if (selectedItem) {
        this.editForm = selectedItem;
        // 打开编辑对话框或执行其他操作
      } else {
        console.log("Item not found with id:", id);
      }
      /* this.editForm=message */
      /* console.log(message.status) */
      this.editForm.status = this.editForm.status ? 1 : 0;
      /* console.log(this.editForm) */
      const { data: res } = await this.$http.post("/back/update_food", this.editForm);

      if (res.code !== 200) {
        return this.$message.error("禁用失败");

      }

      this.$message.success("修改成功");
      /* console.log(this.editForm) */

      this.getFood();

    },

    // 上传文件之前的钩子
    handleBeforeUpload(file) {

      console.log('按钮', this.titleMap)
      if (!(file.type === 'image/png' || file.type === 'image/gif' || file.type === 'image/jpg' || file.type ===
        'image/jpeg')) {
        this.$notify.warning({
          title: '警告',
          message: '请上传格式为image/png, image/gif, image/jpg, image/jpeg的图片'
        })
      }
      let size = file.size / 1024 / 1024 / 2
      if (size > 2) {
        this.$notify.warning({
          title: '警告',
          message: '图片大小必须小于2M'
        })
      }

    },
    //图片上传超过数量限制
    handleExceed(files, fileList) {
      this.$message.error("上传图片不能超过1张!");
    },
    handleRemove(file, fileList) {
      this.$message.error("删除成功!");
    },
    handleRemovemany(file, fileList) {
      // console.log(file.raw.uid)
      // 假设你要删除数组中 uid 为某个值的元素
      console.log("文件666", file)
      const uidToRemove = file.raw.uid; // 你的 uid 值

      // 找到要删除的元素的索引
      const indexToRemove = this.uploadFilesMany.findIndex(file1 => file1.uid === uidToRemove);

      // 如果找到了对应的元素，就将其从数组中删除
      if (indexToRemove !== -1) {
        this.uploadFilesMany.splice(indexToRemove, 1);
      }
      this.$message.error("删除成功!");
    },
    editRemovemany(file, fileList) {
      // console.log(file.raw.uid)
      // 假设你要删除数组中 uid 为某个值的元素
      const uidToRemove = file.uid; // 你的 uid 值
      // 找到要删除的元素的索引file1.uid === uidToRemove
      const indexToRemove = this.uploadFilesMany.findIndex(file1 => file1.uid === uidToRemove);
      // 如果找到了对应的元素，就将其从数组中删除
      if (indexToRemove !== -1) {
        this.uploadFilesMany.splice(indexToRemove, 1);
      }
      this.$message.error("删除成功!");

    },
    // 图片上传失败时
    uploadError() {
      this.$message.error("图片上传失败!");
    },
    //预览图片
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    //文件改变时 on-change方法 ，fileList[0].raw 就是传给后端的值
    //filelist这个对象里面有很多属性，我们上传文件时，实际上传的是filelist列表中每一项的raw,只有raw可以正常上传， 获取到文件后，需要定义变量保存文件。所以需要获取filelist中的raw进行保存。
    //这里我用的formdata上传多文件，console打印formdata，文件在控制台中显示的格式为binary。

    changeFile(file, fileList) {
      this.uploadFiles = fileList[0].raw
    },
    changeFileMany(file, fileList) {
      this.uploadFilesMany.push(file.raw)
    },
    //新增美食
    uploadFileFun() {
      this.$refs.addFormRef.validate((valid) => {
        if (!valid) return;
        let config
        let fd = new FormData();
        fd.append('name', this.addForm.name);
        fd.append('cost_time', this.addForm.cost_time);
        fd.append('craft', this.addForm.craft);
        fd.append('difficult', this.addForm.difficult);
        fd.append('flavour', this.addForm.flavour);
        fd.append('food_type', this.addForm.food_type);
        fd.append('ingredients', this.addForm.ingredients);
        fd.append('accessories', this.addForm.accessories);
        // console.log('addform', this.addForm)
        this.addForm.steps.forEach((step, index) => {
          this.steps += `步骤step${index + 1}${step.value}\n`;
        });
        fd.append('step', this.steps);
        fd.append('status', 1);
        // console.log('fd',fd)
        // console.log(this.$refs.upload)
        // console.log('aaa', this.$refs.upload)
        // console.log('bbb', this.$refs.uploadmany)
        if (this.$refs.upload.uploadFiles.length === 0) {
          fd.append('cover', undefined);

        } else {
          fd.append('cover', this.uploadFiles);

          config = {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
        }

        if (this.$refs.uploadmany.uploadFiles.length === 0) {
          fd.append('pic_path', undefined);

        } else {
          // fd.append('pic_path', this.uploadFilesMany);
          this.uploadFilesMany.forEach(file => {
            // 第一个参数可改，看后台接口接收什么就改成什么。
            // 第二个参数，是没一个文件的文件流，有时候是file，有时候是file.raw
            // 打印出来，根据时间情况来传入。我也不知道为什么，可能是elm版本封装的json格式不一样
            fd.append('pic_path', file)
          })
          config = {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
        }
        fd.forEach((value, key) => {
          console.log(key, value);
        })
        this.$http.post("/back/add_food", fd, config).then(res => {
          fd.forEach((value, key) => {
            console.log(key, value);
          });

          if (res.data.code == 200) {
            this.showAddDialogVisible = false;
            this.getFood();
            this.$message.success("添加美食成功");
            //新增完清空表单内容
            setTimeout(() => {
              this.$refs.addFormRef.resetFields();
            }, 200)

            // this.reload()
          } else {
            this.$message.error(res.data.msg);
          }
        }).catch(res => {
          console.log(res)
        })


      })
    },

    add() {
      this.dialogStatus = "addStore"
      this.dialogFormVisible = true
      this.goodsId = "" //新增商品是商品ID为空
    },
    // 取消
    cancel() {
      this.dialogFormVisible = false
      this.$refs[formName].resetFields()
    },
    //编辑
    handleEdit(index, row) {
      this.form = this.tableData[index]
      this.dialogStatus = "editStore"
      this.goodsId = row.id
      this.currentIndex = index
      this.dialogFormVisible = true
    },
    removeStep(item) {
      var index = this.addForm.steps.indexOf(item)
      if (index !== -1) {
        this.addForm.steps.splice(index, 1)
      }
    },
    removeStepedit(item) {
      var index = this.editForm.steps.indexOf(item)
      if (index !== -1) {
        this.editForm.steps.splice(index, 1)
      }
      console.log(this.editForm.steps)

    },
    addStep() {
      this.addForm.steps.push({
        value: '',
        key: Date.now()
      });
      console.log(this.addForm.steps)
    },
    addStepedit() {

      this.editForm.steps.push({
        value: '',
        key: Date.now()
      });
      console.log(this.editForm.steps)

    },
    async searchFoodList(){
      console.log(this.queryInfo.query)
      const { data: res } = await this.$http.post("/goods/search_goods", {
        "name": this.queryInfo.query
      });
      if (res.code !== 200) {
        /* console.log(res); */
        this.$message.error(res.msg);
      }
      this.$message.success(res.msg);
      this.total = res.data.length;
      this.foodlistall = res.data;
      this.foodlistall = this.foodlistall.map(item => ({
        ...item,
        status: item.status === 1
      }));
      this.fenye();
    }




  }
}
</script>
<style scoped>
.food .breadcrumb .el-breadcrumb {
  font-size: 16px !important;
}
.el-table {
  margin-top: 20px;
}
.btns {
  display: flex;
  justify-content: flex-end;
}
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
.step-container {
  display: flex;
  align-items: center;
}

.step-input {
  flex: 1; /* 占据剩余宽度 */
  /* margin-bottom: 10px; */
}

.remove-button {
  margin-left: 10px; /* 调整删除按钮与输入框之间的间距 */
}
</style>