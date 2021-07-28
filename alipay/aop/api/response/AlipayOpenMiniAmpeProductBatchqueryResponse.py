#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmpeProductInfo import AmpeProductInfo


class AlipayOpenMiniAmpeProductBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeProductBatchqueryResponse, self).__init__()
        self._product_list = None

    @property
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, value):
        if isinstance(value, list):
            self._product_list = list()
            for i in value:
                if isinstance(i, AmpeProductInfo):
                    self._product_list.append(i)
                else:
                    self._product_list.append(AmpeProductInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeProductBatchqueryResponse, self).parse_response_content(response_content)
        if 'product_list' in response:
            self.product_list = response['product_list']
