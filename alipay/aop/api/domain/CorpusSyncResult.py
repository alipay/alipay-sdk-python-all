#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CorpusSyncResult(object):

    def __init__(self):
        self._exception_count = None
        self._ext_info = None
        self._insert_count = None
        self._modified_count = None

    @property
    def exception_count(self):
        return self._exception_count

    @exception_count.setter
    def exception_count(self, value):
        self._exception_count = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def insert_count(self):
        return self._insert_count

    @insert_count.setter
    def insert_count(self, value):
        self._insert_count = value
    @property
    def modified_count(self):
        return self._modified_count

    @modified_count.setter
    def modified_count(self, value):
        self._modified_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.exception_count:
            if hasattr(self.exception_count, 'to_alipay_dict'):
                params['exception_count'] = self.exception_count.to_alipay_dict()
            else:
                params['exception_count'] = self.exception_count
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.insert_count:
            if hasattr(self.insert_count, 'to_alipay_dict'):
                params['insert_count'] = self.insert_count.to_alipay_dict()
            else:
                params['insert_count'] = self.insert_count
        if self.modified_count:
            if hasattr(self.modified_count, 'to_alipay_dict'):
                params['modified_count'] = self.modified_count.to_alipay_dict()
            else:
                params['modified_count'] = self.modified_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CorpusSyncResult()
        if 'exception_count' in d:
            o.exception_count = d['exception_count']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'insert_count' in d:
            o.insert_count = d['insert_count']
        if 'modified_count' in d:
            o.modified_count = d['modified_count']
        return o


