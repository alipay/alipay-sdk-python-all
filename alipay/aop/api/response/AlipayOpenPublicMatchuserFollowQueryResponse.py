#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicMatchuserFollowQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicMatchuserFollowQueryResponse, self).__init__()
        self._is_follow = None
        self._user_id = None

    @property
    def is_follow(self):
        return self._is_follow

    @is_follow.setter
    def is_follow(self, value):
        self._is_follow = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicMatchuserFollowQueryResponse, self).parse_response_content(response_content)
        if 'is_follow' in response:
            self.is_follow = response['is_follow']
        if 'user_id' in response:
            self.user_id = response['user_id']
