#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsurancePerson import InsurancePerson
from alipay.aop.api.domain.InsurancePeriod import InsurancePeriod
from alipay.aop.api.domain.InsurancePerson import InsurancePerson
from alipay.aop.api.domain.MobileDeviceInfo import MobileDeviceInfo


class AlipayInsSceneMobileCodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneMobileCodeQueryResponse, self).__init__()
        self._applicant = None
        self._insurance_period = None
        self._insured = None
        self._mobile_device_info = None
        self._policy_no = None
        self._premium = None
        self._repair_type = None
        self._status = None

    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        if isinstance(value, InsurancePerson):
            self._applicant = value
        else:
            self._applicant = InsurancePerson.from_alipay_dict(value)
    @property
    def insurance_period(self):
        return self._insurance_period

    @insurance_period.setter
    def insurance_period(self, value):
        if isinstance(value, InsurancePeriod):
            self._insurance_period = value
        else:
            self._insurance_period = InsurancePeriod.from_alipay_dict(value)
    @property
    def insured(self):
        return self._insured

    @insured.setter
    def insured(self, value):
        if isinstance(value, InsurancePerson):
            self._insured = value
        else:
            self._insured = InsurancePerson.from_alipay_dict(value)
    @property
    def mobile_device_info(self):
        return self._mobile_device_info

    @mobile_device_info.setter
    def mobile_device_info(self, value):
        if isinstance(value, MobileDeviceInfo):
            self._mobile_device_info = value
        else:
            self._mobile_device_info = MobileDeviceInfo.from_alipay_dict(value)
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def repair_type(self):
        return self._repair_type

    @repair_type.setter
    def repair_type(self, value):
        self._repair_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneMobileCodeQueryResponse, self).parse_response_content(response_content)
        if 'applicant' in response:
            self.applicant = response['applicant']
        if 'insurance_period' in response:
            self.insurance_period = response['insurance_period']
        if 'insured' in response:
            self.insured = response['insured']
        if 'mobile_device_info' in response:
            self.mobile_device_info = response['mobile_device_info']
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
        if 'premium' in response:
            self.premium = response['premium']
        if 'repair_type' in response:
            self.repair_type = response['repair_type']
        if 'status' in response:
            self.status = response['status']
