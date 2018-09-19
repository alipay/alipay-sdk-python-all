#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountFinriskInstriskmonitorKeywordsBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountFinriskInstriskmonitorKeywordsBatchqueryResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                self._result.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayAccountFinriskInstriskmonitorKeywordsBatchqueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
