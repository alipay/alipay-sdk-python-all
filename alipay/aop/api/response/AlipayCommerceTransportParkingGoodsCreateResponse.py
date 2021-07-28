#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportParkingGoodsCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportParkingGoodsCreateResponse, self).__init__()
        self._goods_id = None
        self._out_id = None

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportParkingGoodsCreateResponse, self).parse_response_content(response_content)
        if 'goods_id' in response:
            self.goods_id = response['goods_id']
        if 'out_id' in response:
            self.out_id = response['out_id']
