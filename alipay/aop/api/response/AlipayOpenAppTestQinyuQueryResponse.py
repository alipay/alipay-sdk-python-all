#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppTestQinyuQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppTestQinyuQueryResponse, self).__init__()
        self._oid = None

    @property
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, value):
        self._oid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppTestQinyuQueryResponse, self).parse_response_content(response_content)
        if 'oid' in response:
            self.oid = response['oid']
