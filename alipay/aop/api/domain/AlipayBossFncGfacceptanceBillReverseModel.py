#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GFAOpenAPIReverseBillAcceptance import GFAOpenAPIReverseBillAcceptance


class AlipayBossFncGfacceptanceBillReverseModel(object):

    def __init__(self):
        self._principal_id = None
        self._reverse_bill_acceptance = None

    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def reverse_bill_acceptance(self):
        return self._reverse_bill_acceptance

    @reverse_bill_acceptance.setter
    def reverse_bill_acceptance(self, value):
        if isinstance(value, GFAOpenAPIReverseBillAcceptance):
            self._reverse_bill_acceptance = value
        else:
            self._reverse_bill_acceptance = GFAOpenAPIReverseBillAcceptance.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.reverse_bill_acceptance:
            if hasattr(self.reverse_bill_acceptance, 'to_alipay_dict'):
                params['reverse_bill_acceptance'] = self.reverse_bill_acceptance.to_alipay_dict()
            else:
                params['reverse_bill_acceptance'] = self.reverse_bill_acceptance
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfacceptanceBillReverseModel()
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'reverse_bill_acceptance' in d:
            o.reverse_bill_acceptance = d['reverse_bill_acceptance']
        return o


