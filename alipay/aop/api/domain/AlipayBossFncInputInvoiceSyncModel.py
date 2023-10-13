#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SyncInvoiceOpenApiOrder import SyncInvoiceOpenApiOrder


class AlipayBossFncInputInvoiceSyncModel(object):

    def __init__(self):
        self._sync_invoice_open_api_order = None

    @property
    def sync_invoice_open_api_order(self):
        return self._sync_invoice_open_api_order

    @sync_invoice_open_api_order.setter
    def sync_invoice_open_api_order(self, value):
        if isinstance(value, SyncInvoiceOpenApiOrder):
            self._sync_invoice_open_api_order = value
        else:
            self._sync_invoice_open_api_order = SyncInvoiceOpenApiOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.sync_invoice_open_api_order:
            if hasattr(self.sync_invoice_open_api_order, 'to_alipay_dict'):
                params['sync_invoice_open_api_order'] = self.sync_invoice_open_api_order.to_alipay_dict()
            else:
                params['sync_invoice_open_api_order'] = self.sync_invoice_open_api_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInputInvoiceSyncModel()
        if 'sync_invoice_open_api_order' in d:
            o.sync_invoice_open_api_order = d['sync_invoice_open_api_order']
        return o


