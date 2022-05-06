#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundIdentitypayMemberQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundIdentitypayMemberQueryResponse, self).__init__()
        self._authentication_type = None
        self._business_params = None
        self._member_name = None
        self._status = None

    @property
    def authentication_type(self):
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, value):
        self._authentication_type = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        self._business_params = value
    @property
    def member_name(self):
        return self._member_name

    @member_name.setter
    def member_name(self, value):
        self._member_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundIdentitypayMemberQueryResponse, self).parse_response_content(response_content)
        if 'authentication_type' in response:
            self.authentication_type = response['authentication_type']
        if 'business_params' in response:
            self.business_params = response['business_params']
        if 'member_name' in response:
            self.member_name = response['member_name']
        if 'status' in response:
            self.status = response['status']
