#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PubNestPub import PubNestPub


class AlipayDataDdtJhjtestCreateModel(object):

    def __init__(self):
        self._com_a = None
        self._id = None
        self._id_openid = None
        self._input_a = None
        self._input_b = None
        self._input_c = None
        self._input_d = None
        self._input_ee = None
        self._map_a_openid = None

    @property
    def com_a(self):
        return self._com_a

    @com_a.setter
    def com_a(self, value):
        if isinstance(value, PubNestPub):
            self._com_a = value
        else:
            self._com_a = PubNestPub.from_alipay_dict(value)
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def id_openid(self):
        return self._id_openid

    @id_openid.setter
    def id_openid(self, value):
        self._id_openid = value
    @property
    def input_a(self):
        return self._input_a

    @input_a.setter
    def input_a(self, value):
        self._input_a = value
    @property
    def input_b(self):
        return self._input_b

    @input_b.setter
    def input_b(self, value):
        self._input_b = value
    @property
    def input_c(self):
        return self._input_c

    @input_c.setter
    def input_c(self, value):
        self._input_c = value
    @property
    def input_d(self):
        return self._input_d

    @input_d.setter
    def input_d(self, value):
        self._input_d = value
    @property
    def input_ee(self):
        return self._input_ee

    @input_ee.setter
    def input_ee(self, value):
        self._input_ee = value
    @property
    def map_a_openid(self):
        return self._map_a_openid

    @map_a_openid.setter
    def map_a_openid(self, value):
        self._map_a_openid = value


    def to_alipay_dict(self):
        params = dict()
        if self.com_a:
            if hasattr(self.com_a, 'to_alipay_dict'):
                params['com_a'] = self.com_a.to_alipay_dict()
            else:
                params['com_a'] = self.com_a
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.id_openid:
            if hasattr(self.id_openid, 'to_alipay_dict'):
                params['id_openid'] = self.id_openid.to_alipay_dict()
            else:
                params['id_openid'] = self.id_openid
        if self.input_a:
            if hasattr(self.input_a, 'to_alipay_dict'):
                params['input_a'] = self.input_a.to_alipay_dict()
            else:
                params['input_a'] = self.input_a
        if self.input_b:
            if hasattr(self.input_b, 'to_alipay_dict'):
                params['input_b'] = self.input_b.to_alipay_dict()
            else:
                params['input_b'] = self.input_b
        if self.input_c:
            if hasattr(self.input_c, 'to_alipay_dict'):
                params['input_c'] = self.input_c.to_alipay_dict()
            else:
                params['input_c'] = self.input_c
        if self.input_d:
            if hasattr(self.input_d, 'to_alipay_dict'):
                params['input_d'] = self.input_d.to_alipay_dict()
            else:
                params['input_d'] = self.input_d
        if self.input_ee:
            if hasattr(self.input_ee, 'to_alipay_dict'):
                params['input_ee'] = self.input_ee.to_alipay_dict()
            else:
                params['input_ee'] = self.input_ee
        if self.map_a_openid:
            if hasattr(self.map_a_openid, 'to_alipay_dict'):
                params['map_a_openid'] = self.map_a_openid.to_alipay_dict()
            else:
                params['map_a_openid'] = self.map_a_openid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDdtJhjtestCreateModel()
        if 'com_a' in d:
            o.com_a = d['com_a']
        if 'id' in d:
            o.id = d['id']
        if 'id_openid' in d:
            o.id_openid = d['id_openid']
        if 'input_a' in d:
            o.input_a = d['input_a']
        if 'input_b' in d:
            o.input_b = d['input_b']
        if 'input_c' in d:
            o.input_c = d['input_c']
        if 'input_d' in d:
            o.input_d = d['input_d']
        if 'input_ee' in d:
            o.input_ee = d['input_ee']
        if 'map_a_openid' in d:
            o.map_a_openid = d['map_a_openid']
        return o


