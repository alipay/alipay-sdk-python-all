#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne


class AlipayOpenDesCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenDesCreateResponse, self).__init__()
        self._ces = None

    @property
    def ces(self):
        return self._ces

    @ces.setter
    def ces(self, value):
        if isinstance(value, GavintestNewLeveaOne):
            self._ces = value
        else:
            self._ces = GavintestNewLeveaOne.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenDesCreateResponse, self).parse_response_content(response_content)
        if 'ces' in response:
            self.ces = response['ces']
