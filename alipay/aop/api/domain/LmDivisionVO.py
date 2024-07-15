#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LmDivisionVO(object):

    def __init__(self):
        self._division_code = None
        self._division_level = None
        self._division_name = None
        self._parent_id = None
        self._pinyin = None

    @property
    def division_code(self):
        return self._division_code

    @division_code.setter
    def division_code(self, value):
        self._division_code = value
    @property
    def division_level(self):
        return self._division_level

    @division_level.setter
    def division_level(self, value):
        self._division_level = value
    @property
    def division_name(self):
        return self._division_name

    @division_name.setter
    def division_name(self, value):
        self._division_name = value
    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value
    @property
    def pinyin(self):
        return self._pinyin

    @pinyin.setter
    def pinyin(self, value):
        self._pinyin = value


    def to_alipay_dict(self):
        params = dict()
        if self.division_code:
            if hasattr(self.division_code, 'to_alipay_dict'):
                params['division_code'] = self.division_code.to_alipay_dict()
            else:
                params['division_code'] = self.division_code
        if self.division_level:
            if hasattr(self.division_level, 'to_alipay_dict'):
                params['division_level'] = self.division_level.to_alipay_dict()
            else:
                params['division_level'] = self.division_level
        if self.division_name:
            if hasattr(self.division_name, 'to_alipay_dict'):
                params['division_name'] = self.division_name.to_alipay_dict()
            else:
                params['division_name'] = self.division_name
        if self.parent_id:
            if hasattr(self.parent_id, 'to_alipay_dict'):
                params['parent_id'] = self.parent_id.to_alipay_dict()
            else:
                params['parent_id'] = self.parent_id
        if self.pinyin:
            if hasattr(self.pinyin, 'to_alipay_dict'):
                params['pinyin'] = self.pinyin.to_alipay_dict()
            else:
                params['pinyin'] = self.pinyin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LmDivisionVO()
        if 'division_code' in d:
            o.division_code = d['division_code']
        if 'division_level' in d:
            o.division_level = d['division_level']
        if 'division_name' in d:
            o.division_name = d['division_name']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        if 'pinyin' in d:
            o.pinyin = d['pinyin']
        return o


