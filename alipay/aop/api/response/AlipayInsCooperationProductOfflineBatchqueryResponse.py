#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsOffilneProduct import InsOffilneProduct


class AlipayInsCooperationProductOfflineBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsCooperationProductOfflineBatchqueryResponse, self).__init__()
        self._product_list = None

    @property
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, value):
        if isinstance(value, list):
            self._product_list = list()
            for i in value:
                if isinstance(i, InsOffilneProduct):
                    self._product_list.append(i)
                else:
                    self._product_list.append(InsOffilneProduct.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsCooperationProductOfflineBatchqueryResponse, self).parse_response_content(response_content)
        if 'product_list' in response:
            self.product_list = response['product_list']
