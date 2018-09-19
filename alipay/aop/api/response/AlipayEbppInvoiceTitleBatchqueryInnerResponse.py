#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceTitleModel import InvoiceTitleModel


class AlipayEbppInvoiceTitleBatchqueryInnerResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceTitleBatchqueryInnerResponse, self).__init__()
        self._title_list = None

    @property
    def title_list(self):
        return self._title_list

    @title_list.setter
    def title_list(self, value):
        if isinstance(value, list):
            self._title_list = list()
            for i in value:
                if isinstance(i, InvoiceTitleModel):
                    self._title_list.append(i)
                else:
                    self._title_list.append(InvoiceTitleModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceTitleBatchqueryInnerResponse, self).parse_response_content(response_content)
        if 'title_list' in response:
            self.title_list = response['title_list']
