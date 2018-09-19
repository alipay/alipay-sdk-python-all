#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsMarketingSellerSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingSellerSignResponse, self).__init__()
        self._agreement_no = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingSellerSignResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
