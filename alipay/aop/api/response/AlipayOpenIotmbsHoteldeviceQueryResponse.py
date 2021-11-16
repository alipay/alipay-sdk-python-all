#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotmbsHoteldeviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotmbsHoteldeviceQueryResponse, self).__init__()
        self._group_id = None
        self._hotel_name = None
        self._room_no = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def hotel_name(self):
        return self._hotel_name

    @hotel_name.setter
    def hotel_name(self, value):
        self._hotel_name = value
    @property
    def room_no(self):
        return self._room_no

    @room_no.setter
    def room_no(self, value):
        self._room_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotmbsHoteldeviceQueryResponse, self).parse_response_content(response_content)
        if 'group_id' in response:
            self.group_id = response['group_id']
        if 'hotel_name' in response:
            self.hotel_name = response['hotel_name']
        if 'room_no' in response:
            self.room_no = response['room_no']
