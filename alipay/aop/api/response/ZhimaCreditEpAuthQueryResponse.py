#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpAuthQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAuthQueryResponse, self).__init__()
        self._ep_cert_no = None
        self._ep_name = None
        self._legal_person_cert_no = None
        self._legal_person_name = None
        self._phone_no = None

    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def legal_person_cert_no(self):
        return self._legal_person_cert_no

    @legal_person_cert_no.setter
    def legal_person_cert_no(self, value):
        self._legal_person_cert_no = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAuthQueryResponse, self).parse_response_content(response_content)
        if 'ep_cert_no' in response:
            self.ep_cert_no = response['ep_cert_no']
        if 'ep_name' in response:
            self.ep_name = response['ep_name']
        if 'legal_person_cert_no' in response:
            self.legal_person_cert_no = response['legal_person_cert_no']
        if 'legal_person_name' in response:
            self.legal_person_name = response['legal_person_name']
        if 'phone_no' in response:
            self.phone_no = response['phone_no']
