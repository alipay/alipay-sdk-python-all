#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInsuranceTpaeventSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceTpaeventSyncResponse, self).__init__()
        self._cert_no = None
        self._cert_type = None
        self._insured_cert_no = None
        self._insured_cert_type = None
        self._insured_name = None
        self._name = None
        self._policy_no = None

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
    def insured_cert_no(self):
        return self._insured_cert_no

    @insured_cert_no.setter
    def insured_cert_no(self, value):
        self._insured_cert_no = value
    @property
    def insured_cert_type(self):
        return self._insured_cert_type

    @insured_cert_type.setter
    def insured_cert_type(self, value):
        self._insured_cert_type = value
    @property
    def insured_name(self):
        return self._insured_name

    @insured_name.setter
    def insured_name(self, value):
        self._insured_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceTpaeventSyncResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'insured_cert_no' in response:
            self.insured_cert_no = response['insured_cert_no']
        if 'insured_cert_type' in response:
            self.insured_cert_type = response['insured_cert_type']
        if 'insured_name' in response:
            self.insured_name = response['insured_name']
        if 'name' in response:
            self.name = response['name']
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
