#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceTitleModel import InvoiceTitleModel


class AlipayEbppInvoiceTitleDynamicGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceTitleDynamicGetResponse, self).__init__()
        self._title = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, InvoiceTitleModel):
            self._title = value
        else:
            self._title = InvoiceTitleModel.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceTitleDynamicGetResponse, self).parse_response_content(response_content)
        if 'title' in response:
            self.title = response['title']
