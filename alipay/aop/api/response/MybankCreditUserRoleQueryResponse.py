#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditUserRoleQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditUserRoleQueryResponse, self).__init__()
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._ip_id = None
        self._ip_role_id = None
        self._ip_type = None
        self._site = None
        self._site_login_id = None
        self._site_user_id = None

    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def ip_type(self):
        return self._ip_type

    @ip_type.setter
    def ip_type(self, value):
        self._ip_type = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def site_login_id(self):
        return self._site_login_id

    @site_login_id.setter
    def site_login_id(self, value):
        self._site_login_id = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditUserRoleQueryResponse, self).parse_response_content(response_content)
        if 'cert_name' in response:
            self.cert_name = response['cert_name']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'ip_id' in response:
            self.ip_id = response['ip_id']
        if 'ip_role_id' in response:
            self.ip_role_id = response['ip_role_id']
        if 'ip_type' in response:
            self.ip_type = response['ip_type']
        if 'site' in response:
            self.site = response['site']
        if 'site_login_id' in response:
            self.site_login_id = response['site_login_id']
        if 'site_user_id' in response:
            self.site_user_id = response['site_user_id']
