#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPayafteruseCreditagreementTransferResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPayafteruseCreditagreementTransferResponse, self).__init__()
        self._credit_agreement_id = None
        self._deduct_agreement_no = None
        self._out_agreement_no = None

    @property
    def credit_agreement_id(self):
        return self._credit_agreement_id

    @credit_agreement_id.setter
    def credit_agreement_id(self, value):
        self._credit_agreement_id = value
    @property
    def deduct_agreement_no(self):
        return self._deduct_agreement_no

    @deduct_agreement_no.setter
    def deduct_agreement_no(self, value):
        self._deduct_agreement_no = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPayafteruseCreditagreementTransferResponse, self).parse_response_content(response_content)
        if 'credit_agreement_id' in response:
            self.credit_agreement_id = response['credit_agreement_id']
        if 'deduct_agreement_no' in response:
            self.deduct_agreement_no = response['deduct_agreement_no']
        if 'out_agreement_no' in response:
            self.out_agreement_no = response['out_agreement_no']
