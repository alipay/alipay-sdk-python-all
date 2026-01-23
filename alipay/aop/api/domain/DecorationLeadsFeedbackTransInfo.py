#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DecorationLeadsFeedbackTransInfo(object):

    def __init__(self):
        self._contract_id = None
        self._deal_time = None
        self._status = None

    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def deal_time(self):
        return self._deal_time

    @deal_time.setter
    def deal_time(self, value):
        self._deal_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.deal_time:
            if hasattr(self.deal_time, 'to_alipay_dict'):
                params['deal_time'] = self.deal_time.to_alipay_dict()
            else:
                params['deal_time'] = self.deal_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DecorationLeadsFeedbackTransInfo()
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'deal_time' in d:
            o.deal_time = d['deal_time']
        if 'status' in d:
            o.status = d['status']
        return o


