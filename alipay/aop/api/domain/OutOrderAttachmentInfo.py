#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OutOrderAttachmentInfo(object):

    def __init__(self):
        self._file_name = None
        self._file_path = None

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


    def to_alipay_dict(self):
        params = dict()
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_path:
            if hasattr(self.file_path, 'to_alipay_dict'):
                params['file_path'] = self.file_path.to_alipay_dict()
            else:
                params['file_path'] = self.file_path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OutOrderAttachmentInfo()
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_path' in d:
            o.file_path = d['file_path']
        return o


