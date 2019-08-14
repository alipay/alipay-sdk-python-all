#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicFollowingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicFollowingQueryResponse, self).__init__()
        self._followed = None

    @property
    def followed(self):
        return self._followed

    @followed.setter
    def followed(self, value):
        self._followed = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicFollowingQueryResponse, self).parse_response_content(response_content)
        if 'followed' in response:
            self.followed = response['followed']
