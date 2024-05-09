#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcoContractInfo import EcoContractInfo


class AlipayEcoContractsLoanInfoSyncModel(object):

    def __init__(self):
        self._contracts = None
        self._sync_request_id = None

    @property
    def contracts(self):
        return self._contracts

    @contracts.setter
    def contracts(self, value):
        if isinstance(value, list):
            self._contracts = list()
            for i in value:
                if isinstance(i, EcoContractInfo):
                    self._contracts.append(i)
                else:
                    self._contracts.append(EcoContractInfo.from_alipay_dict(i))
    @property
    def sync_request_id(self):
        return self._sync_request_id

    @sync_request_id.setter
    def sync_request_id(self, value):
        self._sync_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.contracts:
            if isinstance(self.contracts, list):
                for i in range(0, len(self.contracts)):
                    element = self.contracts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contracts[i] = element.to_alipay_dict()
            if hasattr(self.contracts, 'to_alipay_dict'):
                params['contracts'] = self.contracts.to_alipay_dict()
            else:
                params['contracts'] = self.contracts
        if self.sync_request_id:
            if hasattr(self.sync_request_id, 'to_alipay_dict'):
                params['sync_request_id'] = self.sync_request_id.to_alipay_dict()
            else:
                params['sync_request_id'] = self.sync_request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoContractsLoanInfoSyncModel()
        if 'contracts' in d:
            o.contracts = d['contracts']
        if 'sync_request_id' in d:
            o.sync_request_id = d['sync_request_id']
        return o


