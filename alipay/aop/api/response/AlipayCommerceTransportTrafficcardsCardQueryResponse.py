#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TrafficCardInfo import TrafficCardInfo
from alipay.aop.api.domain.TrafficCardInfo import TrafficCardInfo


class AlipayCommerceTransportTrafficcardsCardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTrafficcardsCardQueryResponse, self).__init__()
        self._bus_card_list = None
        self._bus_scene_desc = None
        self._has_valid_card = None
        self._metro_card_list = None
        self._metro_scene_desc = None

    @property
    def bus_card_list(self):
        return self._bus_card_list

    @bus_card_list.setter
    def bus_card_list(self, value):
        if isinstance(value, list):
            self._bus_card_list = list()
            for i in value:
                if isinstance(i, TrafficCardInfo):
                    self._bus_card_list.append(i)
                else:
                    self._bus_card_list.append(TrafficCardInfo.from_alipay_dict(i))
    @property
    def bus_scene_desc(self):
        return self._bus_scene_desc

    @bus_scene_desc.setter
    def bus_scene_desc(self, value):
        self._bus_scene_desc = value
    @property
    def has_valid_card(self):
        return self._has_valid_card

    @has_valid_card.setter
    def has_valid_card(self, value):
        self._has_valid_card = value
    @property
    def metro_card_list(self):
        return self._metro_card_list

    @metro_card_list.setter
    def metro_card_list(self, value):
        if isinstance(value, list):
            self._metro_card_list = list()
            for i in value:
                if isinstance(i, TrafficCardInfo):
                    self._metro_card_list.append(i)
                else:
                    self._metro_card_list.append(TrafficCardInfo.from_alipay_dict(i))
    @property
    def metro_scene_desc(self):
        return self._metro_scene_desc

    @metro_scene_desc.setter
    def metro_scene_desc(self, value):
        self._metro_scene_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTrafficcardsCardQueryResponse, self).parse_response_content(response_content)
        if 'bus_card_list' in response:
            self.bus_card_list = response['bus_card_list']
        if 'bus_scene_desc' in response:
            self.bus_scene_desc = response['bus_scene_desc']
        if 'has_valid_card' in response:
            self.has_valid_card = response['has_valid_card']
        if 'metro_card_list' in response:
            self.metro_card_list = response['metro_card_list']
        if 'metro_scene_desc' in response:
            self.metro_scene_desc = response['metro_scene_desc']
