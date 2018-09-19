#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarParkingAgreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingAgreementQueryResponse, self).__init__()
        self._agreement_status = None

    @property
    def agreement_status(self):
        return self._agreement_status

    @agreement_status.setter
    def agreement_status(self, value):
        self._agreement_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingAgreementQueryResponse, self).parse_response_content(response_content)
        if 'agreement_status' in response:
            self.agreement_status = response['agreement_status']
