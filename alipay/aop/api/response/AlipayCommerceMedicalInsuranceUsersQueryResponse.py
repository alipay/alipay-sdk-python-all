#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsuranceUserInformation import InsuranceUserInformation


class AlipayCommerceMedicalInsuranceUsersQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceUsersQueryResponse, self).__init__()
        self._insurance_user_models = None
        self._signed = None
        self._user_token = None

    @property
    def insurance_user_models(self):
        return self._insurance_user_models

    @insurance_user_models.setter
    def insurance_user_models(self, value):
        if isinstance(value, list):
            self._insurance_user_models = list()
            for i in value:
                if isinstance(i, InsuranceUserInformation):
                    self._insurance_user_models.append(i)
                else:
                    self._insurance_user_models.append(InsuranceUserInformation.from_alipay_dict(i))
    @property
    def signed(self):
        return self._signed

    @signed.setter
    def signed(self, value):
        self._signed = value
    @property
    def user_token(self):
        return self._user_token

    @user_token.setter
    def user_token(self, value):
        self._user_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceUsersQueryResponse, self).parse_response_content(response_content)
        if 'insurance_user_models' in response:
            self.insurance_user_models = response['insurance_user_models']
        if 'signed' in response:
            self.signed = response['signed']
        if 'user_token' in response:
            self.user_token = response['user_token']
