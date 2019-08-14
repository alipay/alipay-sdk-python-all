#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoantradeShoptransferConsultResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeShoptransferConsultResponse, self).__init__()
        self._consult_result = None
        self._refuse_code = None
        self._refuse_desc = None

    @property
    def consult_result(self):
        return self._consult_result

    @consult_result.setter
    def consult_result(self, value):
        self._consult_result = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_desc(self):
        return self._refuse_desc

    @refuse_desc.setter
    def refuse_desc(self, value):
        self._refuse_desc = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeShoptransferConsultResponse, self).parse_response_content(response_content)
        if 'consult_result' in response:
            self.consult_result = response['consult_result']
        if 'refuse_code' in response:
            self.refuse_code = response['refuse_code']
        if 'refuse_desc' in response:
            self.refuse_desc = response['refuse_desc']
