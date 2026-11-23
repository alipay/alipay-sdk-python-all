#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftBlessGoodwillSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftBlessGoodwillSubmitResponse, self).__init__()
        self._actual_issue_value = None

    @property
    def actual_issue_value(self):
        return self._actual_issue_value

    @actual_issue_value.setter
    def actual_issue_value(self, value):
        self._actual_issue_value = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftBlessGoodwillSubmitResponse, self).parse_response_content(response_content)
        if 'actual_issue_value' in response:
            self.actual_issue_value = response['actual_issue_value']
