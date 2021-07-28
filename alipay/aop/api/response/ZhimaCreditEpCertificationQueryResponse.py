#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpCertificationQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCertificationQueryResponse, self).__init__()
        self._attorney_letter = None
        self._auth_status = None
        self._business_license = None
        self._certify_status = None
        self._ep_cert_no = None
        self._ep_name = None
        self._legal_person_id_card_back = None
        self._legal_person_id_card_front = None
        self._user_name = None

    @property
    def attorney_letter(self):
        return self._attorney_letter

    @attorney_letter.setter
    def attorney_letter(self, value):
        self._attorney_letter = value
    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def business_license(self):
        return self._business_license

    @business_license.setter
    def business_license(self, value):
        self._business_license = value
    @property
    def certify_status(self):
        return self._certify_status

    @certify_status.setter
    def certify_status(self, value):
        self._certify_status = value
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
    def legal_person_id_card_back(self):
        return self._legal_person_id_card_back

    @legal_person_id_card_back.setter
    def legal_person_id_card_back(self, value):
        self._legal_person_id_card_back = value
    @property
    def legal_person_id_card_front(self):
        return self._legal_person_id_card_front

    @legal_person_id_card_front.setter
    def legal_person_id_card_front(self, value):
        self._legal_person_id_card_front = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCertificationQueryResponse, self).parse_response_content(response_content)
        if 'attorney_letter' in response:
            self.attorney_letter = response['attorney_letter']
        if 'auth_status' in response:
            self.auth_status = response['auth_status']
        if 'business_license' in response:
            self.business_license = response['business_license']
        if 'certify_status' in response:
            self.certify_status = response['certify_status']
        if 'ep_cert_no' in response:
            self.ep_cert_no = response['ep_cert_no']
        if 'ep_name' in response:
            self.ep_name = response['ep_name']
        if 'legal_person_id_card_back' in response:
            self.legal_person_id_card_back = response['legal_person_id_card_back']
        if 'legal_person_id_card_front' in response:
            self.legal_person_id_card_front = response['legal_person_id_card_front']
        if 'user_name' in response:
            self.user_name = response['user_name']
