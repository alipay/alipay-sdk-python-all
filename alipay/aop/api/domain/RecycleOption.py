#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleOption(object):

    def __init__(self):
        self._option_code = None
        self._option_name = None
        self._relation_id = None

    @property
    def option_code(self):
        return self._option_code

    @option_code.setter
    def option_code(self, value):
        self._option_code = value
    @property
    def option_name(self):
        return self._option_name

    @option_name.setter
    def option_name(self, value):
        self._option_name = value
    @property
    def relation_id(self):
        return self._relation_id

    @relation_id.setter
    def relation_id(self, value):
        self._relation_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.option_code:
            if hasattr(self.option_code, 'to_alipay_dict'):
                params['option_code'] = self.option_code.to_alipay_dict()
            else:
                params['option_code'] = self.option_code
        if self.option_name:
            if hasattr(self.option_name, 'to_alipay_dict'):
                params['option_name'] = self.option_name.to_alipay_dict()
            else:
                params['option_name'] = self.option_name
        if self.relation_id:
            if hasattr(self.relation_id, 'to_alipay_dict'):
                params['relation_id'] = self.relation_id.to_alipay_dict()
            else:
                params['relation_id'] = self.relation_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleOption()
        if 'option_code' in d:
            o.option_code = d['option_code']
        if 'option_name' in d:
            o.option_name = d['option_name']
        if 'relation_id' in d:
            o.relation_id = d['relation_id']
        return o


