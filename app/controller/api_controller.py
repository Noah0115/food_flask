from flask import request
from flask_restful import Resource
from flask_uploads import UploadSet, IMAGES
from app.model import Data

# 上传文件
photos = UploadSet("photos", IMAGES)
class FileUploadResource(Resource):
    def post(self):
        """处理POST请求，上传文件。

       Returns:
           dict: 包含文件上传状态和文件URL的字典。
       """
        try:
            # 检查请求中是否包含“照片”文件
            if "photo" not in request.files:
                return {"error": "No file part"}, 400

            photo = request.files["photo"]

            # 检查是否提供了文件名
            if photo.filename == "":
                return {"error": "No selected file"}, 400

            # 保存上传的文件
            filename = photos.save(photo)

            # 获取上传文件的URL
            file_url = photos.url(filename)

            return {"status": "success", "file_url": file_url}, 201

        except Exception as e:
            return {"error": str(e)}, 500
