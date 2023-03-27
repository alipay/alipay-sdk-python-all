#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntLinkeAlcollectioncenterCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntLinkeAlcollectioncenterCreateResponse, self).__init__()
        self._affair_id = None

    @property
    def affair_id(self):
        return self._affair_id

    @affair_id.setter
    def affair_id(self, value):
        self._affair_id = value

    def parse_response_content(self, response_content):
        response = super(AntLinkeAlcollectioncenterCreateResponse, self).parse_response_content(response_content)
        if 'affair_id' in response:
            self.affair_id = response['affair_id']
