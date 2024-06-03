#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdQingyongtestQueryModel(object):

    def __init__(self):
        self._enum_2 = None
        self._enums = None
        self._key_id = None

    @property
    def enum_2(self):
        return self._enum_2

    @enum_2.setter
    def enum_2(self, value):
        self._enum_2 = value
    @property
    def enums(self):
        return self._enums

    @enums.setter
    def enums(self, value):
        self._enums = value
    @property
    def key_id(self):
        return self._key_id

    @key_id.setter
    def key_id(self, value):
        self._key_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enum_2:
            if hasattr(self.enum_2, 'to_alipay_dict'):
                params['enum_2'] = self.enum_2.to_alipay_dict()
            else:
                params['enum_2'] = self.enum_2
        if self.enums:
            if hasattr(self.enums, 'to_alipay_dict'):
                params['enums'] = self.enums.to_alipay_dict()
            else:
                params['enums'] = self.enums
        if self.key_id:
            if hasattr(self.key_id, 'to_alipay_dict'):
                params['key_id'] = self.key_id.to_alipay_dict()
            else:
                params['key_id'] = self.key_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdQingyongtestQueryModel()
        if 'enum_2' in d:
            o.enum_2 = d['enum_2']
        if 'enums' in d:
            o.enums = d['enums']
        if 'key_id' in d:
            o.key_id = d['key_id']
        return o


