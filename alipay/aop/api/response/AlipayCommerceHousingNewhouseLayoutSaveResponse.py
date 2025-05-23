#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHousingNewhouseLayoutSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHousingNewhouseLayoutSaveResponse, self).__init__()
        self._layout_id = None

    @property
    def layout_id(self):
        return self._layout_id

    @layout_id.setter
    def layout_id(self, value):
        self._layout_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHousingNewhouseLayoutSaveResponse, self).parse_response_content(response_content)
        if 'layout_id' in response:
            self.layout_id = response['layout_id']
