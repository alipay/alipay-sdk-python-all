#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPayafteruseCreditagreementSignResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPayafteruseCreditagreementSignResponse, self).__init__()
        self._credit_agreement_id = None
        self._out_agreement_no = None

    @property
    def credit_agreement_id(self):
        return self._credit_agreement_id

    @credit_agreement_id.setter
    def credit_agreement_id(self, value):
        self._credit_agreement_id = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPayafteruseCreditagreementSignResponse, self).parse_response_content(response_content)
        if 'credit_agreement_id' in response:
            self.credit_agreement_id = response['credit_agreement_id']
        if 'out_agreement_no' in response:
            self.out_agreement_no = response['out_agreement_no']
