#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeUserRiskConsultResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeUserRiskConsultResponse, self).__init__()
        self._permit = None
        self._refuse_code = None
        self._risk_order_no = None

    @property
    def permit(self):
        return self._permit

    @permit.setter
    def permit(self, value):
        self._permit = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def risk_order_no(self):
        return self._risk_order_no

    @risk_order_no.setter
    def risk_order_no(self, value):
        self._risk_order_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeUserRiskConsultResponse, self).parse_response_content(response_content)
        if 'permit' in response:
            self.permit = response['permit']
        if 'refuse_code' in response:
            self.refuse_code = response['refuse_code']
        if 'risk_order_no' in response:
            self.risk_order_no = response['risk_order_no']
