#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCstrainingOrgstructureCreateormodifyModel(object):

    def __init__(self):
        self._action_type = None
        self._data = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCstrainingOrgstructureCreateormodifyModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'data' in d:
            o.data = d['data']
        return o


