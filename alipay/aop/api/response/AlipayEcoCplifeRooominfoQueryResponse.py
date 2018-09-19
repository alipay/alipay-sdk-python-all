#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CplifeRoomDetail import CplifeRoomDetail


class AlipayEcoCplifeRooominfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCplifeRooominfoQueryResponse, self).__init__()
        self._room_info = None

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

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCplifeRooominfoQueryResponse, self).parse_response_content(response_content)
        if 'room_info' in response:
            self.room_info = response['room_info']
