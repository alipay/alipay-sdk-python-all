#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpSceneAgreementCancelResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpSceneAgreementCancelResponse, self).__init__()
        self._credit_order_no = None

    @property
    def credit_order_no(self):
        return self._credit_order_no

    @credit_order_no.setter
    def credit_order_no(self, value):
        self._credit_order_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpSceneAgreementCancelResponse, self).parse_response_content(response_content)
        if 'credit_order_no' in response:
            self.credit_order_no = response['credit_order_no']
