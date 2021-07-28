#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ParkingGoodsDetail import ParkingGoodsDetail


class AlipayCommerceTransportParkingGoodsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportParkingGoodsQueryResponse, self).__init__()
        self._parking_goods_detail = None

    @property
    def parking_goods_detail(self):
        return self._parking_goods_detail

    @parking_goods_detail.setter
    def parking_goods_detail(self, value):
        if isinstance(value, ParkingGoodsDetail):
            self._parking_goods_detail = value
        else:
            self._parking_goods_detail = ParkingGoodsDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportParkingGoodsQueryResponse, self).parse_response_content(response_content)
        if 'parking_goods_detail' in response:
            self.parking_goods_detail = response['parking_goods_detail']
