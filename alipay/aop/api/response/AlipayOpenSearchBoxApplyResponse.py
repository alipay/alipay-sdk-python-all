#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSearchBoxApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchBoxApplyResponse, self).__init__()
        self._box_id = None

    @property
    def box_id(self):
        return self._box_id

    @box_id.setter
    def box_id(self, value):
        self._box_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchBoxApplyResponse, self).parse_response_content(response_content)
        if 'box_id' in response:
            self.box_id = response['box_id']
