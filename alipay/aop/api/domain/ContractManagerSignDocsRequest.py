#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractManagerSignDocsRequest(object):

    def __init__(self):
        self._file_id = None
        self._file_name = None
        self._total_page = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.total_page:
            if hasattr(self.total_page, 'to_alipay_dict'):
                params['total_page'] = self.total_page.to_alipay_dict()
            else:
                params['total_page'] = self.total_page
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractManagerSignDocsRequest()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'total_page' in d:
            o.total_page = d['total_page']
        return o


