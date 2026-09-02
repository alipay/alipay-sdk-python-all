#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDapplyOrdersimpleinfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDapplyOrdersimpleinfoBatchqueryResponse, self).__init__()
        self._order_biz_ids = None

    @property
    def order_biz_ids(self):
        return self._order_biz_ids

    @order_biz_ids.setter
    def order_biz_ids(self, value):
        if isinstance(value, list):
            self._order_biz_ids = list()
            for i in value:
                self._order_biz_ids.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDapplyOrdersimpleinfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'order_biz_ids' in response:
            self.order_biz_ids = response['order_biz_ids']
