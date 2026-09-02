#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceNxactivityQueryModel(object):

    def __init__(self):
        self._act_scheme_id = None
        self._open_id = None

    @property
    def act_scheme_id(self):
        return self._act_scheme_id

    @act_scheme_id.setter
    def act_scheme_id(self, value):
        self._act_scheme_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.act_scheme_id:
            if hasattr(self.act_scheme_id, 'to_alipay_dict'):
                params['act_scheme_id'] = self.act_scheme_id.to_alipay_dict()
            else:
                params['act_scheme_id'] = self.act_scheme_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceNxactivityQueryModel()
        if 'act_scheme_id' in d:
            o.act_scheme_id = d['act_scheme_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        return o


