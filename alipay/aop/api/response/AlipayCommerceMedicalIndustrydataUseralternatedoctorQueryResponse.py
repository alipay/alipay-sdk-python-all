#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserAlternateDoctor import UserAlternateDoctor


class AlipayCommerceMedicalIndustrydataUseralternatedoctorQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIndustrydataUseralternatedoctorQueryResponse, self).__init__()
        self._alipay_user_id = None
        self._alternate_doctor_list = None
        self._user_id_open_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def alternate_doctor_list(self):
        return self._alternate_doctor_list

    @alternate_doctor_list.setter
    def alternate_doctor_list(self, value):
        if isinstance(value, list):
            self._alternate_doctor_list = list()
            for i in value:
                if isinstance(i, UserAlternateDoctor):
                    self._alternate_doctor_list.append(i)
                else:
                    self._alternate_doctor_list.append(UserAlternateDoctor.from_alipay_dict(i))
    @property
    def user_id_open_id(self):
        return self._user_id_open_id

    @user_id_open_id.setter
    def user_id_open_id(self, value):
        self._user_id_open_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIndustrydataUseralternatedoctorQueryResponse, self).parse_response_content(response_content)
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'alternate_doctor_list' in response:
            self.alternate_doctor_list = response['alternate_doctor_list']
        if 'user_id_open_id' in response:
            self.user_id_open_id = response['user_id_open_id']
