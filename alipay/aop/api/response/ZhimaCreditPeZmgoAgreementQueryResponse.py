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
        self._biz_type = None
        self._open_id = None
        self._sign_time = None
        self._start_time = None

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
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'sign_time' in response:
            self.sign_time = response['sign_time']
        if 'start_time' in response:
            self.start_time = response['start_time']
