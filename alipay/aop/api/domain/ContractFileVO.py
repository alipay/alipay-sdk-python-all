#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractFileVO(object):

    def __init__(self):
        self._file_addr = None
        self._file_name = None

    @property
    def file_addr(self):
        return self._file_addr

    @file_addr.setter
    def file_addr(self, value):
        self._file_addr = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_addr:
            if hasattr(self.file_addr, 'to_alipay_dict'):
                params['file_addr'] = self.file_addr.to_alipay_dict()
            else:
                params['file_addr'] = self.file_addr
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
        o = ContractFileVO()
        if 'file_addr' in d:
            o.file_addr = d['file_addr']
        if 'file_name' in d:
            o.file_name = d['file_name']
        return o


