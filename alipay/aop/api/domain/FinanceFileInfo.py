#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FinanceFileInfo(object):

    def __init__(self):
        self._file_hash = None
        self._file_id = None
        self._file_key = None

    @property
    def file_hash(self):
        return self._file_hash

    @file_hash.setter
    def file_hash(self, value):
        self._file_hash = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_key(self):
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_hash:
            if hasattr(self.file_hash, 'to_alipay_dict'):
                params['file_hash'] = self.file_hash.to_alipay_dict()
            else:
                params['file_hash'] = self.file_hash
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.file_key:
            if hasattr(self.file_key, 'to_alipay_dict'):
                params['file_key'] = self.file_key.to_alipay_dict()
            else:
                params['file_key'] = self.file_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinanceFileInfo()
        if 'file_hash' in d:
            o.file_hash = d['file_hash']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_key' in d:
            o.file_key = d['file_key']
        return o


