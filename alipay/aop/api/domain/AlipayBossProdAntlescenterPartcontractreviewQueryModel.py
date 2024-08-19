#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntlescenterPartcontractreviewQueryModel(object):

    def __init__(self):
        self._audit_type = None
        self._contract_no = None

    @property
    def audit_type(self):
        return self._audit_type

    @audit_type.setter
    def audit_type(self, value):
        self._audit_type = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_type:
            if hasattr(self.audit_type, 'to_alipay_dict'):
                params['audit_type'] = self.audit_type.to_alipay_dict()
            else:
                params['audit_type'] = self.audit_type
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlescenterPartcontractreviewQueryModel()
        if 'audit_type' in d:
            o.audit_type = d['audit_type']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        return o


