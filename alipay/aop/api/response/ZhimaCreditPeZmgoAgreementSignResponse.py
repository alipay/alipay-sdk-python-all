#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeZmgoAgreementSignResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeZmgoAgreementSignResponse, self).__init__()
        self._agreement_id = None
        self._biz_type = None
        self._exp_invalid_time = None
        self._out_request_no = None
        self._partner_id = None
        self._sign_time = None
        self._start_time = None
        self._template_id = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def exp_invalid_time(self):
        return self._exp_invalid_time

    @exp_invalid_time.setter
    def exp_invalid_time(self, value):
        self._exp_invalid_time = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeZmgoAgreementSignResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'exp_invalid_time' in response:
            self.exp_invalid_time = response['exp_invalid_time']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'sign_time' in response:
            self.sign_time = response['sign_time']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'template_id' in response:
            self.template_id = response['template_id']
