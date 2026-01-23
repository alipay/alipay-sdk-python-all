#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MeasureUnitVO(object):

    def __init__(self):
        self._unit_id = None
        self._unit_name = None
        self._unit_name_alias = None

    @property
    def unit_id(self):
        return self._unit_id

    @unit_id.setter
    def unit_id(self, value):
        self._unit_id = value
    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value
    @property
    def unit_name_alias(self):
        return self._unit_name_alias

    @unit_name_alias.setter
    def unit_name_alias(self, value):
        self._unit_name_alias = value


    def to_alipay_dict(self):
        params = dict()
        if self.unit_id:
            if hasattr(self.unit_id, 'to_alipay_dict'):
                params['unit_id'] = self.unit_id.to_alipay_dict()
            else:
                params['unit_id'] = self.unit_id
        if self.unit_name:
            if hasattr(self.unit_name, 'to_alipay_dict'):
                params['unit_name'] = self.unit_name.to_alipay_dict()
            else:
                params['unit_name'] = self.unit_name
        if self.unit_name_alias:
            if hasattr(self.unit_name_alias, 'to_alipay_dict'):
                params['unit_name_alias'] = self.unit_name_alias.to_alipay_dict()
            else:
                params['unit_name_alias'] = self.unit_name_alias
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MeasureUnitVO()
        if 'unit_id' in d:
            o.unit_id = d['unit_id']
        if 'unit_name' in d:
            o.unit_name = d['unit_name']
        if 'unit_name_alias' in d:
            o.unit_name_alias = d['unit_name_alias']
        return o


