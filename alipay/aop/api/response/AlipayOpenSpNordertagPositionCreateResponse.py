#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNordertagPositionCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordertagPositionCreateResponse, self).__init__()
        self._tag_position_id = None

    @property
    def tag_position_id(self):
        return self._tag_position_id

    @tag_position_id.setter
    def tag_position_id(self, value):
        self._tag_position_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordertagPositionCreateResponse, self).parse_response_content(response_content)
        if 'tag_position_id' in response:
            self.tag_position_id = response['tag_position_id']
