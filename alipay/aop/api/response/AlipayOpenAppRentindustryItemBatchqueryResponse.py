#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantSpuQueryResult import MerchantSpuQueryResult


class AlipayOpenAppRentindustryItemBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppRentindustryItemBatchqueryResponse, self).__init__()
        self._data = None
        self._size = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, MerchantSpuQueryResult):
                    self._data.append(i)
                else:
                    self._data.append(MerchantSpuQueryResult.from_alipay_dict(i))
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppRentindustryItemBatchqueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'size' in response:
            self.size = response['size']
