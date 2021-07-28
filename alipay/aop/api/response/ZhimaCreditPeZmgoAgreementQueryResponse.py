#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeZmgoAgreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeZmgoAgreementQueryResponse, self).__init__()
        self._agreement_id = None
        self._agreement_name = None
        self._agreement_status = None
        self._alipay_user_id = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def agreement_name(self):
        return self._agreement_name

    @agreement_name.setter
    def agreement_name(self, value):
        self._agreement_name = value
    @property
    def agreement_status(self):
        return self._agreement_status

    @agreement_status.setter
    def agreement_status(self, value):
        self._agreement_status = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeZmgoAgreementQueryResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'agreement_name' in response:
            self.agreement_name = response['agreement_name']
        if 'agreement_status' in response:
            self.agreement_status = response['agreement_status']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
