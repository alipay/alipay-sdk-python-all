#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayMarketingImageEnhanceUploadRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._image_directory_id = None
        self._material_field = None
        self._material_spec_id = None
        self._need_enhance = None
        self._upload_scene = None
        self._image_content = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def image_directory_id(self):
        return self._image_directory_id

    @image_directory_id.setter
    def image_directory_id(self, value):
        self._image_directory_id = value
    @property
    def material_field(self):
        return self._material_field

    @material_field.setter
    def material_field(self, value):
        self._material_field = value
    @property
    def material_spec_id(self):
        return self._material_spec_id

    @material_spec_id.setter
    def material_spec_id(self, value):
        self._material_spec_id = value
    @property
    def need_enhance(self):
        return self._need_enhance

    @need_enhance.setter
    def need_enhance(self, value):
        self._need_enhance = value
    @property
    def upload_scene(self):
        return self._upload_scene

    @upload_scene.setter
    def upload_scene(self, value):
        self._upload_scene = value

    @property
    def image_content(self):
        return self._image_content

    @image_content.setter
    def image_content(self, value):
        if not isinstance(value, FileItem):
            return
        self._image_content = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.marketing.image.enhance.upload'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.image_directory_id:
            if hasattr(self.image_directory_id, 'to_alipay_dict'):
                params['image_directory_id'] = json.dumps(obj=self.image_directory_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['image_directory_id'] = self.image_directory_id
        if self.material_field:
            if hasattr(self.material_field, 'to_alipay_dict'):
                params['material_field'] = json.dumps(obj=self.material_field.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['material_field'] = self.material_field
        if self.material_spec_id:
            if hasattr(self.material_spec_id, 'to_alipay_dict'):
                params['material_spec_id'] = json.dumps(obj=self.material_spec_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['material_spec_id'] = self.material_spec_id
        if self.need_enhance:
            if hasattr(self.need_enhance, 'to_alipay_dict'):
                params['need_enhance'] = json.dumps(obj=self.need_enhance.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['need_enhance'] = self.need_enhance
        if self.upload_scene:
            if hasattr(self.upload_scene, 'to_alipay_dict'):
                params['upload_scene'] = json.dumps(obj=self.upload_scene.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['upload_scene'] = self.upload_scene
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        if self.image_content:
            multipart_params['image_content'] = self.image_content
        return multipart_params
