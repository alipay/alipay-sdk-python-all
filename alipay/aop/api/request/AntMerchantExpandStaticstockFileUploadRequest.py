#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AntMerchantExpandStaticstockFileUploadRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._file_format = None
        self._file_name = None
        self._file_url = None
        self._time_period_end = None
        self._time_period_start = None
        self._total_count = None
        self._upload_batch_no = None
        self._upload_format = None
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
    def file_format(self):
        return self._file_format

    @file_format.setter
    def file_format(self, value):
        self._file_format = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def time_period_end(self):
        return self._time_period_end

    @time_period_end.setter
    def time_period_end(self, value):
        self._time_period_end = value
    @property
    def time_period_start(self):
        return self._time_period_start

    @time_period_start.setter
    def time_period_start(self, value):
        self._time_period_start = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def upload_batch_no(self):
        return self._upload_batch_no

    @upload_batch_no.setter
    def upload_batch_no(self, value):
        self._upload_batch_no = value
    @property
    def upload_format(self):
        return self._upload_format

    @upload_format.setter
    def upload_format(self, value):
        self._upload_format = value

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
        params[P_METHOD] = 'ant.merchant.expand.staticstock.file.upload'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.file_format:
            if hasattr(self.file_format, 'to_alipay_dict'):
                params['file_format'] = json.dumps(obj=self.file_format.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_format'] = self.file_format
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = json.dumps(obj=self.file_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_name'] = self.file_name
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = json.dumps(obj=self.file_url.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_url'] = self.file_url
        if self.time_period_end:
            if hasattr(self.time_period_end, 'to_alipay_dict'):
                params['time_period_end'] = json.dumps(obj=self.time_period_end.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['time_period_end'] = self.time_period_end
        if self.time_period_start:
            if hasattr(self.time_period_start, 'to_alipay_dict'):
                params['time_period_start'] = json.dumps(obj=self.time_period_start.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['time_period_start'] = self.time_period_start
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = json.dumps(obj=self.total_count.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['total_count'] = self.total_count
        if self.upload_batch_no:
            if hasattr(self.upload_batch_no, 'to_alipay_dict'):
                params['upload_batch_no'] = json.dumps(obj=self.upload_batch_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['upload_batch_no'] = self.upload_batch_no
        if self.upload_format:
            if hasattr(self.upload_format, 'to_alipay_dict'):
                params['upload_format'] = json.dumps(obj=self.upload_format.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['upload_format'] = self.upload_format
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
