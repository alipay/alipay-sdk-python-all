#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractConsultResultVO import ContractConsultResultVO


class InterTradeConsultOpenApiResult(object):

    def __init__(self):
        self._contracts = None
        self._need_approval = None

    @property
    def contracts(self):
        return self._contracts

    @contracts.setter
    def contracts(self, value):
        if isinstance(value, list):
            self._contracts = list()
            for i in value:
                if isinstance(i, ContractConsultResultVO):
                    self._contracts.append(i)
                else:
                    self._contracts.append(ContractConsultResultVO.from_alipay_dict(i))
    @property
    def need_approval(self):
        return self._need_approval

    @need_approval.setter
    def need_approval(self, value):
        self._need_approval = value


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
        if self.need_approval:
            if hasattr(self.need_approval, 'to_alipay_dict'):
                params['need_approval'] = self.need_approval.to_alipay_dict()
            else:
                params['need_approval'] = self.need_approval
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InterTradeConsultOpenApiResult()
        if 'contracts' in d:
            o.contracts = d['contracts']
        if 'need_approval' in d:
            o.need_approval = d['need_approval']
        return o


