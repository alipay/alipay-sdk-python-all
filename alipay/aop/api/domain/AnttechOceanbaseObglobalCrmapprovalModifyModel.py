#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalCrmapprovalModifyModel(object):

    def __init__(self):
        self._crm_approval_status = None
        self._modifier = None
        self._payment_settlement_no = None

    @property
    def crm_approval_status(self):
        return self._crm_approval_status

    @crm_approval_status.setter
    def crm_approval_status(self, value):
        self._crm_approval_status = value
    @property
    def modifier(self):
        return self._modifier

    @modifier.setter
    def modifier(self, value):
        self._modifier = value
    @property
    def payment_settlement_no(self):
        return self._payment_settlement_no

    @payment_settlement_no.setter
    def payment_settlement_no(self, value):
        self._payment_settlement_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.crm_approval_status:
            if hasattr(self.crm_approval_status, 'to_alipay_dict'):
                params['crm_approval_status'] = self.crm_approval_status.to_alipay_dict()
            else:
                params['crm_approval_status'] = self.crm_approval_status
        if self.modifier:
            if hasattr(self.modifier, 'to_alipay_dict'):
                params['modifier'] = self.modifier.to_alipay_dict()
            else:
                params['modifier'] = self.modifier
        if self.payment_settlement_no:
            if hasattr(self.payment_settlement_no, 'to_alipay_dict'):
                params['payment_settlement_no'] = self.payment_settlement_no.to_alipay_dict()
            else:
                params['payment_settlement_no'] = self.payment_settlement_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalCrmapprovalModifyModel()
        if 'crm_approval_status' in d:
            o.crm_approval_status = d['crm_approval_status']
        if 'modifier' in d:
            o.modifier = d['modifier']
        if 'payment_settlement_no' in d:
            o.payment_settlement_no = d['payment_settlement_no']
        return o


