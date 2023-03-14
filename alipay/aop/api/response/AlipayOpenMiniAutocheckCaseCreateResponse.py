#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniAutocheckCaseCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAutocheckCaseCreateResponse, self).__init__()
        self._case_id = None

    @property
    def case_id(self):
        return self._case_id

    @case_id.setter
    def case_id(self, value):
        self._case_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAutocheckCaseCreateResponse, self).parse_response_content(response_content)
        if 'case_id' in response:
            self.case_id = response['case_id']
