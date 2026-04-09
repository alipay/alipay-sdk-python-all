#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FileList import FileList


class AlipaySecurityProdAltechlegalDepositCreateModel(object):

    def __init__(self):
        self._category_code = None
        self._corp_code = None
        self._deposit_name = None
        self._device_info = None
        self._file_list = None
        self._record_address = None
        self._source = None

    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def corp_code(self):
        return self._corp_code

    @corp_code.setter
    def corp_code(self, value):
        self._corp_code = value
    @property
    def deposit_name(self):
        return self._deposit_name

    @deposit_name.setter
    def deposit_name(self, value):
        self._deposit_name = value
    @property
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        self._device_info = value
    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                if isinstance(i, FileList):
                    self._file_list.append(i)
                else:
                    self._file_list.append(FileList.from_alipay_dict(i))
    @property
    def record_address(self):
        return self._record_address

    @record_address.setter
    def record_address(self, value):
        self._record_address = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.corp_code:
            if hasattr(self.corp_code, 'to_alipay_dict'):
                params['corp_code'] = self.corp_code.to_alipay_dict()
            else:
                params['corp_code'] = self.corp_code
        if self.deposit_name:
            if hasattr(self.deposit_name, 'to_alipay_dict'):
                params['deposit_name'] = self.deposit_name.to_alipay_dict()
            else:
                params['deposit_name'] = self.deposit_name
        if self.device_info:
            if hasattr(self.device_info, 'to_alipay_dict'):
                params['device_info'] = self.device_info.to_alipay_dict()
            else:
                params['device_info'] = self.device_info
        if self.file_list:
            if isinstance(self.file_list, list):
                for i in range(0, len(self.file_list)):
                    element = self.file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_list[i] = element.to_alipay_dict()
            if hasattr(self.file_list, 'to_alipay_dict'):
                params['file_list'] = self.file_list.to_alipay_dict()
            else:
                params['file_list'] = self.file_list
        if self.record_address:
            if hasattr(self.record_address, 'to_alipay_dict'):
                params['record_address'] = self.record_address.to_alipay_dict()
            else:
                params['record_address'] = self.record_address
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdAltechlegalDepositCreateModel()
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'corp_code' in d:
            o.corp_code = d['corp_code']
        if 'deposit_name' in d:
            o.deposit_name = d['deposit_name']
        if 'device_info' in d:
            o.device_info = d['device_info']
        if 'file_list' in d:
            o.file_list = d['file_list']
        if 'record_address' in d:
            o.record_address = d['record_address']
        if 'source' in d:
            o.source = d['source']
        return o


