#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneOrderChangeSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneOrderChangeSyncResponse, self).__init__()
        self._accept_order_id = None

    @property
    def accept_order_id(self):
        return self._accept_order_id

    @accept_order_id.setter
    def accept_order_id(self, value):
        self._accept_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneOrderChangeSyncResponse, self).parse_response_content(response_content)
        if 'accept_order_id' in response:
            self.accept_order_id = response['accept_order_id']
