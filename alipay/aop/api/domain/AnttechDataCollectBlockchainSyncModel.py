#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechDataCollectBlockchainSyncModel(object):

    def __init__(self):
        self._account_data = None
        self._block_chain_id = None
        self._contract_data = None
        self._end_height = None
        self._start_height = None
        self._transaction_data = None

    @property
    def account_data(self):
        return self._account_data

    @account_data.setter
    def account_data(self, value):
        self._account_data = value
    @property
    def block_chain_id(self):
        return self._block_chain_id

    @block_chain_id.setter
    def block_chain_id(self, value):
        self._block_chain_id = value
    @property
    def contract_data(self):
        return self._contract_data

    @contract_data.setter
    def contract_data(self, value):
        self._contract_data = value
    @property
    def end_height(self):
        return self._end_height

    @end_height.setter
    def end_height(self, value):
        self._end_height = value
    @property
    def start_height(self):
        return self._start_height

    @start_height.setter
    def start_height(self, value):
        self._start_height = value
    @property
    def transaction_data(self):
        return self._transaction_data

    @transaction_data.setter
    def transaction_data(self, value):
        self._transaction_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_data:
            if hasattr(self.account_data, 'to_alipay_dict'):
                params['account_data'] = self.account_data.to_alipay_dict()
            else:
                params['account_data'] = self.account_data
        if self.block_chain_id:
            if hasattr(self.block_chain_id, 'to_alipay_dict'):
                params['block_chain_id'] = self.block_chain_id.to_alipay_dict()
            else:
                params['block_chain_id'] = self.block_chain_id
        if self.contract_data:
            if hasattr(self.contract_data, 'to_alipay_dict'):
                params['contract_data'] = self.contract_data.to_alipay_dict()
            else:
                params['contract_data'] = self.contract_data
        if self.end_height:
            if hasattr(self.end_height, 'to_alipay_dict'):
                params['end_height'] = self.end_height.to_alipay_dict()
            else:
                params['end_height'] = self.end_height
        if self.start_height:
            if hasattr(self.start_height, 'to_alipay_dict'):
                params['start_height'] = self.start_height.to_alipay_dict()
            else:
                params['start_height'] = self.start_height
        if self.transaction_data:
            if hasattr(self.transaction_data, 'to_alipay_dict'):
                params['transaction_data'] = self.transaction_data.to_alipay_dict()
            else:
                params['transaction_data'] = self.transaction_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechDataCollectBlockchainSyncModel()
        if 'account_data' in d:
            o.account_data = d['account_data']
        if 'block_chain_id' in d:
            o.block_chain_id = d['block_chain_id']
        if 'contract_data' in d:
            o.contract_data = d['contract_data']
        if 'end_height' in d:
            o.end_height = d['end_height']
        if 'start_height' in d:
            o.start_height = d['start_height']
        if 'transaction_data' in d:
            o.transaction_data = d['transaction_data']
        return o


