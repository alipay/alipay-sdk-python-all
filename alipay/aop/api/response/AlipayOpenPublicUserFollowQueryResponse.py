#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicUserFollowQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicUserFollowQueryResponse, self).__init__()
        self._is_follow = None

    @property
    def is_follow(self):
        return self._is_follow

    @is_follow.setter
    def is_follow(self, value):
        self._is_follow = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicUserFollowQueryResponse, self).parse_response_content(response_content)
        if 'is_follow' in response:
            self.is_follow = response['is_follow']
