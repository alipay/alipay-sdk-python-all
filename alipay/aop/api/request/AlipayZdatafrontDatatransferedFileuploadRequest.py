#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayZdatafrontDatatransferedFileuploadRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._columns = None
        self._file_description = None
        self._file_digest = None
        self._file_type = None
        self._primary_key = None
        self._records = None
        self._type_id = None
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
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, value):
        self._columns = value
    @property
    def file_description(self):
        return self._file_description

    @file_description.setter
    def file_description(self, value):
        self._file_description = value
    @property
    def file_digest(self):
        return self._file_digest

    @file_digest.setter
    def file_digest(self, value):
        self._file_digest = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def primary_key(self):
        return self._primary_key

    @primary_key.setter
    def primary_key(self, value):
        self._primary_key = value
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        self._records = value
    @property
    def type_id(self):
        return self._type_id

    @type_id.setter
    def type_id(self, value):
        self._type_id = value

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
        params[P_METHOD] = 'alipay.zdatafront.datatransfered.fileupload'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.columns:
            if hasattr(self.columns, 'to_alipay_dict'):
                params['columns'] = json.dumps(obj=self.columns.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['columns'] = self.columns
        if self.file_description:
            if hasattr(self.file_description, 'to_alipay_dict'):
                params['file_description'] = json.dumps(obj=self.file_description.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_description'] = self.file_description
        if self.file_digest:
            if hasattr(self.file_digest, 'to_alipay_dict'):
                params['file_digest'] = json.dumps(obj=self.file_digest.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_digest'] = self.file_digest
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = json.dumps(obj=self.file_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_type'] = self.file_type
        if self.primary_key:
            if hasattr(self.primary_key, 'to_alipay_dict'):
                params['primary_key'] = json.dumps(obj=self.primary_key.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['primary_key'] = self.primary_key
        if self.records:
            if hasattr(self.records, 'to_alipay_dict'):
                params['records'] = json.dumps(obj=self.records.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['records'] = self.records
        if self.type_id:
            if hasattr(self.type_id, 'to_alipay_dict'):
                params['type_id'] = json.dumps(obj=self.type_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['type_id'] = self.type_id
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
