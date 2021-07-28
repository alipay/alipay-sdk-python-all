#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BFActivityOpenApiResult import BFActivityOpenApiResult


class AlipayPcreditHuabeiPcbenefitcoreBfactivitfacadeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiPcbenefitcoreBfactivitfacadeQueryResponse, self).__init__()
        self._error_context = None
        self._result = None
        self._success = None

    @property
    def error_context(self):
        return self._error_context

    @error_context.setter
    def error_context(self, value):
        if isinstance(value, list):
            self._error_context = list()
            for i in value:
                self._error_context.append(i)
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, BFActivityOpenApiResult):
            self._result = value
        else:
            self._result = BFActivityOpenApiResult.from_alipay_dict(value)
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiPcbenefitcoreBfactivitfacadeQueryResponse, self).parse_response_content(response_content)
        if 'error_context' in response:
            self.error_context = response['error_context']
        if 'result' in response:
            self.result = response['result']
        if 'success' in response:
            self.success = response['success']
