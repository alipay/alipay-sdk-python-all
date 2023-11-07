#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AntfortuneStockStockinstopsBackflowUploadRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._compress_type = None
        self._forward_host = None
        self._forward_room = None
        self._forward_time = None
        self._forward_trace = None
        self._forward_zone = None
        self._inst_id = None
        self._msg_type = None
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
    def compress_type(self):
        return self._compress_type

    @compress_type.setter
    def compress_type(self, value):
        self._compress_type = value
    @property
    def forward_host(self):
        return self._forward_host

    @forward_host.setter
    def forward_host(self, value):
        self._forward_host = value
    @property
    def forward_room(self):
        return self._forward_room

    @forward_room.setter
    def forward_room(self, value):
        self._forward_room = value
    @property
    def forward_time(self):
        return self._forward_time

    @forward_time.setter
    def forward_time(self, value):
        self._forward_time = value
    @property
    def forward_trace(self):
        return self._forward_trace

    @forward_trace.setter
    def forward_trace(self, value):
        self._forward_trace = value
    @property
    def forward_zone(self):
        return self._forward_zone

    @forward_zone.setter
    def forward_zone(self, value):
        self._forward_zone = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value

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
        params[P_METHOD] = 'antfortune.stock.stockinstops.backflow.upload'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.compress_type:
            if hasattr(self.compress_type, 'to_alipay_dict'):
                params['compress_type'] = json.dumps(obj=self.compress_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['compress_type'] = self.compress_type
        if self.forward_host:
            if hasattr(self.forward_host, 'to_alipay_dict'):
                params['forward_host'] = json.dumps(obj=self.forward_host.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['forward_host'] = self.forward_host
        if self.forward_room:
            if hasattr(self.forward_room, 'to_alipay_dict'):
                params['forward_room'] = json.dumps(obj=self.forward_room.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['forward_room'] = self.forward_room
        if self.forward_time:
            if hasattr(self.forward_time, 'to_alipay_dict'):
                params['forward_time'] = json.dumps(obj=self.forward_time.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['forward_time'] = self.forward_time
        if self.forward_trace:
            if hasattr(self.forward_trace, 'to_alipay_dict'):
                params['forward_trace'] = json.dumps(obj=self.forward_trace.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['forward_trace'] = self.forward_trace
        if self.forward_zone:
            if hasattr(self.forward_zone, 'to_alipay_dict'):
                params['forward_zone'] = json.dumps(obj=self.forward_zone.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['forward_zone'] = self.forward_zone
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = json.dumps(obj=self.inst_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['inst_id'] = self.inst_id
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = json.dumps(obj=self.msg_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['msg_type'] = self.msg_type
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
