#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class ZhimaMerchantCloseloopDataUploadRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._biz_ext_params = None
        self._columns = None
        self._file_charset = None
        self._linked_merchant_id = None
        self._primary_key_columns = None
        self._records = None
        self._scene_code = None
        self._file = None
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
    def biz_ext_params(self):
        return self._biz_ext_params

    @biz_ext_params.setter
    def biz_ext_params(self, value):
        self._biz_ext_params = value
    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, value):
        self._columns = value
    @property
    def file_charset(self):
        return self._file_charset

    @file_charset.setter
    def file_charset(self, value):
        self._file_charset = value
    @property
    def linked_merchant_id(self):
        return self._linked_merchant_id

    @linked_merchant_id.setter
    def linked_merchant_id(self, value):
        self._linked_merchant_id = value
    @property
    def primary_key_columns(self):
        return self._primary_key_columns

    @primary_key_columns.setter
    def primary_key_columns(self, value):
        self._primary_key_columns = value
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        self._records = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        if not isinstance(value, FileItem):
            return
        self._file = value

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
        params[P_METHOD] = 'zhima.merchant.closeloop.data.upload'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.biz_ext_params:
            if hasattr(self.biz_ext_params, 'to_alipay_dict'):
                params['biz_ext_params'] = json.dumps(obj=self.biz_ext_params.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['biz_ext_params'] = self.biz_ext_params
        if self.columns:
            if hasattr(self.columns, 'to_alipay_dict'):
                params['columns'] = json.dumps(obj=self.columns.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['columns'] = self.columns
        if self.file_charset:
            if hasattr(self.file_charset, 'to_alipay_dict'):
                params['file_charset'] = json.dumps(obj=self.file_charset.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_charset'] = self.file_charset
        if self.linked_merchant_id:
            if hasattr(self.linked_merchant_id, 'to_alipay_dict'):
                params['linked_merchant_id'] = json.dumps(obj=self.linked_merchant_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['linked_merchant_id'] = self.linked_merchant_id
        if self.primary_key_columns:
            if hasattr(self.primary_key_columns, 'to_alipay_dict'):
                params['primary_key_columns'] = json.dumps(obj=self.primary_key_columns.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['primary_key_columns'] = self.primary_key_columns
        if self.records:
            if hasattr(self.records, 'to_alipay_dict'):
                params['records'] = json.dumps(obj=self.records.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['records'] = self.records
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = json.dumps(obj=self.scene_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['scene_code'] = self.scene_code
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
        if self.file:
            multipart_params['file'] = self.file
        return multipart_params
