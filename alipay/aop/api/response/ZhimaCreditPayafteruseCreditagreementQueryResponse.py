#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPayafteruseCreditagreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPayafteruseCreditagreementQueryResponse, self).__init__()
        self._agreement_status = None
        self._biz_time = None
        self._credit_agreement_id = None
        self._out_agreement_no = None

    @property
    def agreement_status(self):
        return self._agreement_status

    @agreement_status.setter
    def agreement_status(self, value):
        self._agreement_status = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
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
        response = super(ZhimaCreditPayafteruseCreditagreementQueryResponse, self).parse_response_content(response_content)
        if 'agreement_status' in response:
            self.agreement_status = response['agreement_status']
        if 'biz_time' in response:
            self.biz_time = response['biz_time']
        if 'credit_agreement_id' in response:
            self.credit_agreement_id = response['credit_agreement_id']
        if 'out_agreement_no' in response:
            self.out_agreement_no = response['out_agreement_no']
