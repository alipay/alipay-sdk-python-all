#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenNppdUsertbidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenNppdUsertbidQueryResponse, self).__init__()
        self._tb_id = None

    @property
    def tb_id(self):
        return self._tb_id

    @tb_id.setter
    def tb_id(self, value):
        self._tb_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenNppdUsertbidQueryResponse, self).parse_response_content(response_content)
        if 'tb_id' in response:
            self.tb_id = response['tb_id']
