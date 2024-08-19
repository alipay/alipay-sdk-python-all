#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsKocshorturlGenerateModel(object):

    def __init__(self):
        self._inst_code = None
        self._koc_uid = None
        self._open_id = None
        self._request_id = None

    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def koc_uid(self):
        return self._koc_uid

    @koc_uid.setter
    def koc_uid(self, value):
        self._koc_uid = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.koc_uid:
            if hasattr(self.koc_uid, 'to_alipay_dict'):
                params['koc_uid'] = self.koc_uid.to_alipay_dict()
            else:
                params['koc_uid'] = self.koc_uid
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsKocshorturlGenerateModel()
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'koc_uid' in d:
            o.koc_uid = d['koc_uid']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


