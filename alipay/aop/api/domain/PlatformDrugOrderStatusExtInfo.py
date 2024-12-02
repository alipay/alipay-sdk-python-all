#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PlatformDrugOrderStatusExtInfo(object):

    def __init__(self):
        self._gmt_refund = None
        self._logistics_company = None
        self._logistics_id = None
        self._refund_amount = None
        self._refund_reason = None

    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def logistics_company(self):
        return self._logistics_company

    @logistics_company.setter
    def logistics_company(self, value):
        self._logistics_company = value
    @property
    def logistics_id(self):
        return self._logistics_id

    @logistics_id.setter
    def logistics_id(self, value):
        self._logistics_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_refund:
            if hasattr(self.gmt_refund, 'to_alipay_dict'):
                params['gmt_refund'] = self.gmt_refund.to_alipay_dict()
            else:
                params['gmt_refund'] = self.gmt_refund
        if self.logistics_company:
            if hasattr(self.logistics_company, 'to_alipay_dict'):
                params['logistics_company'] = self.logistics_company.to_alipay_dict()
            else:
                params['logistics_company'] = self.logistics_company
        if self.logistics_id:
            if hasattr(self.logistics_id, 'to_alipay_dict'):
                params['logistics_id'] = self.logistics_id.to_alipay_dict()
            else:
                params['logistics_id'] = self.logistics_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlatformDrugOrderStatusExtInfo()
        if 'gmt_refund' in d:
            o.gmt_refund = d['gmt_refund']
        if 'logistics_company' in d:
            o.logistics_company = d['logistics_company']
        if 'logistics_id' in d:
            o.logistics_id = d['logistics_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        return o


