#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MinRate import MinRate
from alipay.aop.api.domain.RoomInfo import RoomInfo


class AlipayCommerceTransportHotelMinpriceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportHotelMinpriceQueryResponse, self).__init__()
        self._hotel_id = None
        self._min_rates = None
        self._room_infos = None

    @property
    def hotel_id(self):
        return self._hotel_id

    @hotel_id.setter
    def hotel_id(self, value):
        self._hotel_id = value
    @property
    def min_rates(self):
        return self._min_rates

    @min_rates.setter
    def min_rates(self, value):
        if isinstance(value, list):
            self._min_rates = list()
            for i in value:
                if isinstance(i, MinRate):
                    self._min_rates.append(i)
                else:
                    self._min_rates.append(MinRate.from_alipay_dict(i))
    @property
    def room_infos(self):
        return self._room_infos

    @room_infos.setter
    def room_infos(self, value):
        if isinstance(value, list):
            self._room_infos = list()
            for i in value:
                if isinstance(i, RoomInfo):
                    self._room_infos.append(i)
                else:
                    self._room_infos.append(RoomInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportHotelMinpriceQueryResponse, self).parse_response_content(response_content)
        if 'hotel_id' in response:
            self.hotel_id = response['hotel_id']
        if 'min_rates' in response:
            self.min_rates = response['min_rates']
        if 'room_infos' in response:
            self.room_infos = response['room_infos']
