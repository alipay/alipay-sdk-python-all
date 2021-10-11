#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceAssetRepaymentProveModel(object):

    def __init__(self):
        self._asset_package_id = None
        self._biz_date = None
        self._encode_type = None
        self._prove_encoded_req = None
        self._prove_encoded_res = None
        self._repay_action = None
        self._request_id = None

    @property
    def asset_package_id(self):
        return self._asset_package_id

    @asset_package_id.setter
    def asset_package_id(self, value):
        self._asset_package_id = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def encode_type(self):
        return self._encode_type

    @encode_type.setter
    def encode_type(self, value):
        self._encode_type = value
    @property
    def prove_encoded_req(self):
        return self._prove_encoded_req

    @prove_encoded_req.setter
    def prove_encoded_req(self, value):
        self._prove_encoded_req = value
    @property
    def prove_encoded_res(self):
        return self._prove_encoded_res

    @prove_encoded_res.setter
    def prove_encoded_res(self, value):
        self._prove_encoded_res = value
    @property
    def repay_action(self):
        return self._repay_action

    @repay_action.setter
    def repay_action(self, value):
        self._repay_action = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_package_id:
            if hasattr(self.asset_package_id, 'to_alipay_dict'):
                params['asset_package_id'] = self.asset_package_id.to_alipay_dict()
            else:
                params['asset_package_id'] = self.asset_package_id
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.encode_type:
            if hasattr(self.encode_type, 'to_alipay_dict'):
                params['encode_type'] = self.encode_type.to_alipay_dict()
            else:
                params['encode_type'] = self.encode_type
        if self.prove_encoded_req:
            if hasattr(self.prove_encoded_req, 'to_alipay_dict'):
                params['prove_encoded_req'] = self.prove_encoded_req.to_alipay_dict()
            else:
                params['prove_encoded_req'] = self.prove_encoded_req
        if self.prove_encoded_res:
            if hasattr(self.prove_encoded_res, 'to_alipay_dict'):
                params['prove_encoded_res'] = self.prove_encoded_res.to_alipay_dict()
            else:
                params['prove_encoded_res'] = self.prove_encoded_res
        if self.repay_action:
            if hasattr(self.repay_action, 'to_alipay_dict'):
                params['repay_action'] = self.repay_action.to_alipay_dict()
            else:
                params['repay_action'] = self.repay_action
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceAssetRepaymentProveModel()
        if 'asset_package_id' in d:
            o.asset_package_id = d['asset_package_id']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'encode_type' in d:
            o.encode_type = d['encode_type']
        if 'prove_encoded_req' in d:
            o.prove_encoded_req = d['prove_encoded_req']
        if 'prove_encoded_res' in d:
            o.prove_encoded_res = d['prove_encoded_res']
        if 'repay_action' in d:
            o.repay_action = d['repay_action']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


