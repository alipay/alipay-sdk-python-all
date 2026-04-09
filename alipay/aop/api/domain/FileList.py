#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FileList(object):

    def __init__(self):
        self._file_hash = None
        self._file_md_5 = None
        self._file_name = None
        self._file_size = None
        self._file_type = None

    @property
    def file_hash(self):
        return self._file_hash

    @file_hash.setter
    def file_hash(self, value):
        self._file_hash = value
    @property
    def file_md_5(self):
        return self._file_md_5

    @file_md_5.setter
    def file_md_5(self, value):
        self._file_md_5 = value
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
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_hash:
            if hasattr(self.file_hash, 'to_alipay_dict'):
                params['file_hash'] = self.file_hash.to_alipay_dict()
            else:
                params['file_hash'] = self.file_hash
        if self.file_md_5:
            if hasattr(self.file_md_5, 'to_alipay_dict'):
                params['file_md_5'] = self.file_md_5.to_alipay_dict()
            else:
                params['file_md_5'] = self.file_md_5
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
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FileList()
        if 'file_hash' in d:
            o.file_hash = d['file_hash']
        if 'file_md_5' in d:
            o.file_md_5 = d['file_md_5']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_size' in d:
            o.file_size = d['file_size']
        if 'file_type' in d:
            o.file_type = d['file_type']
        return o


