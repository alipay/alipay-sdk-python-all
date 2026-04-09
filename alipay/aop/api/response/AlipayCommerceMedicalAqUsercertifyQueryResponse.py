#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalAqUsercertifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAqUsercertifyQueryResponse, self).__init__()
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._certify_state = None
        self._mobile = None

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
    def certify_state(self):
        return self._certify_state

    @certify_state.setter
    def certify_state(self, value):
        self._certify_state = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAqUsercertifyQueryResponse, self).parse_response_content(response_content)
        if 'cert_name' in response:
            self.cert_name = response['cert_name']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'certify_state' in response:
            self.certify_state = response['certify_state']
        if 'mobile' in response:
            self.mobile = response['mobile']
