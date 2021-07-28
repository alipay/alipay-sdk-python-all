#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoFilePathQueryModel(object):

    def __init__(self):
        self._content_md_5 = None
        self._content_type = None
        self._file_name = None
        self._file_size = None

    @property
    def content_md_5(self):
        return self._content_md_5

    @content_md_5.setter
    def content_md_5(self, value):
        self._content_md_5 = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_md_5:
            if hasattr(self.content_md_5, 'to_alipay_dict'):
                params['content_md_5'] = self.content_md_5.to_alipay_dict()
            else:
                params['content_md_5'] = self.content_md_5
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_size:
            if hasattr(self.file_size, 'to_alipay_dict'):
                params['file_size'] = self.file_size.to_alipay_dict()
            else:
                params['file_size'] = self.file_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoFilePathQueryModel()
        if 'content_md_5' in d:
            o.content_md_5 = d['content_md_5']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_size' in d:
            o.file_size = d['file_size']
        return o


