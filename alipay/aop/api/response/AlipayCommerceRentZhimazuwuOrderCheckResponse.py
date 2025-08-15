#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentZhimazuwuOrderCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentZhimazuwuOrderCheckResponse, self).__init__()
        self._free_to_send_scene = None

    @property
    def free_to_send_scene(self):
        return self._free_to_send_scene

    @free_to_send_scene.setter
    def free_to_send_scene(self, value):
        self._free_to_send_scene = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentZhimazuwuOrderCheckResponse, self).parse_response_content(response_content)
        if 'free_to_send_scene' in response:
            self.free_to_send_scene = response['free_to_send_scene']
