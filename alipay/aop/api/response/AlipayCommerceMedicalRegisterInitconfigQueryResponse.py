#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HisMemberCardConfDTO import HisMemberCardConfDTO
from alipay.aop.api.domain.HisPayConfDTO import HisPayConfDTO
from alipay.aop.api.domain.RegisterPatientConfDTO import RegisterPatientConfDTO


class AlipayCommerceMedicalRegisterInitconfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterInitconfigQueryResponse, self).__init__()
        self._his_member_card_conf = None
        self._his_pay_conf = None
        self._isv_source_name = None
        self._page_h_5_switch = None
        self._register_patient_conf = None
        self._register_patient_scene_code = None

    @property
    def his_member_card_conf(self):
        return self._his_member_card_conf

    @his_member_card_conf.setter
    def his_member_card_conf(self, value):
        if isinstance(value, HisMemberCardConfDTO):
            self._his_member_card_conf = value
        else:
            self._his_member_card_conf = HisMemberCardConfDTO.from_alipay_dict(value)
    @property
    def his_pay_conf(self):
        return self._his_pay_conf

    @his_pay_conf.setter
    def his_pay_conf(self, value):
        if isinstance(value, HisPayConfDTO):
            self._his_pay_conf = value
        else:
            self._his_pay_conf = HisPayConfDTO.from_alipay_dict(value)
    @property
    def isv_source_name(self):
        return self._isv_source_name

    @isv_source_name.setter
    def isv_source_name(self, value):
        self._isv_source_name = value
    @property
    def page_h_5_switch(self):
        return self._page_h_5_switch

    @page_h_5_switch.setter
    def page_h_5_switch(self, value):
        self._page_h_5_switch = value
    @property
    def register_patient_conf(self):
        return self._register_patient_conf

    @register_patient_conf.setter
    def register_patient_conf(self, value):
        if isinstance(value, RegisterPatientConfDTO):
            self._register_patient_conf = value
        else:
            self._register_patient_conf = RegisterPatientConfDTO.from_alipay_dict(value)
    @property
    def register_patient_scene_code(self):
        return self._register_patient_scene_code

    @register_patient_scene_code.setter
    def register_patient_scene_code(self, value):
        self._register_patient_scene_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterInitconfigQueryResponse, self).parse_response_content(response_content)
        if 'his_member_card_conf' in response:
            self.his_member_card_conf = response['his_member_card_conf']
        if 'his_pay_conf' in response:
            self.his_pay_conf = response['his_pay_conf']
        if 'isv_source_name' in response:
            self.isv_source_name = response['isv_source_name']
        if 'page_h_5_switch' in response:
            self.page_h_5_switch = response['page_h_5_switch']
        if 'register_patient_conf' in response:
            self.register_patient_conf = response['register_patient_conf']
        if 'register_patient_scene_code' in response:
            self.register_patient_scene_code = response['register_patient_scene_code']
