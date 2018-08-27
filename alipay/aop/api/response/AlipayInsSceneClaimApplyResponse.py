#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneClaimApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneClaimApplyResponse, self).__init__()
        self._claim_report_no = None
        self._out_biz_no = None
        self._out_request_no = None

    @property
    def claim_report_no(self):
        return self._claim_report_no

    @claim_report_no.setter
    def claim_report_no(self, value):
        self._claim_report_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneClaimApplyResponse, self).parse_response_content(response_content)
        if 'claim_report_no' in response:
            self.claim_report_no = response['claim_report_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
