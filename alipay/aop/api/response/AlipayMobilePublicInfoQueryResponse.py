#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicInfoQueryResponse, self).__init__()
        self._app_name = None
        self._audit_desc = None
        self._audit_status = None
        self._is_online = None
        self._is_release = None
        self._logo_url = None
        self._public_greeting = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def audit_desc(self):
        return self._audit_desc

    @audit_desc.setter
    def audit_desc(self, value):
        self._audit_desc = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def is_online(self):
        return self._is_online

    @is_online.setter
    def is_online(self, value):
        self._is_online = value
    @property
    def is_release(self):
        return self._is_release

    @is_release.setter
    def is_release(self, value):
        self._is_release = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def public_greeting(self):
        return self._public_greeting

    @public_greeting.setter
    def public_greeting(self, value):
        self._public_greeting = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicInfoQueryResponse, self).parse_response_content(response_content)
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'audit_desc' in response:
            self.audit_desc = response['audit_desc']
        if 'audit_status' in response:
            self.audit_status = response['audit_status']
        if 'is_online' in response:
            self.is_online = response['is_online']
        if 'is_release' in response:
            self.is_release = response['is_release']
        if 'logo_url' in response:
            self.logo_url = response['logo_url']
        if 'public_greeting' in response:
            self.public_greeting = response['public_greeting']
