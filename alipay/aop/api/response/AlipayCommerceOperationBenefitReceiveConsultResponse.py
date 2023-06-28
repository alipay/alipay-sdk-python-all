#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationBenefitReceiveConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationBenefitReceiveConsultResponse, self).__init__()
        self._result = None
        self._result_desc = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationBenefitReceiveConsultResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
