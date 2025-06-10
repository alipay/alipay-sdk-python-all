#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTerminalEdgecloudSwnetflowPoolusageSyncModel(object):

    def __init__(self):
        self._biling_cycle = None
        self._credential_name = None
        self._data_type = None
        self._pool_id = None
        self._rest_flow = None
        self._total_flow = None
        self._usage_ratio = None

    @property
    def biling_cycle(self):
        return self._biling_cycle

    @biling_cycle.setter
    def biling_cycle(self, value):
        self._biling_cycle = value
    @property
    def credential_name(self):
        return self._credential_name

    @credential_name.setter
    def credential_name(self, value):
        self._credential_name = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def pool_id(self):
        return self._pool_id

    @pool_id.setter
    def pool_id(self, value):
        self._pool_id = value
    @property
    def rest_flow(self):
        return self._rest_flow

    @rest_flow.setter
    def rest_flow(self, value):
        self._rest_flow = value
    @property
    def total_flow(self):
        return self._total_flow

    @total_flow.setter
    def total_flow(self, value):
        self._total_flow = value
    @property
    def usage_ratio(self):
        return self._usage_ratio

    @usage_ratio.setter
    def usage_ratio(self, value):
        self._usage_ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.biling_cycle:
            if hasattr(self.biling_cycle, 'to_alipay_dict'):
                params['biling_cycle'] = self.biling_cycle.to_alipay_dict()
            else:
                params['biling_cycle'] = self.biling_cycle
        if self.credential_name:
            if hasattr(self.credential_name, 'to_alipay_dict'):
                params['credential_name'] = self.credential_name.to_alipay_dict()
            else:
                params['credential_name'] = self.credential_name
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.pool_id:
            if hasattr(self.pool_id, 'to_alipay_dict'):
                params['pool_id'] = self.pool_id.to_alipay_dict()
            else:
                params['pool_id'] = self.pool_id
        if self.rest_flow:
            if hasattr(self.rest_flow, 'to_alipay_dict'):
                params['rest_flow'] = self.rest_flow.to_alipay_dict()
            else:
                params['rest_flow'] = self.rest_flow
        if self.total_flow:
            if hasattr(self.total_flow, 'to_alipay_dict'):
                params['total_flow'] = self.total_flow.to_alipay_dict()
            else:
                params['total_flow'] = self.total_flow
        if self.usage_ratio:
            if hasattr(self.usage_ratio, 'to_alipay_dict'):
                params['usage_ratio'] = self.usage_ratio.to_alipay_dict()
            else:
                params['usage_ratio'] = self.usage_ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTerminalEdgecloudSwnetflowPoolusageSyncModel()
        if 'biling_cycle' in d:
            o.biling_cycle = d['biling_cycle']
        if 'credential_name' in d:
            o.credential_name = d['credential_name']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'pool_id' in d:
            o.pool_id = d['pool_id']
        if 'rest_flow' in d:
            o.rest_flow = d['rest_flow']
        if 'total_flow' in d:
            o.total_flow = d['total_flow']
        if 'usage_ratio' in d:
            o.usage_ratio = d['usage_ratio']
        return o


