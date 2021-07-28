#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceTruspleCompanycreditinquirySubmitResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceTruspleCompanycreditinquirySubmitResponse, self).__init__()
        self._result_status = None

    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceTruspleCompanycreditinquirySubmitResponse, self).parse_response_content(response_content)
        if 'result_status' in response:
            self.result_status = response['result_status']
