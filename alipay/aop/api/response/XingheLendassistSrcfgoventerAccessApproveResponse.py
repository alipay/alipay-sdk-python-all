#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class XingheLendassistSrcfgoventerAccessApproveResponse(AlipayResponse):

    def __init__(self):
        super(XingheLendassistSrcfgoventerAccessApproveResponse, self).__init__()
        self._apply_no = None
        self._approve_result = None
        self._refuse_reason = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def approve_result(self):
        return self._approve_result

    @approve_result.setter
    def approve_result(self, value):
        self._approve_result = value
    @property
    def refuse_reason(self):
        return self._refuse_reason

    @refuse_reason.setter
    def refuse_reason(self, value):
        self._refuse_reason = value

    def parse_response_content(self, response_content):
        response = super(XingheLendassistSrcfgoventerAccessApproveResponse, self).parse_response_content(response_content)
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'approve_result' in response:
            self.approve_result = response['approve_result']
        if 'refuse_reason' in response:
            self.refuse_reason = response['refuse_reason']
