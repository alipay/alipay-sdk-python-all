#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditCreditriskDsddAdmitConsultResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditCreditriskDsddAdmitConsultResponse, self).__init__()
        self._amt_grade = None
        self._status = None

    @property
    def amt_grade(self):
        return self._amt_grade

    @amt_grade.setter
    def amt_grade(self, value):
        self._amt_grade = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditCreditriskDsddAdmitConsultResponse, self).parse_response_content(response_content)
        if 'amt_grade' in response:
            self.amt_grade = response['amt_grade']
        if 'status' in response:
            self.status = response['status']
