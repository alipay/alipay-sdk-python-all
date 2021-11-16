#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractAttachDTO(object):

    def __init__(self):
        self._file_key = None
        self._file_name = None

    @property
    def file_key(self):
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_key:
            if hasattr(self.file_key, 'to_alipay_dict'):
                params['file_key'] = self.file_key.to_alipay_dict()
            else:
                params['file_key'] = self.file_key
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractAttachDTO()
        if 'file_key' in d:
            o.file_key = d['file_key']
        if 'file_name' in d:
            o.file_name = d['file_name']
        return o


