#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneClaimNewreportCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneClaimNewreportCreateResponse, self).__init__()
        self._claim_report_no = None

    @property
    def claim_report_no(self):
        return self._claim_report_no

    @claim_report_no.setter
    def claim_report_no(self, value):
        self._claim_report_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneClaimNewreportCreateResponse, self).parse_response_content(response_content)
        if 'claim_report_no' in response:
            self.claim_report_no = response['claim_report_no']
