#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenLotteryCampModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenLotteryCampModifyResponse, self).__init__()
        self._camp_id = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenLotteryCampModifyResponse, self).parse_response_content(response_content)
        if 'camp_id' in response:
            self.camp_id = response['camp_id']
