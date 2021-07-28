#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceRiskApplyModel(object):

    def __init__(self):
        self._asset_type = None
        self._request_id = None
        self._risk_object = None
        self._risk_type = None

    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def risk_object(self):
        return self._risk_object

    @risk_object.setter
    def risk_object(self, value):
        self._risk_object = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.risk_object:
            if hasattr(self.risk_object, 'to_alipay_dict'):
                params['risk_object'] = self.risk_object.to_alipay_dict()
            else:
                params['risk_object'] = self.risk_object
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceRiskApplyModel()
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'risk_object' in d:
            o.risk_object = d['risk_object']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        return o


