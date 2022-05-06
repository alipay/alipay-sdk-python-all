#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserAuthAgreement import UserAuthAgreement


class AlipayOpenAuthUserauthRelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthUserauthRelationQueryResponse, self).__init__()
        self._app_logo = None
        self._app_name = None
        self._auth_agreements = None
        self._auth_content = None
        self._auth_end = None
        self._auth_start = None

    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        self._app_logo = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def auth_agreements(self):
        return self._auth_agreements

    @auth_agreements.setter
    def auth_agreements(self, value):
        if isinstance(value, list):
            self._auth_agreements = list()
            for i in value:
                if isinstance(i, UserAuthAgreement):
                    self._auth_agreements.append(i)
                else:
                    self._auth_agreements.append(UserAuthAgreement.from_alipay_dict(i))
    @property
    def auth_content(self):
        return self._auth_content

    @auth_content.setter
    def auth_content(self, value):
        if isinstance(value, list):
            self._auth_content = list()
            for i in value:
                self._auth_content.append(i)
    @property
    def auth_end(self):
        return self._auth_end

    @auth_end.setter
    def auth_end(self, value):
        self._auth_end = value
    @property
    def auth_start(self):
        return self._auth_start

    @auth_start.setter
    def auth_start(self, value):
        self._auth_start = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthUserauthRelationQueryResponse, self).parse_response_content(response_content)
        if 'app_logo' in response:
            self.app_logo = response['app_logo']
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'auth_agreements' in response:
            self.auth_agreements = response['auth_agreements']
        if 'auth_content' in response:
            self.auth_content = response['auth_content']
        if 'auth_end' in response:
            self.auth_end = response['auth_end']
        if 'auth_start' in response:
            self.auth_start = response['auth_start']
