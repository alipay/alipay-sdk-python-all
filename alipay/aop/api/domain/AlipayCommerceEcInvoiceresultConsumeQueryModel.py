#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcInvoiceresultConsumeQueryModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._invoice_apply_id = None
        self._outer_apply_id = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def invoice_apply_id(self):
        return self._invoice_apply_id

    @invoice_apply_id.setter
    def invoice_apply_id(self, value):
        self._invoice_apply_id = value
    @property
    def outer_apply_id(self):
        return self._outer_apply_id

    @outer_apply_id.setter
    def outer_apply_id(self, value):
        self._outer_apply_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.invoice_apply_id:
            if hasattr(self.invoice_apply_id, 'to_alipay_dict'):
                params['invoice_apply_id'] = self.invoice_apply_id.to_alipay_dict()
            else:
                params['invoice_apply_id'] = self.invoice_apply_id
        if self.outer_apply_id:
            if hasattr(self.outer_apply_id, 'to_alipay_dict'):
                params['outer_apply_id'] = self.outer_apply_id.to_alipay_dict()
            else:
                params['outer_apply_id'] = self.outer_apply_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcInvoiceresultConsumeQueryModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'invoice_apply_id' in d:
            o.invoice_apply_id = d['invoice_apply_id']
        if 'outer_apply_id' in d:
            o.outer_apply_id = d['outer_apply_id']
        return o


