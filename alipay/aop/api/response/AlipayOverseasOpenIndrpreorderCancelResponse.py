#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndrISVResult import IndrISVResult


class AlipayOverseasOpenIndrpreorderCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenIndrpreorderCancelResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, IndrISVResult):
            self._result = value
        else:
            self._result = IndrISVResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasOpenIndrpreorderCancelResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
