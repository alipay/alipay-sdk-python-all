#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SalesForceContractStatusSyncResult(object):

    def __init__(self):
        self._contract_status = None
        self._external_contract_id = None
        self._request_id = None

    @property
    def contract_status(self):
        return self._contract_status

    @contract_status.setter
    def contract_status(self, value):
        self._contract_status = value
    @property
    def external_contract_id(self):
        return self._external_contract_id

    @external_contract_id.setter
    def external_contract_id(self, value):
        self._external_contract_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_status:
            if hasattr(self.contract_status, 'to_alipay_dict'):
                params['contract_status'] = self.contract_status.to_alipay_dict()
            else:
                params['contract_status'] = self.contract_status
        if self.external_contract_id:
            if hasattr(self.external_contract_id, 'to_alipay_dict'):
                params['external_contract_id'] = self.external_contract_id.to_alipay_dict()
            else:
                params['external_contract_id'] = self.external_contract_id
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
        o = SalesForceContractStatusSyncResult()
        if 'contract_status' in d:
            o.contract_status = d['contract_status']
        if 'external_contract_id' in d:
            o.external_contract_id = d['external_contract_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


