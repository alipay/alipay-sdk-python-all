#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeZmgoAgreementUnsignResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeZmgoAgreementUnsignResponse, self).__init__()
        self._agreement_id = None
        self._withhold_plan_no = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def withhold_plan_no(self):
        return self._withhold_plan_no

    @withhold_plan_no.setter
    def withhold_plan_no(self, value):
        self._withhold_plan_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeZmgoAgreementUnsignResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'withhold_plan_no' in response:
            self.withhold_plan_no = response['withhold_plan_no']
