#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RcsmartAuditContent(object):

    def __init__(self):
        self._content_biz_type = None
        self._content_data = None
        self._content_type = None
        self._ext_param = None
        self._file_id = None
        self._out_content_id = None

    @property
    def content_biz_type(self):
        return self._content_biz_type

    @content_biz_type.setter
    def content_biz_type(self, value):
        self._content_biz_type = value
    @property
    def content_data(self):
        return self._content_data

    @content_data.setter
    def content_data(self, value):
        self._content_data = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def out_content_id(self):
        return self._out_content_id

    @out_content_id.setter
    def out_content_id(self, value):
        self._out_content_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_biz_type:
            if hasattr(self.content_biz_type, 'to_alipay_dict'):
                params['content_biz_type'] = self.content_biz_type.to_alipay_dict()
            else:
                params['content_biz_type'] = self.content_biz_type
        if self.content_data:
            if hasattr(self.content_data, 'to_alipay_dict'):
                params['content_data'] = self.content_data.to_alipay_dict()
            else:
                params['content_data'] = self.content_data
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.out_content_id:
            if hasattr(self.out_content_id, 'to_alipay_dict'):
                params['out_content_id'] = self.out_content_id.to_alipay_dict()
            else:
                params['out_content_id'] = self.out_content_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RcsmartAuditContent()
        if 'content_biz_type' in d:
            o.content_biz_type = d['content_biz_type']
        if 'content_data' in d:
            o.content_data = d['content_data']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'out_content_id' in d:
            o.out_content_id = d['out_content_id']
        return o


