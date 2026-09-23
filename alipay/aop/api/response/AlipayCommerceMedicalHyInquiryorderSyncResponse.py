#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHyInquiryorderSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHyInquiryorderSyncResponse, self).__init__()
        self._refund_request_no = None

    @property
    def refund_request_no(self):
        return self._refund_request_no

    @refund_request_no.setter
    def refund_request_no(self, value):
        self._refund_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHyInquiryorderSyncResponse, self).parse_response_content(response_content)
        if 'refund_request_no' in response:
            self.refund_request_no = response['refund_request_no']
