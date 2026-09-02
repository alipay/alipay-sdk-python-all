#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenContentUsereventcontentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenContentUsereventcontentQueryResponse, self).__init__()
        self._biz_code = None
        self._biz_message = None
        self._point_supplies_data = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_message(self):
        return self._biz_message

    @biz_message.setter
    def biz_message(self, value):
        self._biz_message = value
    @property
    def point_supplies_data(self):
        return self._point_supplies_data

    @point_supplies_data.setter
    def point_supplies_data(self, value):
        self._point_supplies_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenContentUsereventcontentQueryResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_message' in response:
            self.biz_message = response['biz_message']
        if 'point_supplies_data' in response:
            self.point_supplies_data = response['point_supplies_data']
