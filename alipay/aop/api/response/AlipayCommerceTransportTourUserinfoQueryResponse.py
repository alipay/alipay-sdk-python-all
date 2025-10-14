#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTourUserinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTourUserinfoQueryResponse, self).__init__()
        self._cert_no = None
        self._cert_type = None
        self._identity_check_result = None
        self._name = None
        self._tele_no = None

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
    def identity_check_result(self):
        return self._identity_check_result

    @identity_check_result.setter
    def identity_check_result(self, value):
        self._identity_check_result = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def tele_no(self):
        return self._tele_no

    @tele_no.setter
    def tele_no(self, value):
        self._tele_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTourUserinfoQueryResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'identity_check_result' in response:
            self.identity_check_result = response['identity_check_result']
        if 'name' in response:
            self.name = response['name']
        if 'tele_no' in response:
            self.tele_no = response['tele_no']
