#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GFAOpenAPIAccountingAcceptance import GFAOpenAPIAccountingAcceptance


class AlipayBossFncGfacceptanceAccountingAcceptModel(object):

    def __init__(self):
        self._accounting_acceptance = None
        self._principal_id = None

    @property
    def accounting_acceptance(self):
        return self._accounting_acceptance

    @accounting_acceptance.setter
    def accounting_acceptance(self, value):
        if isinstance(value, GFAOpenAPIAccountingAcceptance):
            self._accounting_acceptance = value
        else:
            self._accounting_acceptance = GFAOpenAPIAccountingAcceptance.from_alipay_dict(value)
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.accounting_acceptance:
            if hasattr(self.accounting_acceptance, 'to_alipay_dict'):
                params['accounting_acceptance'] = self.accounting_acceptance.to_alipay_dict()
            else:
                params['accounting_acceptance'] = self.accounting_acceptance
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
        o = AlipayBossFncGfacceptanceAccountingAcceptModel()
        if 'accounting_acceptance' in d:
            o.accounting_acceptance = d['accounting_acceptance']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        return o


