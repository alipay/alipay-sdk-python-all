#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ObfBillAcceptanceRequest import ObfBillAcceptanceRequest


class AnttechOceanbaseBillAcceptanceSyncModel(object):

    def __init__(self):
        self._obf_bill_acceptance_request = None

    @property
    def obf_bill_acceptance_request(self):
        return self._obf_bill_acceptance_request

    @obf_bill_acceptance_request.setter
    def obf_bill_acceptance_request(self, value):
        if isinstance(value, list):
            self._obf_bill_acceptance_request = list()
            for i in value:
                if isinstance(i, ObfBillAcceptanceRequest):
                    self._obf_bill_acceptance_request.append(i)
                else:
                    self._obf_bill_acceptance_request.append(ObfBillAcceptanceRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.obf_bill_acceptance_request:
            if isinstance(self.obf_bill_acceptance_request, list):
                for i in range(0, len(self.obf_bill_acceptance_request)):
                    element = self.obf_bill_acceptance_request[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.obf_bill_acceptance_request[i] = element.to_alipay_dict()
            if hasattr(self.obf_bill_acceptance_request, 'to_alipay_dict'):
                params['obf_bill_acceptance_request'] = self.obf_bill_acceptance_request.to_alipay_dict()
            else:
                params['obf_bill_acceptance_request'] = self.obf_bill_acceptance_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseBillAcceptanceSyncModel()
        if 'obf_bill_acceptance_request' in d:
            o.obf_bill_acceptance_request = d['obf_bill_acceptance_request']
        return o


