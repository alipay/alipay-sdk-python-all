#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsStationCooperationModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsStationCooperationModifyResponse, self).__init__()
        self._event_type = None
        self._station_brand_id = None
        self._station_shop_id = None

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def station_brand_id(self):
        return self._station_brand_id

    @station_brand_id.setter
    def station_brand_id(self, value):
        self._station_brand_id = value
    @property
    def station_shop_id(self):
        return self._station_shop_id

    @station_shop_id.setter
    def station_shop_id(self, value):
        self._station_shop_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsStationCooperationModifyResponse, self).parse_response_content(response_content)
        if 'event_type' in response:
            self.event_type = response['event_type']
        if 'station_brand_id' in response:
            self.station_brand_id = response['station_brand_id']
        if 'station_shop_id' in response:
            self.station_shop_id = response['station_shop_id']
