#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccessProduceOrder import AccessProduceOrder


class KoubeiSalesKbassetStuffProduceorderBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiSalesKbassetStuffProduceorderBatchqueryResponse, self).__init__()
        self._has_next_page = None
        self._list = None

    @property
    def has_next_page(self):
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, value):
        self._has_next_page = value
    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, AccessProduceOrder):
                    self._list.append(i)
                else:
                    self._list.append(AccessProduceOrder.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiSalesKbassetStuffProduceorderBatchqueryResponse, self).parse_response_content(response_content)
        if 'has_next_page' in response:
            self.has_next_page = response['has_next_page']
        if 'list' in response:
            self.list = response['list']
