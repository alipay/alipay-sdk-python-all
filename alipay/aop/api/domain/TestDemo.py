#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TestDemo(object):

    def __init__(self):
        self._a_open_id = None
        self._a_uid = None
        self._date_a = None
        self._open_id = None
        self._price_a = None
        self._string_a = None
        self._string_yingshe = None
        self._string_yingshe_1_open_id = None
        self._string_yingshe_2_openid = None
        self._uid = None

    @property
    def a_open_id(self):
        return self._a_open_id

    @a_open_id.setter
    def a_open_id(self, value):
        self._a_open_id = value
    @property
    def a_uid(self):
        return self._a_uid

    @a_uid.setter
    def a_uid(self, value):
        self._a_uid = value
    @property
    def date_a(self):
        return self._date_a

    @date_a.setter
    def date_a(self, value):
        if isinstance(value, list):
            self._date_a = list()
            for i in value:
                self._date_a.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def price_a(self):
        return self._price_a

    @price_a.setter
    def price_a(self, value):
        if isinstance(value, list):
            self._price_a = list()
            for i in value:
                self._price_a.append(i)
    @property
    def string_a(self):
        return self._string_a

    @string_a.setter
    def string_a(self, value):
        if isinstance(value, list):
            self._string_a = list()
            for i in value:
                self._string_a.append(i)
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
        if self.a_open_id:
            if hasattr(self.a_open_id, 'to_alipay_dict'):
                params['a_open_id'] = self.a_open_id.to_alipay_dict()
            else:
                params['a_open_id'] = self.a_open_id
        if self.a_uid:
            if hasattr(self.a_uid, 'to_alipay_dict'):
                params['a_uid'] = self.a_uid.to_alipay_dict()
            else:
                params['a_uid'] = self.a_uid
        if self.date_a:
            if isinstance(self.date_a, list):
                for i in range(0, len(self.date_a)):
                    element = self.date_a[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.date_a[i] = element.to_alipay_dict()
            if hasattr(self.date_a, 'to_alipay_dict'):
                params['date_a'] = self.date_a.to_alipay_dict()
            else:
                params['date_a'] = self.date_a
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.price_a:
            if isinstance(self.price_a, list):
                for i in range(0, len(self.price_a)):
                    element = self.price_a[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.price_a[i] = element.to_alipay_dict()
            if hasattr(self.price_a, 'to_alipay_dict'):
                params['price_a'] = self.price_a.to_alipay_dict()
            else:
                params['price_a'] = self.price_a
        if self.string_a:
            if isinstance(self.string_a, list):
                for i in range(0, len(self.string_a)):
                    element = self.string_a[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.string_a[i] = element.to_alipay_dict()
            if hasattr(self.string_a, 'to_alipay_dict'):
                params['string_a'] = self.string_a.to_alipay_dict()
            else:
                params['string_a'] = self.string_a
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
        if 'a_open_id' in d:
            o.a_open_id = d['a_open_id']
        if 'a_uid' in d:
            o.a_uid = d['a_uid']
        if 'date_a' in d:
            o.date_a = d['date_a']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'price_a' in d:
            o.price_a = d['price_a']
        if 'string_a' in d:
            o.string_a = d['string_a']
        if 'string_yingshe' in d:
            o.string_yingshe = d['string_yingshe']
        if 'string_yingshe_1_open_id' in d:
            o.string_yingshe_1_open_id = d['string_yingshe_1_open_id']
        if 'string_yingshe_2_openid' in d:
            o.string_yingshe_2_openid = d['string_yingshe_2_openid']
        if 'uid' in d:
            o.uid = d['uid']
        return o


