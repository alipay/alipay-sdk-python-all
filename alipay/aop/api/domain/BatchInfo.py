#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InterTradeContractPartner import InterTradeContractPartner


class BatchInfo(object):

    def __init__(self):
        self._contract_no = None
        self._contract_partners = None

    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def contract_partners(self):
        return self._contract_partners

    @contract_partners.setter
    def contract_partners(self, value):
        if isinstance(value, list):
            self._contract_partners = list()
            for i in value:
                if isinstance(i, InterTradeContractPartner):
                    self._contract_partners.append(i)
                else:
                    self._contract_partners.append(InterTradeContractPartner.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.contract_partners:
            if isinstance(self.contract_partners, list):
                for i in range(0, len(self.contract_partners)):
                    element = self.contract_partners[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_partners[i] = element.to_alipay_dict()
            if hasattr(self.contract_partners, 'to_alipay_dict'):
                params['contract_partners'] = self.contract_partners.to_alipay_dict()
            else:
                params['contract_partners'] = self.contract_partners
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BatchInfo()
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'contract_partners' in d:
            o.contract_partners = d['contract_partners']
        return o


