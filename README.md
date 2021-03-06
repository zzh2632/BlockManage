# 工具目的
对文档/知识 按分块进行管理，组织为知识树，便于进行文档的编写和重构

# 功能
- 树状结构，支持基本的结构操作：
    - 创建子节点：ctrl+n
    - 创建兄弟节点：enter
    - 删除节点：delete
    - 将节点及子节点移动到上一层级: ctrl + ←
    - 将节点及子节点移动到下一层级：ctrl + →
    - 将节点及子节点移动到当前层级前一位置：ctrl+↑
    - 将节点及子节点移动到当前层级后一位置：ctrl+↓
    - 全部展开
    - 全部折叠
    - 节点重命名：F2
- 树状结构中的每个节点可指定其属性：描述、备注、链接
- 窗口隐藏/显示：alt + `
- 文件管理
    - 导入 xml 存档文件
    - 保存：ctrl+s
    - 保存为 xml 存档文件
- 样式
    - 仿 markdown 标题层级样式

# 获取
<https://github.com/zzh2632/BlockManage/tree/main/dist>

# 开发计划

## 操作
- 切换到节点属性：Tab
- 树形结构按层级展开/折叠
- 支持拖拽节点
- 撤销/恢复
- 节点链接属性支持点击

## 表格数据
- 增加写作目的列

## 样式
- 黑色风格
- 分块待处理标签
- 自定义字体样式
- 存档保留列宽
- 界面网格
- 节点链接属性支持多行

## 拓展
- 读取markdown列表纯文本导入为树形结构
- 本体-实体记录
- 知识图谱构建

# 待修复问题
- 向下移动超出末尾造成crash
- 对根节点操作 crash
- 树操作同步选中状态
- 取消保存 crash
