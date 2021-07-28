#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayInsSceneInsserviceprodSerattachmentUploadRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._biz_data = None
        self._file_biz_code = None
        self._file_desc = None
        self._file_name = None
        self._file_path = None
        self._file_size = None
        self._file_type = None
        self._out_biz_no = None
        self._ser_biz_no = None
        self._ser_biz_type = None
        self._upload_time = None
        self._file_content = None
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
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def file_biz_code(self):
        return self._file_biz_code

    @file_biz_code.setter
    def file_biz_code(self, value):
        self._file_biz_code = value
    @property
    def file_desc(self):
        return self._file_desc

    @file_desc.setter
    def file_desc(self, value):
        self._file_desc = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def ser_biz_no(self):
        return self._ser_biz_no

    @ser_biz_no.setter
    def ser_biz_no(self, value):
        self._ser_biz_no = value
    @property
    def ser_biz_type(self):
        return self._ser_biz_type

    @ser_biz_type.setter
    def ser_biz_type(self, value):
        self._ser_biz_type = value
    @property
    def upload_time(self):
        return self._upload_time

    @upload_time.setter
    def upload_time(self, value):
        self._upload_time = value

    @property
    def file_content(self):
        return self._file_content

    @file_content.setter
    def file_content(self, value):
        if not isinstance(value, FileItem):
            return
        self._file_content = value

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
        params[P_METHOD] = 'alipay.ins.scene.insserviceprod.serattachment.upload'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = json.dumps(obj=self.biz_data.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['biz_data'] = self.biz_data
        if self.file_biz_code:
            if hasattr(self.file_biz_code, 'to_alipay_dict'):
                params['file_biz_code'] = json.dumps(obj=self.file_biz_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_biz_code'] = self.file_biz_code
        if self.file_desc:
            if hasattr(self.file_desc, 'to_alipay_dict'):
                params['file_desc'] = json.dumps(obj=self.file_desc.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_desc'] = self.file_desc
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = json.dumps(obj=self.file_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_name'] = self.file_name
        if self.file_path:
            if hasattr(self.file_path, 'to_alipay_dict'):
                params['file_path'] = json.dumps(obj=self.file_path.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_path'] = self.file_path
        if self.file_size:
            if hasattr(self.file_size, 'to_alipay_dict'):
                params['file_size'] = json.dumps(obj=self.file_size.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_size'] = self.file_size
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = json.dumps(obj=self.file_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_type'] = self.file_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = json.dumps(obj=self.out_biz_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.ser_biz_no:
            if hasattr(self.ser_biz_no, 'to_alipay_dict'):
                params['ser_biz_no'] = json.dumps(obj=self.ser_biz_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['ser_biz_no'] = self.ser_biz_no
        if self.ser_biz_type:
            if hasattr(self.ser_biz_type, 'to_alipay_dict'):
                params['ser_biz_type'] = json.dumps(obj=self.ser_biz_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['ser_biz_type'] = self.ser_biz_type
        if self.upload_time:
            if hasattr(self.upload_time, 'to_alipay_dict'):
                params['upload_time'] = json.dumps(obj=self.upload_time.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['upload_time'] = self.upload_time
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
        if self.file_content:
            multipart_params['file_content'] = self.file_content
        return multipart_params
