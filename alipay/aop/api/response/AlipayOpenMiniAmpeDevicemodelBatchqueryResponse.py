#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmpeProductInfo import AmpeProductInfo


class AlipayOpenMiniAmpeDevicemodelBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeDevicemodelBatchqueryResponse, self).__init__()
        self._product_info = None

    @property
    def product_info(self):
        return self._product_info

    @product_info.setter
    def product_info(self, value):
        if isinstance(value, AmpeProductInfo):
            self._product_info = value
        else:
            self._product_info = AmpeProductInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeDevicemodelBatchqueryResponse, self).parse_response_content(response_content)
        if 'product_info' in response:
            self.product_info = response['product_info']
