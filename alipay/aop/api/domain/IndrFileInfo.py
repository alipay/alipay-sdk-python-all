#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndrFileInfo(object):

    def __init__(self):
        self._file_format = None
        self._file_id = None

    @property
    def file_format(self):
        return self._file_format

    @file_format.setter
    def file_format(self, value):
        self._file_format = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_format:
            if hasattr(self.file_format, 'to_alipay_dict'):
                params['file_format'] = self.file_format.to_alipay_dict()
            else:
                params['file_format'] = self.file_format
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndrFileInfo()
        if 'file_format' in d:
            o.file_format = d['file_format']
        if 'file_id' in d:
            o.file_id = d['file_id']
        return o


