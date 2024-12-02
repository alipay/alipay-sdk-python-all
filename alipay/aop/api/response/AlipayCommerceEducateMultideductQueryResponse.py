#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateMultideductQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateMultideductQueryResponse, self).__init__()
        self._agreement_no = None
        self._agreement_status = None
        self._asset = None
        self._open_id = None
        self._school_code = None
        self._user_id = None
        self._user_unique_id = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def agreement_status(self):
        return self._agreement_status

    @agreement_status.setter
    def agreement_status(self, value):
        self._agreement_status = value
    @property
    def asset(self):
        return self._asset

    @asset.setter
    def asset(self, value):
        self._asset = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def school_code(self):
        return self._school_code

    @school_code.setter
    def school_code(self, value):
        self._school_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_unique_id(self):
        return self._user_unique_id

    @user_unique_id.setter
    def user_unique_id(self, value):
        self._user_unique_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateMultideductQueryResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'agreement_status' in response:
            self.agreement_status = response['agreement_status']
        if 'asset' in response:
            self.asset = response['asset']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'school_code' in response:
            self.school_code = response['school_code']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_unique_id' in response:
            self.user_unique_id = response['user_unique_id']
