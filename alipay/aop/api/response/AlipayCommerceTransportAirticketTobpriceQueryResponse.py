#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AirticketPriceQueryInfo import AirticketPriceQueryInfo


class AlipayCommerceTransportAirticketTobpriceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportAirticketTobpriceQueryResponse, self).__init__()
        self._data = None
        self._out_biz_no = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, AirticketPriceQueryInfo):
                    self._data.append(i)
                else:
                    self._data.append(AirticketPriceQueryInfo.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportAirticketTobpriceQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
