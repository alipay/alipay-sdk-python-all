#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiProformaInvoiceAddOrder import OpenApiProformaInvoiceAddOrder


class AlipayBossFncGfinvoiceOutputproformanobillApplyModel(object):

    def __init__(self):
        self._proforma_invoice_add_order = None

    @property
    def proforma_invoice_add_order(self):
        return self._proforma_invoice_add_order

    @proforma_invoice_add_order.setter
    def proforma_invoice_add_order(self, value):
        if isinstance(value, OpenApiProformaInvoiceAddOrder):
            self._proforma_invoice_add_order = value
        else:
            self._proforma_invoice_add_order = OpenApiProformaInvoiceAddOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.proforma_invoice_add_order:
            if hasattr(self.proforma_invoice_add_order, 'to_alipay_dict'):
                params['proforma_invoice_add_order'] = self.proforma_invoice_add_order.to_alipay_dict()
            else:
                params['proforma_invoice_add_order'] = self.proforma_invoice_add_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfinvoiceOutputproformanobillApplyModel()
        if 'proforma_invoice_add_order' in d:
            o.proforma_invoice_add_order = d['proforma_invoice_add_order']
        return o


