#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalCommercialShopstaffQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialShopstaffQueryResponse, self).__init__()
        self._alipay_logon_id = None
        self._role = None
        self._staff_name = None

    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def staff_name(self):
        return self._staff_name

    @staff_name.setter
    def staff_name(self, value):
        self._staff_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialShopstaffQueryResponse, self).parse_response_content(response_content)
        if 'alipay_logon_id' in response:
            self.alipay_logon_id = response['alipay_logon_id']
        if 'role' in response:
            self.role = response['role']
        if 'staff_name' in response:
            self.staff_name = response['staff_name']
