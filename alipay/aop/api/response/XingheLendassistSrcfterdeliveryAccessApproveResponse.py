#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class XingheLendassistSrcfterdeliveryAccessApproveResponse(AlipayResponse):

    def __init__(self):
        super(XingheLendassistSrcfterdeliveryAccessApproveResponse, self).__init__()
        self._approve_result = None
        self._delivery_apply_no = None
        self._refuse_reason = None

    @property
    def approve_result(self):
        return self._approve_result

    @approve_result.setter
    def approve_result(self, value):
        self._approve_result = value
    @property
    def delivery_apply_no(self):
        return self._delivery_apply_no

    @delivery_apply_no.setter
    def delivery_apply_no(self, value):
        self._delivery_apply_no = value
    @property
    def refuse_reason(self):
        return self._refuse_reason

    @refuse_reason.setter
    def refuse_reason(self, value):
        self._refuse_reason = value

    def parse_response_content(self, response_content):
        response = super(XingheLendassistSrcfterdeliveryAccessApproveResponse, self).parse_response_content(response_content)
        if 'approve_result' in response:
            self.approve_result = response['approve_result']
        if 'delivery_apply_no' in response:
            self.delivery_apply_no = response['delivery_apply_no']
        if 'refuse_reason' in response:
            self.refuse_reason = response['refuse_reason']
