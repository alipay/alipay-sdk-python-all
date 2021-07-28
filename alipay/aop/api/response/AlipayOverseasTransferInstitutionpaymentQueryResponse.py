#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTransferInstitutionpaymentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTransferInstitutionpaymentQueryResponse, self).__init__()
        self._pass_through_info = None
        self._payment_details = None

    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value
    @property
    def payment_details(self):
        return self._payment_details

    @payment_details.setter
    def payment_details(self, value):
        if isinstance(value, list):
            self._payment_details = list()
            for i in value:
                self._payment_details.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTransferInstitutionpaymentQueryResponse, self).parse_response_content(response_content)
        if 'pass_through_info' in response:
            self.pass_through_info = response['pass_through_info']
        if 'payment_details' in response:
            self.payment_details = response['payment_details']
