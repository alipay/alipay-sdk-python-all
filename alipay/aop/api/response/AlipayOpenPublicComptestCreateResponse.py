#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicComptestCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicComptestCreateResponse, self).__init__()
        self._result = None
        self._resulttwo = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def resulttwo(self):
        return self._resulttwo

    @resulttwo.setter
    def resulttwo(self, value):
        self._resulttwo = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicComptestCreateResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'resulttwo' in response:
            self.resulttwo = response['resulttwo']
