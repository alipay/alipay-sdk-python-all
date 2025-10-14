#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractChangeSyncRequest import ContractChangeSyncRequest


class AlipayBossFncGfsettleprodGfcontractcenterCreateormodifyModel(object):

    def __init__(self):
        self._contract_change_sync_request = None

    @property
    def contract_change_sync_request(self):
        return self._contract_change_sync_request

    @contract_change_sync_request.setter
    def contract_change_sync_request(self, value):
        if isinstance(value, ContractChangeSyncRequest):
            self._contract_change_sync_request = value
        else:
            self._contract_change_sync_request = ContractChangeSyncRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.contract_change_sync_request:
            if hasattr(self.contract_change_sync_request, 'to_alipay_dict'):
                params['contract_change_sync_request'] = self.contract_change_sync_request.to_alipay_dict()
            else:
                params['contract_change_sync_request'] = self.contract_change_sync_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodGfcontractcenterCreateormodifyModel()
        if 'contract_change_sync_request' in d:
            o.contract_change_sync_request = d['contract_change_sync_request']
        return o


