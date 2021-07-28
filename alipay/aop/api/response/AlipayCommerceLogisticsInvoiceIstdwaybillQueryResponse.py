#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WaybillInvoiceQueryIstd import WaybillInvoiceQueryIstd


class AlipayCommerceLogisticsInvoiceIstdwaybillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsInvoiceIstdwaybillQueryResponse, self).__init__()
        self._status = None
        self._waybill_invoices = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def waybill_invoices(self):
        return self._waybill_invoices

    @waybill_invoices.setter
    def waybill_invoices(self, value):
        if isinstance(value, list):
            self._waybill_invoices = list()
            for i in value:
                if isinstance(i, WaybillInvoiceQueryIstd):
                    self._waybill_invoices.append(i)
                else:
                    self._waybill_invoices.append(WaybillInvoiceQueryIstd.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsInvoiceIstdwaybillQueryResponse, self).parse_response_content(response_content)
        if 'status' in response:
            self.status = response['status']
        if 'waybill_invoices' in response:
            self.waybill_invoices = response['waybill_invoices']
