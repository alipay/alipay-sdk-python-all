#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityRoomCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityRoomCreateResponse, self).__init__()
        self._community_room_url = None
        self._room_id = None

    @property
    def community_room_url(self):
        return self._community_room_url

    @community_room_url.setter
    def community_room_url(self, value):
        self._community_room_url = value
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityRoomCreateResponse, self).parse_response_content(response_content)
        if 'community_room_url' in response:
            self.community_room_url = response['community_room_url']
        if 'room_id' in response:
            self.room_id = response['room_id']
