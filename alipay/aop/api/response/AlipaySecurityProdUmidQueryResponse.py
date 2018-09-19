#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdUmidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdUmidQueryResponse, self).__init__()
        self._umid = None

    @property
    def umid(self):
        return self._umid

    @umid.setter
    def umid(self, value):
        self._umid = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdUmidQueryResponse, self).parse_response_content(response_content)
        if 'umid' in response:
            self.umid = response['umid']
