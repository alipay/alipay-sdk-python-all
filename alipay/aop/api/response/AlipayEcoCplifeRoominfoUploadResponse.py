#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CplifeRoomInfoResp import CplifeRoomInfoResp


class AlipayEcoCplifeRoominfoUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCplifeRoominfoUploadResponse, self).__init__()
        self._community_id = None
        self._room_info_set = None

    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def room_info_set(self):
        return self._room_info_set

    @room_info_set.setter
    def room_info_set(self, value):
        if isinstance(value, list):
            self._room_info_set = list()
            for i in value:
                if isinstance(i, CplifeRoomInfoResp):
                    self._room_info_set.append(i)
                else:
                    self._room_info_set.append(CplifeRoomInfoResp.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCplifeRoominfoUploadResponse, self).parse_response_content(response_content)
        if 'community_id' in response:
            self.community_id = response['community_id']
        if 'room_info_set' in response:
            self.room_info_set = response['room_info_set']
