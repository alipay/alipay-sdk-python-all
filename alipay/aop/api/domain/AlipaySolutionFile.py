#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySolutionFile(object):

    def __init__(self):
        self._file_code = None
        self._file_id = None

    @property
    def file_code(self):
        return self._file_code

    @file_code.setter
    def file_code(self, value):
        self._file_code = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_code:
            if hasattr(self.file_code, 'to_alipay_dict'):
                params['file_code'] = self.file_code.to_alipay_dict()
            else:
                params['file_code'] = self.file_code
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
        o = AlipaySolutionFile()
        if 'file_code' in d:
            o.file_code = d['file_code']
        if 'file_id' in d:
            o.file_id = d['file_id']
        return o


