#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GFAOpenAPIBillAcceptance import GFAOpenAPIBillAcceptance


class AlipayBossFncGfacceptanceBillAcceptModel(object):

    def __init__(self):
        self._bill_acceptance = None
        self._principal_id = None

    @property
    def bill_acceptance(self):
        return self._bill_acceptance

    @bill_acceptance.setter
    def bill_acceptance(self, value):
        if isinstance(value, GFAOpenAPIBillAcceptance):
            self._bill_acceptance = value
        else:
            self._bill_acceptance = GFAOpenAPIBillAcceptance.from_alipay_dict(value)
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_acceptance:
            if hasattr(self.bill_acceptance, 'to_alipay_dict'):
                params['bill_acceptance'] = self.bill_acceptance.to_alipay_dict()
            else:
                params['bill_acceptance'] = self.bill_acceptance
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfacceptanceBillAcceptModel()
        if 'bill_acceptance' in d:
            o.bill_acceptance = d['bill_acceptance']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        return o


