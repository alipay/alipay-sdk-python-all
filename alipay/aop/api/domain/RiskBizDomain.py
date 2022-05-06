#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskBizDomain(object):

    def __init__(self):
        self._code = None
        self._description = None
        self._english_name = None
        self._full_name = None
        self._name = None
        self._name_pinyin = None
        self._tnt_inst_id = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def english_name(self):
        return self._english_name

    @english_name.setter
    def english_name(self, value):
        self._english_name = value
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def name_pinyin(self):
        return self._name_pinyin

    @name_pinyin.setter
    def name_pinyin(self, value):
        self._name_pinyin = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.english_name:
            if hasattr(self.english_name, 'to_alipay_dict'):
                params['english_name'] = self.english_name.to_alipay_dict()
            else:
                params['english_name'] = self.english_name
        if self.full_name:
            if hasattr(self.full_name, 'to_alipay_dict'):
                params['full_name'] = self.full_name.to_alipay_dict()
            else:
                params['full_name'] = self.full_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.name_pinyin:
            if hasattr(self.name_pinyin, 'to_alipay_dict'):
                params['name_pinyin'] = self.name_pinyin.to_alipay_dict()
            else:
                params['name_pinyin'] = self.name_pinyin
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskBizDomain()
        if 'code' in d:
            o.code = d['code']
        if 'description' in d:
            o.description = d['description']
        if 'english_name' in d:
            o.english_name = d['english_name']
        if 'full_name' in d:
            o.full_name = d['full_name']
        if 'name' in d:
            o.name = d['name']
        if 'name_pinyin' in d:
            o.name_pinyin = d['name_pinyin']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


