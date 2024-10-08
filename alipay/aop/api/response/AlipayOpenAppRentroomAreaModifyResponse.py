#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppRentroomAreaModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppRentroomAreaModifyResponse, self).__init__()
        self._area_id = None
        self._out_area_id = None

    @property
    def area_id(self):
        return self._area_id

    @area_id.setter
    def area_id(self, value):
        self._area_id = value
    @property
    def out_area_id(self):
        return self._out_area_id

    @out_area_id.setter
    def out_area_id(self, value):
        self._out_area_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppRentroomAreaModifyResponse, self).parse_response_content(response_content)
        if 'area_id' in response:
            self.area_id = response['area_id']
        if 'out_area_id' in response:
            self.out_area_id = response['out_area_id']
