#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHomedoctorUserinfoShareResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHomedoctorUserinfoShareResponse, self).__init__()
        self._aq_open_id = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._certify_id = None
        self._certify_state = None
        self._mobile_phone = None

    @property
    def aq_open_id(self):
        return self._aq_open_id

    @aq_open_id.setter
    def aq_open_id(self, value):
        self._aq_open_id = value
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
    def certify_id(self):
        return self._certify_id

    @certify_id.setter
    def certify_id(self, value):
        self._certify_id = value
    @property
    def certify_state(self):
        return self._certify_state

    @certify_state.setter
    def certify_state(self, value):
        self._certify_state = value
    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        self._mobile_phone = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHomedoctorUserinfoShareResponse, self).parse_response_content(response_content)
        if 'aq_open_id' in response:
            self.aq_open_id = response['aq_open_id']
        if 'cert_name' in response:
            self.cert_name = response['cert_name']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'certify_id' in response:
            self.certify_id = response['certify_id']
        if 'certify_state' in response:
            self.certify_state = response['certify_state']
        if 'mobile_phone' in response:
            self.mobile_phone = response['mobile_phone']
