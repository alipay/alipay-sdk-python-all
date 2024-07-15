#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AreaInfoVO(object):

    def __init__(self):
        self._code = None
        self._en_name = None
        self._name = None
        self._parent_code = None
        self._spell = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def en_name(self):
        return self._en_name

    @en_name.setter
    def en_name(self, value):
        self._en_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def parent_code(self):
        return self._parent_code

    @parent_code.setter
    def parent_code(self, value):
        self._parent_code = value
    @property
    def spell(self):
        return self._spell

    @spell.setter
    def spell(self, value):
        self._spell = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.en_name:
            if hasattr(self.en_name, 'to_alipay_dict'):
                params['en_name'] = self.en_name.to_alipay_dict()
            else:
                params['en_name'] = self.en_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.parent_code:
            if hasattr(self.parent_code, 'to_alipay_dict'):
                params['parent_code'] = self.parent_code.to_alipay_dict()
            else:
                params['parent_code'] = self.parent_code
        if self.spell:
            if hasattr(self.spell, 'to_alipay_dict'):
                params['spell'] = self.spell.to_alipay_dict()
            else:
                params['spell'] = self.spell
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AreaInfoVO()
        if 'code' in d:
            o.code = d['code']
        if 'en_name' in d:
            o.en_name = d['en_name']
        if 'name' in d:
            o.name = d['name']
        if 'parent_code' in d:
            o.parent_code = d['parent_code']
        if 'spell' in d:
            o.spell = d['spell']
        return o


