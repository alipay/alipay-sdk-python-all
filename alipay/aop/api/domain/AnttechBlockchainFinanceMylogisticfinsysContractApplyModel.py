#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceMylogisticfinsysContractApplyModel(object):

    def __init__(self):
        self._contract_name = None

    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceMylogisticfinsysContractApplyModel()
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        return o


