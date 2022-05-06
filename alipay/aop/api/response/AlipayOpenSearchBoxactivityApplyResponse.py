#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSearchBoxactivityApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchBoxactivityApplyResponse, self).__init__()
        self._box_activity_id = None

    @property
    def box_activity_id(self):
        return self._box_activity_id

    @box_activity_id.setter
    def box_activity_id(self, value):
        self._box_activity_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchBoxactivityApplyResponse, self).parse_response_content(response_content)
        if 'box_activity_id' in response:
            self.box_activity_id = response['box_activity_id']
