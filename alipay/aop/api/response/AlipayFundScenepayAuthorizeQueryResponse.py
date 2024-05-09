#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundScenepayAuthorizeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundScenepayAuthorizeQueryResponse, self).__init__()
        self._authorization_id = None
        self._authorize_manage_url = None
        self._authorize_platform = None
        self._out_agreement_no = None
        self._status = None

    @property
    def authorization_id(self):
        return self._authorization_id

    @authorization_id.setter
    def authorization_id(self, value):
        self._authorization_id = value
    @property
    def authorize_manage_url(self):
        return self._authorize_manage_url

    @authorize_manage_url.setter
    def authorize_manage_url(self, value):
        self._authorize_manage_url = value
    @property
    def authorize_platform(self):
        return self._authorize_platform

    @authorize_platform.setter
    def authorize_platform(self, value):
        self._authorize_platform = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundScenepayAuthorizeQueryResponse, self).parse_response_content(response_content)
        if 'authorization_id' in response:
            self.authorization_id = response['authorization_id']
        if 'authorize_manage_url' in response:
            self.authorize_manage_url = response['authorize_manage_url']
        if 'authorize_platform' in response:
            self.authorize_platform = response['authorize_platform']
        if 'out_agreement_no' in response:
            self.out_agreement_no = response['out_agreement_no']
        if 'status' in response:
            self.status = response['status']
