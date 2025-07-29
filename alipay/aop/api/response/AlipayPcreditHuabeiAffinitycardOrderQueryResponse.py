#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAffinitycardOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAffinitycardOrderQueryResponse, self).__init__()
        self._occupy_scene_amount = None

    @property
    def occupy_scene_amount(self):
        return self._occupy_scene_amount

    @occupy_scene_amount.setter
    def occupy_scene_amount(self, value):
        self._occupy_scene_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAffinitycardOrderQueryResponse, self).parse_response_content(response_content)
        if 'occupy_scene_amount' in response:
            self.occupy_scene_amount = response['occupy_scene_amount']
