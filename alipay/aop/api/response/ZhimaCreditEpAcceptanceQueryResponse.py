#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpAcceptanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAcceptanceQueryResponse, self).__init__()
        self._acceptance_status = None
        self._ep_cert_no = None
        self._ep_name = None
        self._legal_person_cert_no = None
        self._legal_person_name = None
        self._tel_phone = None
        self._user_id = None

    @property
    def acceptance_status(self):
        return self._acceptance_status

    @acceptance_status.setter
    def acceptance_status(self, value):
        self._acceptance_status = value
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
    def tel_phone(self):
        return self._tel_phone

    @tel_phone.setter
    def tel_phone(self, value):
        self._tel_phone = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAcceptanceQueryResponse, self).parse_response_content(response_content)
        if 'acceptance_status' in response:
            self.acceptance_status = response['acceptance_status']
        if 'ep_cert_no' in response:
            self.ep_cert_no = response['ep_cert_no']
        if 'ep_name' in response:
            self.ep_name = response['ep_name']
        if 'legal_person_cert_no' in response:
            self.legal_person_cert_no = response['legal_person_cert_no']
        if 'legal_person_name' in response:
            self.legal_person_name = response['legal_person_name']
        if 'tel_phone' in response:
            self.tel_phone = response['tel_phone']
        if 'user_id' in response:
            self.user_id = response['user_id']
