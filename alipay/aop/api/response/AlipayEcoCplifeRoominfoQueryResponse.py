#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CplifeRoomDetail import CplifeRoomDetail


class AlipayEcoCplifeRoominfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCplifeRoominfoQueryResponse, self).__init__()
        self._room_info = None
        self._total_room_number = None

    @property
    def room_info(self):
        return self._room_info

    @room_info.setter
    def room_info(self, value):
        if isinstance(value, list):
            self._room_info = list()
            for i in value:
                if isinstance(i, CplifeRoomDetail):
                    self._room_info.append(i)
                else:
                    self._room_info.append(CplifeRoomDetail.from_alipay_dict(i))
    @property
    def total_room_number(self):
        return self._total_room_number

    @total_room_number.setter
    def total_room_number(self, value):
        self._total_room_number = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCplifeRoominfoQueryResponse, self).parse_response_content(response_content)
        if 'room_info' in response:
            self.room_info = response['room_info']
        if 'total_room_number' in response:
            self.total_room_number = response['total_room_number']
