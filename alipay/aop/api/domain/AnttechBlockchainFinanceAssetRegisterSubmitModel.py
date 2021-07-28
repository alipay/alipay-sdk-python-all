#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceAssetRegisterSubmitModel(object):

    def __init__(self):
        self._asset_id = None
        self._asset_type = None
        self._operate = None
        self._submit_data = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def submit_data(self):
        return self._submit_data

    @submit_data.setter
    def submit_data(self, value):
        self._submit_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.submit_data:
            if hasattr(self.submit_data, 'to_alipay_dict'):
                params['submit_data'] = self.submit_data.to_alipay_dict()
            else:
                params['submit_data'] = self.submit_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceAssetRegisterSubmitModel()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'operate' in d:
            o.operate = d['operate']
        if 'submit_data' in d:
            o.submit_data = d['submit_data']
        return o


