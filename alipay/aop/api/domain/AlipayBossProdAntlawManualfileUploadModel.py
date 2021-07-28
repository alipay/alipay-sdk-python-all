#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractFileVO import ContractFileVO


class AlipayBossProdAntlawManualfileUploadModel(object):

    def __init__(self):
        self._biz_code = None
        self._file_list = None
        self._request_token = None
        self._source_sys = None
        self._time_stamp = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                if isinstance(i, ContractFileVO):
                    self._file_list.append(i)
                else:
                    self._file_list.append(ContractFileVO.from_alipay_dict(i))
    @property
    def request_token(self):
        return self._request_token

    @request_token.setter
    def request_token(self, value):
        self._request_token = value
    @property
    def source_sys(self):
        return self._source_sys

    @source_sys.setter
    def source_sys(self, value):
        self._source_sys = value
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
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
        if self.request_token:
            if hasattr(self.request_token, 'to_alipay_dict'):
                params['request_token'] = self.request_token.to_alipay_dict()
            else:
                params['request_token'] = self.request_token
        if self.source_sys:
            if hasattr(self.source_sys, 'to_alipay_dict'):
                params['source_sys'] = self.source_sys.to_alipay_dict()
            else:
                params['source_sys'] = self.source_sys
        if self.time_stamp:
            if hasattr(self.time_stamp, 'to_alipay_dict'):
                params['time_stamp'] = self.time_stamp.to_alipay_dict()
            else:
                params['time_stamp'] = self.time_stamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlawManualfileUploadModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'file_list' in d:
            o.file_list = d['file_list']
        if 'request_token' in d:
            o.request_token = d['request_token']
        if 'source_sys' in d:
            o.source_sys = d['source_sys']
        if 'time_stamp' in d:
            o.time_stamp = d['time_stamp']
        return o


