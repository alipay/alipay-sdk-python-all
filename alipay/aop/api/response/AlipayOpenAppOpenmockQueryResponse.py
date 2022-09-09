#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppOpenmockQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppOpenmockQueryResponse, self).__init__()
        self._xxxsa = None

    @property
    def xxxsa(self):
        return self._xxxsa

    @xxxsa.setter
    def xxxsa(self, value):
        self._xxxsa = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppOpenmockQueryResponse, self).parse_response_content(response_content)
        if 'xxxsa' in response:
            self.xxxsa = response['xxxsa']
