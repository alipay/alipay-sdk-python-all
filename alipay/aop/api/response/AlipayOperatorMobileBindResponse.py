#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOperatorMobileBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOperatorMobileBindResponse, self).__init__()
        self._alipay_user_id = None
        self._certificate = None
        self._mobile_no = None
        self._status = None
        self._user_name = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def certificate(self):
        return self._certificate

    @certificate.setter
    def certificate(self, value):
        self._certificate = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOperatorMobileBindResponse, self).parse_response_content(response_content)
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'certificate' in response:
            self.certificate = response['certificate']
        if 'mobile_no' in response:
            self.mobile_no = response['mobile_no']
        if 'status' in response:
            self.status = response['status']
        if 'user_name' in response:
            self.user_name = response['user_name']
