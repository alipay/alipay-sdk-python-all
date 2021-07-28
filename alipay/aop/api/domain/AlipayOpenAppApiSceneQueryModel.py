#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppApiSceneQueryModel(object):

    def __init__(self):
        self._api_name = None
        self._field_name = None

    @property
    def api_name(self):
        return self._api_name

    @api_name.setter
    def api_name(self, value):
        self._api_name = value
    @property
    def field_name(self):
        return self._field_name

    @field_name.setter
    def field_name(self, value):
        self._field_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_name:
            if hasattr(self.api_name, 'to_alipay_dict'):
                params['api_name'] = self.api_name.to_alipay_dict()
            else:
                params['api_name'] = self.api_name
        if self.field_name:
            if hasattr(self.field_name, 'to_alipay_dict'):
                params['field_name'] = self.field_name.to_alipay_dict()
            else:
                params['field_name'] = self.field_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppApiSceneQueryModel()
        if 'api_name' in d:
            o.api_name = d['api_name']
        if 'field_name' in d:
            o.field_name = d['field_name']
        return o


