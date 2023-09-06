#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InputInvoiceRegisterResponse import InputInvoiceRegisterResponse


class AlipayBossFncInputinvoiceRegisterCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncInputinvoiceRegisterCreateResponse, self).__init__()
        self._result_set = None

    @property
    def result_set(self):
        return self._result_set

    @result_set.setter
    def result_set(self, value):
        if isinstance(value, InputInvoiceRegisterResponse):
            self._result_set = value
        else:
            self._result_set = InputInvoiceRegisterResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncInputinvoiceRegisterCreateResponse, self).parse_response_content(response_content)
        if 'result_set' in response:
            self.result_set = response['result_set']
