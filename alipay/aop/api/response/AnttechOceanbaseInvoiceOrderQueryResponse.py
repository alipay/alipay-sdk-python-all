#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ObcInvoiceResult import ObcInvoiceResult


class AnttechOceanbaseInvoiceOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseInvoiceOrderQueryResponse, self).__init__()
        self._id = None
        self._invoices = None
        self._memo = None
        self._status = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def invoices(self):
        return self._invoices

    @invoices.setter
    def invoices(self, value):
        if isinstance(value, list):
            self._invoices = list()
            for i in value:
                if isinstance(i, ObcInvoiceResult):
                    self._invoices.append(i)
                else:
                    self._invoices.append(ObcInvoiceResult.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseInvoiceOrderQueryResponse, self).parse_response_content(response_content)
        if 'id' in response:
            self.id = response['id']
        if 'invoices' in response:
            self.invoices = response['invoices']
        if 'memo' in response:
            self.memo = response['memo']
        if 'status' in response:
            self.status = response['status']
