#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoAutoaftermarketAttachmentUploadModel(object):

    def __init__(self):
        self._ant_biz_id = None
        self._biz_type = None
        self._extra = None
        self._file_biz_code = None
        self._file_content = None
        self._file_name = None
        self._file_store_type = None
        self._file_type = None
        self._out_biz_id = None
        self._path = None
        self._upload_time = None

    @property
    def ant_biz_id(self):
        return self._ant_biz_id

    @ant_biz_id.setter
    def ant_biz_id(self, value):
        self._ant_biz_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def extra(self):
        return self._extra

    @extra.setter
    def extra(self, value):
        self._extra = value
    @property
    def file_biz_code(self):
        return self._file_biz_code

    @file_biz_code.setter
    def file_biz_code(self, value):
        self._file_biz_code = value
    @property
    def file_content(self):
        return self._file_content

    @file_content.setter
    def file_content(self, value):
        self._file_content = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_store_type(self):
        return self._file_store_type

    @file_store_type.setter
    def file_store_type(self, value):
        self._file_store_type = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def upload_time(self):
        return self._upload_time

    @upload_time.setter
    def upload_time(self, value):
        self._upload_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_biz_id:
            if hasattr(self.ant_biz_id, 'to_alipay_dict'):
                params['ant_biz_id'] = self.ant_biz_id.to_alipay_dict()
            else:
                params['ant_biz_id'] = self.ant_biz_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.extra:
            if hasattr(self.extra, 'to_alipay_dict'):
                params['extra'] = self.extra.to_alipay_dict()
            else:
                params['extra'] = self.extra
        if self.file_biz_code:
            if hasattr(self.file_biz_code, 'to_alipay_dict'):
                params['file_biz_code'] = self.file_biz_code.to_alipay_dict()
            else:
                params['file_biz_code'] = self.file_biz_code
        if self.file_content:
            if hasattr(self.file_content, 'to_alipay_dict'):
                params['file_content'] = self.file_content.to_alipay_dict()
            else:
                params['file_content'] = self.file_content
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_store_type:
            if hasattr(self.file_store_type, 'to_alipay_dict'):
                params['file_store_type'] = self.file_store_type.to_alipay_dict()
            else:
                params['file_store_type'] = self.file_store_type
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.upload_time:
            if hasattr(self.upload_time, 'to_alipay_dict'):
                params['upload_time'] = self.upload_time.to_alipay_dict()
            else:
                params['upload_time'] = self.upload_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsAutoAutoaftermarketAttachmentUploadModel()
        if 'ant_biz_id' in d:
            o.ant_biz_id = d['ant_biz_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'extra' in d:
            o.extra = d['extra']
        if 'file_biz_code' in d:
            o.file_biz_code = d['file_biz_code']
        if 'file_content' in d:
            o.file_content = d['file_content']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_store_type' in d:
            o.file_store_type = d['file_store_type']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'path' in d:
            o.path = d['path']
        if 'upload_time' in d:
            o.upload_time = d['upload_time']
        return o


