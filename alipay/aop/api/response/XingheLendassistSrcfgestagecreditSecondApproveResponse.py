#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class XingheLendassistSrcfgestagecreditSecondApproveResponse(AlipayResponse):

    def __init__(self):
        super(XingheLendassistSrcfgestagecreditSecondApproveResponse, self).__init__()
        self._approve_result = None
        self._refuse_reason = None

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
        response = super(XingheLendassistSrcfgestagecreditSecondApproveResponse, self).parse_response_content(response_content)
        if 'approve_result' in response:
            self.approve_result = response['approve_result']
        if 'refuse_reason' in response:
            self.refuse_reason = response['refuse_reason']
