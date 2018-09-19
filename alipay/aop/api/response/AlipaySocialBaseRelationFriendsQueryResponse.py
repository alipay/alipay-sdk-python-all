#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FriendListVO import FriendListVO


class AlipaySocialBaseRelationFriendsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseRelationFriendsQueryResponse, self).__init__()
        self._friend_list = None

    @property
    def friend_list(self):
        return self._friend_list

    @friend_list.setter
    def friend_list(self, value):
        if isinstance(value, list):
            self._friend_list = list()
            for i in value:
                if isinstance(i, FriendListVO):
                    self._friend_list.append(i)
                else:
                    self._friend_list.append(FriendListVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseRelationFriendsQueryResponse, self).parse_response_content(response_content)
        if 'friend_list' in response:
            self.friend_list = response['friend_list']
