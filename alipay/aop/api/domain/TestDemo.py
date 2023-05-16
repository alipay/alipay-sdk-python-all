#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TestDemo(object):

    def __init__(self):
        self._open_id = None
        self._string_yingshe = None
        self._string_yingshe_1_open_id = None
        self._string_yingshe_2_openid = None
        self._uid = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def string_yingshe(self):
        return self._string_yingshe

    @string_yingshe.setter
    def string_yingshe(self, value):
        self._string_yingshe = value
    @property
    def string_yingshe_1_open_id(self):
        return self._string_yingshe_1_open_id

    @string_yingshe_1_open_id.setter
    def string_yingshe_1_open_id(self, value):
        self._string_yingshe_1_open_id = value
    @property
    def string_yingshe_2_openid(self):
        return self._string_yingshe_2_openid

    @string_yingshe_2_openid.setter
    def string_yingshe_2_openid(self, value):
        self._string_yingshe_2_openid = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.string_yingshe:
            if hasattr(self.string_yingshe, 'to_alipay_dict'):
                params['string_yingshe'] = self.string_yingshe.to_alipay_dict()
            else:
                params['string_yingshe'] = self.string_yingshe
        if self.string_yingshe_1_open_id:
            if hasattr(self.string_yingshe_1_open_id, 'to_alipay_dict'):
                params['string_yingshe_1_open_id'] = self.string_yingshe_1_open_id.to_alipay_dict()
            else:
                params['string_yingshe_1_open_id'] = self.string_yingshe_1_open_id
        if self.string_yingshe_2_openid:
            if hasattr(self.string_yingshe_2_openid, 'to_alipay_dict'):
                params['string_yingshe_2_openid'] = self.string_yingshe_2_openid.to_alipay_dict()
            else:
                params['string_yingshe_2_openid'] = self.string_yingshe_2_openid
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TestDemo()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'string_yingshe' in d:
            o.string_yingshe = d['string_yingshe']
        if 'string_yingshe_1_open_id' in d:
            o.string_yingshe_1_open_id = d['string_yingshe_1_open_id']
        if 'string_yingshe_2_openid' in d:
            o.string_yingshe_2_openid = d['string_yingshe_2_openid']
        if 'uid' in d:
            o.uid = d['uid']
        return o


