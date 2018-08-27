#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoEduJzPostPublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoEduJzPostPublishResponse, self).__init__()
        self._third_id = None

    @property
    def third_id(self):
        return self._third_id

    @third_id.setter
    def third_id(self, value):
        self._third_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoEduJzPostPublishResponse, self).parse_response_content(response_content)
        if 'third_id' in response:
            self.third_id = response['third_id']
