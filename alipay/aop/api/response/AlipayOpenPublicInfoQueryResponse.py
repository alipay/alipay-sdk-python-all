#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PublicAuditStatus import PublicAuditStatus


class AlipayOpenPublicInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicInfoQueryResponse, self).__init__()
        self._app_name = None
        self._audit_desc = None
        self._audit_status = None
        self._audit_status_list = None
        self._background_url = None
        self._introduction = None
        self._is_online = None
        self._is_release = None
        self._logo_url = None
        self._mcc_code_desc = None
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
    def audit_status_list(self):
        return self._audit_status_list

    @audit_status_list.setter
    def audit_status_list(self, value):
        if isinstance(value, list):
            self._audit_status_list = list()
            for i in value:
                if isinstance(i, PublicAuditStatus):
                    self._audit_status_list.append(i)
                else:
                    self._audit_status_list.append(PublicAuditStatus.from_alipay_dict(i))
    @property
    def background_url(self):
        return self._background_url

    @background_url.setter
    def background_url(self, value):
        self._background_url = value
    @property
    def introduction(self):
        return self._introduction

    @introduction.setter
    def introduction(self, value):
        self._introduction = value
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
    def mcc_code_desc(self):
        return self._mcc_code_desc

    @mcc_code_desc.setter
    def mcc_code_desc(self, value):
        self._mcc_code_desc = value
    @property
    def public_greeting(self):
        return self._public_greeting

    @public_greeting.setter
    def public_greeting(self, value):
        self._public_greeting = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicInfoQueryResponse, self).parse_response_content(response_content)
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'audit_desc' in response:
            self.audit_desc = response['audit_desc']
        if 'audit_status' in response:
            self.audit_status = response['audit_status']
        if 'audit_status_list' in response:
            self.audit_status_list = response['audit_status_list']
        if 'background_url' in response:
            self.background_url = response['background_url']
        if 'introduction' in response:
            self.introduction = response['introduction']
        if 'is_online' in response:
            self.is_online = response['is_online']
        if 'is_release' in response:
            self.is_release = response['is_release']
        if 'logo_url' in response:
            self.logo_url = response['logo_url']
        if 'mcc_code_desc' in response:
            self.mcc_code_desc = response['mcc_code_desc']
        if 'public_greeting' in response:
            self.public_greeting = response['public_greeting']
