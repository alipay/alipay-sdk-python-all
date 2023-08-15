#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseHttpaccessDomainGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseHttpaccessDomainGetResponse, self).__init__()
        self._cname = None
        self._force_https = None
        self._has_cert = None
        self._name = None
        self._ssl_cert = None
        self._ssl_key = None

    @property
    def cname(self):
        return self._cname

    @cname.setter
    def cname(self, value):
        self._cname = value
    @property
    def force_https(self):
        return self._force_https

    @force_https.setter
    def force_https(self, value):
        self._force_https = value
    @property
    def has_cert(self):
        return self._has_cert

    @has_cert.setter
    def has_cert(self, value):
        self._has_cert = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def ssl_cert(self):
        return self._ssl_cert

    @ssl_cert.setter
    def ssl_cert(self, value):
        self._ssl_cert = value
    @property
    def ssl_key(self):
        return self._ssl_key

    @ssl_key.setter
    def ssl_key(self, value):
        self._ssl_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseHttpaccessDomainGetResponse, self).parse_response_content(response_content)
        if 'cname' in response:
            self.cname = response['cname']
        if 'force_https' in response:
            self.force_https = response['force_https']
        if 'has_cert' in response:
            self.has_cert = response['has_cert']
        if 'name' in response:
            self.name = response['name']
        if 'ssl_cert' in response:
            self.ssl_cert = response['ssl_cert']
        if 'ssl_key' in response:
            self.ssl_key = response['ssl_key']
