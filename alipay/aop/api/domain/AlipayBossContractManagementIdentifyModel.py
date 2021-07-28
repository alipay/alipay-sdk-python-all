#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BatchInfo import BatchInfo


class AlipayBossContractManagementIdentifyModel(object):

    def __init__(self):
        self._biz_source = None
        self._contracts = None

    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def contracts(self):
        return self._contracts

    @contracts.setter
    def contracts(self, value):
        if isinstance(value, list):
            self._contracts = list()
            for i in value:
                if isinstance(i, BatchInfo):
                    self._contracts.append(i)
                else:
                    self._contracts.append(BatchInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossContractManagementIdentifyModel()
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'contracts' in d:
            o.contracts = d['contracts']
        return o


