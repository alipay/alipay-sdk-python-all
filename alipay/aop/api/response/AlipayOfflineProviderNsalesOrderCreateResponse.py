#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderNsalesOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderNsalesOrderCreateResponse, self).__init__()
        self._express_timeout = None
        self._order_url = None
        self._sales_entry_order_id = None

    @property
    def express_timeout(self):
        return self._express_timeout

    @express_timeout.setter
    def express_timeout(self, value):
        self._express_timeout = value
    @property
    def order_url(self):
        return self._order_url

    @order_url.setter
    def order_url(self, value):
        self._order_url = value
    @property
    def sales_entry_order_id(self):
        return self._sales_entry_order_id

    @sales_entry_order_id.setter
    def sales_entry_order_id(self, value):
        self._sales_entry_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderNsalesOrderCreateResponse, self).parse_response_content(response_content)
        if 'express_timeout' in response:
            self.express_timeout = response['express_timeout']
        if 'order_url' in response:
            self.order_url = response['order_url']
        if 'sales_entry_order_id' in response:
            self.sales_entry_order_id = response['sales_entry_order_id']
