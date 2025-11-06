#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneClaimOverdueApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneClaimOverdueApplyResponse, self).__init__()
        self._overdue_no = None

    @property
    def overdue_no(self):
        return self._overdue_no

    @overdue_no.setter
    def overdue_no(self, value):
        self._overdue_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneClaimOverdueApplyResponse, self).parse_response_content(response_content)
        if 'overdue_no' in response:
            self.overdue_no = response['overdue_no']
