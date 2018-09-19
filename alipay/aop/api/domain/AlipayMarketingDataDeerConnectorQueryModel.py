#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingDataDeerConnectorQueryModel(object):

    def __init__(self):
        self._connector_id = None
        self._params = None

    @property
    def connector_id(self):
        return self._connector_id

    @connector_id.setter
    def connector_id(self, value):
        self._connector_id = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value


    def to_alipay_dict(self):
        params = dict()
        if self.connector_id:
            if hasattr(self.connector_id, 'to_alipay_dict'):
                params['connector_id'] = self.connector_id.to_alipay_dict()
            else:
                params['connector_id'] = self.connector_id
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingDataDeerConnectorQueryModel()
        if 'connector_id' in d:
            o.connector_id = d['connector_id']
        if 'params' in d:
            o.params = d['params']
        return o


