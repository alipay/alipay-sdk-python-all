#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoanapplyElmCreditloanadmitQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyElmCreditloanadmitQueryResponse, self).__init__()
        self._admit_label = None

    @property
    def admit_label(self):
        return self._admit_label

    @admit_label.setter
    def admit_label(self, value):
        self._admit_label = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyElmCreditloanadmitQueryResponse, self).parse_response_content(response_content)
        if 'admit_label' in response:
            self.admit_label = response['admit_label']
