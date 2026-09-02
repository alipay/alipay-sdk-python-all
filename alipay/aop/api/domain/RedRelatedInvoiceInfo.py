#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RedRelatedInvoiceInfo(object):

    def __init__(self):
        self._origin_invoice_kind = None
        self._origin_invoice_no = None
        self._red_reason = None

    @property
    def origin_invoice_kind(self):
        return self._origin_invoice_kind

    @origin_invoice_kind.setter
    def origin_invoice_kind(self, value):
        self._origin_invoice_kind = value
    @property
    def origin_invoice_no(self):
        return self._origin_invoice_no

    @origin_invoice_no.setter
    def origin_invoice_no(self, value):
        self._origin_invoice_no = value
    @property
    def red_reason(self):
        return self._red_reason

    @red_reason.setter
    def red_reason(self, value):
        self._red_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.origin_invoice_kind:
            if hasattr(self.origin_invoice_kind, 'to_alipay_dict'):
                params['origin_invoice_kind'] = self.origin_invoice_kind.to_alipay_dict()
            else:
                params['origin_invoice_kind'] = self.origin_invoice_kind
        if self.origin_invoice_no:
            if hasattr(self.origin_invoice_no, 'to_alipay_dict'):
                params['origin_invoice_no'] = self.origin_invoice_no.to_alipay_dict()
            else:
                params['origin_invoice_no'] = self.origin_invoice_no
        if self.red_reason:
            if hasattr(self.red_reason, 'to_alipay_dict'):
                params['red_reason'] = self.red_reason.to_alipay_dict()
            else:
                params['red_reason'] = self.red_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RedRelatedInvoiceInfo()
        if 'origin_invoice_kind' in d:
            o.origin_invoice_kind = d['origin_invoice_kind']
        if 'origin_invoice_no' in d:
            o.origin_invoice_no = d['origin_invoice_no']
        if 'red_reason' in d:
            o.red_reason = d['red_reason']
        return o


