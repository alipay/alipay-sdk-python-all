#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiContractFileMsgDTO(object):

    def __init__(self):
        self._contract_type = None
        self._file_name = None
        self._file_url = None

    @property
    def contract_type(self):
        return self._contract_type

    @contract_type.setter
    def contract_type(self, value):
        self._contract_type = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_type:
            if hasattr(self.contract_type, 'to_alipay_dict'):
                params['contract_type'] = self.contract_type.to_alipay_dict()
            else:
                params['contract_type'] = self.contract_type
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiContractFileMsgDTO()
        if 'contract_type' in d:
            o.contract_type = d['contract_type']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_url' in d:
            o.file_url = d['file_url']
        return o


