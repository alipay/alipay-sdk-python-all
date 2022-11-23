#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WidgetDataAuditPassResult(object):

    def __init__(self):
        self._alipay_data_id = None
        self._data_id = None

    @property
    def alipay_data_id(self):
        return self._alipay_data_id

    @alipay_data_id.setter
    def alipay_data_id(self, value):
        self._alipay_data_id = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_data_id:
            if hasattr(self.alipay_data_id, 'to_alipay_dict'):
                params['alipay_data_id'] = self.alipay_data_id.to_alipay_dict()
            else:
                params['alipay_data_id'] = self.alipay_data_id
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WidgetDataAuditPassResult()
        if 'alipay_data_id' in d:
            o.alipay_data_id = d['alipay_data_id']
        if 'data_id' in d:
            o.data_id = d['data_id']
        return o


