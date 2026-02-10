#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLifeserviceRoomstockSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceRoomstockSyncResponse, self).__init__()
        self._room_id = None

    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceRoomstockSyncResponse, self).parse_response_content(response_content)
        if 'room_id' in response:
            self.room_id = response['room_id']
