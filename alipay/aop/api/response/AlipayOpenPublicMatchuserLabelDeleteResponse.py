#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ErrorMatcher import ErrorMatcher


class AlipayOpenPublicMatchuserLabelDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicMatchuserLabelDeleteResponse, self).__init__()
        self._error_count = None
        self._error_matchers = None

    @property
    def error_count(self):
        return self._error_count

    @error_count.setter
    def error_count(self, value):
        self._error_count = value
    @property
    def error_matchers(self):
        return self._error_matchers

    @error_matchers.setter
    def error_matchers(self, value):
        if isinstance(value, list):
            self._error_matchers = list()
            for i in value:
                if isinstance(i, ErrorMatcher):
                    self._error_matchers.append(i)
                else:
                    self._error_matchers.append(ErrorMatcher.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicMatchuserLabelDeleteResponse, self).parse_response_content(response_content)
        if 'error_count' in response:
            self.error_count = response['error_count']
        if 'error_matchers' in response:
            self.error_matchers = response['error_matchers']
