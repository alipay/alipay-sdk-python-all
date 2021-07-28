#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceAssetIssueSubmitModel(object):

    def __init__(self):
        self._asset_id = None
        self._pub_key = None
        self._sign_algorithm = None
        self._sign_data = None
        self._signature = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def pub_key(self):
        return self._pub_key

    @pub_key.setter
    def pub_key(self, value):
        self._pub_key = value
    @property
    def sign_algorithm(self):
        return self._sign_algorithm

    @sign_algorithm.setter
    def sign_algorithm(self, value):
        self._sign_algorithm = value
    @property
    def sign_data(self):
        return self._sign_data

    @sign_data.setter
    def sign_data(self, value):
        self._sign_data = value
    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        self._signature = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.pub_key:
            if hasattr(self.pub_key, 'to_alipay_dict'):
                params['pub_key'] = self.pub_key.to_alipay_dict()
            else:
                params['pub_key'] = self.pub_key
        if self.sign_algorithm:
            if hasattr(self.sign_algorithm, 'to_alipay_dict'):
                params['sign_algorithm'] = self.sign_algorithm.to_alipay_dict()
            else:
                params['sign_algorithm'] = self.sign_algorithm
        if self.sign_data:
            if hasattr(self.sign_data, 'to_alipay_dict'):
                params['sign_data'] = self.sign_data.to_alipay_dict()
            else:
                params['sign_data'] = self.sign_data
        if self.signature:
            if hasattr(self.signature, 'to_alipay_dict'):
                params['signature'] = self.signature.to_alipay_dict()
            else:
                params['signature'] = self.signature
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceAssetIssueSubmitModel()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'pub_key' in d:
            o.pub_key = d['pub_key']
        if 'sign_algorithm' in d:
            o.sign_algorithm = d['sign_algorithm']
        if 'sign_data' in d:
            o.sign_data = d['sign_data']
        if 'signature' in d:
            o.signature = d['signature']
        return o


