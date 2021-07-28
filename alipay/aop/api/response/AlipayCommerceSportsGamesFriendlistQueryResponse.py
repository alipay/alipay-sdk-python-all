#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FriendVO import FriendVO


class AlipayCommerceSportsGamesFriendlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSportsGamesFriendlistQueryResponse, self).__init__()
        self._friend_list = None
        self._self_open_id = None

    @property
    def friend_list(self):
        return self._friend_list

    @friend_list.setter
    def friend_list(self, value):
        if isinstance(value, list):
            self._friend_list = list()
            for i in value:
                if isinstance(i, FriendVO):
                    self._friend_list.append(i)
                else:
                    self._friend_list.append(FriendVO.from_alipay_dict(i))
    @property
    def self_open_id(self):
        return self._self_open_id

    @self_open_id.setter
    def self_open_id(self, value):
        self._self_open_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSportsGamesFriendlistQueryResponse, self).parse_response_content(response_content)
        if 'friend_list' in response:
            self.friend_list = response['friend_list']
        if 'self_open_id' in response:
            self.self_open_id = response['self_open_id']
