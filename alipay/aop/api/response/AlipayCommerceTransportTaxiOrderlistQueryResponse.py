#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaxiOrder import TaxiOrder


class AlipayCommerceTransportTaxiOrderlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiOrderlistQueryResponse, self).__init__()
        self._taxi_order = None

    @property
    def taxi_order(self):
        return self._taxi_order

    @taxi_order.setter
    def taxi_order(self, value):
        if isinstance(value, list):
            self._taxi_order = list()
            for i in value:
                if isinstance(i, TaxiOrder):
                    self._taxi_order.append(i)
                else:
                    self._taxi_order.append(TaxiOrder.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiOrderlistQueryResponse, self).parse_response_content(response_content)
        if 'taxi_order' in response:
            self.taxi_order = response['taxi_order']
