#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpCertificationQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCertificationQueryResponse, self).__init__()
        self._attorney_face_time = None
        self._attorney_letter = None
        self._auth_status = None
        self._business_license = None
        self._certify_channel = None
        self._certify_end_date = None
        self._certify_fail_reasons = None
        self._certify_mode = None
        self._certify_person_card_no_postfix = None
        self._certify_status = None
        self._email_address = None
        self._ep_cert_no = None
        self._ep_name = None
        self._has_li_xin_certificate = None
        self._legal_person_cert_no = None
        self._legal_person_face_time = None
        self._legal_person_id_card_back = None
        self._legal_person_id_card_front = None
        self._legal_person_name = None
        self._li_xin_ep = None
        self._user_name = None

    @property
    def attorney_face_time(self):
        return self._attorney_face_time

    @attorney_face_time.setter
    def attorney_face_time(self, value):
        self._attorney_face_time = value
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
    def certify_channel(self):
        return self._certify_channel

    @certify_channel.setter
    def certify_channel(self, value):
        self._certify_channel = value
    @property
    def certify_end_date(self):
        return self._certify_end_date

    @certify_end_date.setter
    def certify_end_date(self, value):
        self._certify_end_date = value
    @property
    def certify_fail_reasons(self):
        return self._certify_fail_reasons

    @certify_fail_reasons.setter
    def certify_fail_reasons(self, value):
        if isinstance(value, list):
            self._certify_fail_reasons = list()
            for i in value:
                self._certify_fail_reasons.append(i)
    @property
    def certify_mode(self):
        return self._certify_mode

    @certify_mode.setter
    def certify_mode(self, value):
        self._certify_mode = value
    @property
    def certify_person_card_no_postfix(self):
        return self._certify_person_card_no_postfix

    @certify_person_card_no_postfix.setter
    def certify_person_card_no_postfix(self, value):
        self._certify_person_card_no_postfix = value
    @property
    def certify_status(self):
        return self._certify_status

    @certify_status.setter
    def certify_status(self, value):
        self._certify_status = value
    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        self._email_address = value
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
    def has_li_xin_certificate(self):
        return self._has_li_xin_certificate

    @has_li_xin_certificate.setter
    def has_li_xin_certificate(self, value):
        self._has_li_xin_certificate = value
    @property
    def legal_person_cert_no(self):
        return self._legal_person_cert_no

    @legal_person_cert_no.setter
    def legal_person_cert_no(self, value):
        self._legal_person_cert_no = value
    @property
    def legal_person_face_time(self):
        return self._legal_person_face_time

    @legal_person_face_time.setter
    def legal_person_face_time(self, value):
        self._legal_person_face_time = value
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
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def li_xin_ep(self):
        return self._li_xin_ep

    @li_xin_ep.setter
    def li_xin_ep(self, value):
        self._li_xin_ep = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCertificationQueryResponse, self).parse_response_content(response_content)
        if 'attorney_face_time' in response:
            self.attorney_face_time = response['attorney_face_time']
        if 'attorney_letter' in response:
            self.attorney_letter = response['attorney_letter']
        if 'auth_status' in response:
            self.auth_status = response['auth_status']
        if 'business_license' in response:
            self.business_license = response['business_license']
        if 'certify_channel' in response:
            self.certify_channel = response['certify_channel']
        if 'certify_end_date' in response:
            self.certify_end_date = response['certify_end_date']
        if 'certify_fail_reasons' in response:
            self.certify_fail_reasons = response['certify_fail_reasons']
        if 'certify_mode' in response:
            self.certify_mode = response['certify_mode']
        if 'certify_person_card_no_postfix' in response:
            self.certify_person_card_no_postfix = response['certify_person_card_no_postfix']
        if 'certify_status' in response:
            self.certify_status = response['certify_status']
        if 'email_address' in response:
            self.email_address = response['email_address']
        if 'ep_cert_no' in response:
            self.ep_cert_no = response['ep_cert_no']
        if 'ep_name' in response:
            self.ep_name = response['ep_name']
        if 'has_li_xin_certificate' in response:
            self.has_li_xin_certificate = response['has_li_xin_certificate']
        if 'legal_person_cert_no' in response:
            self.legal_person_cert_no = response['legal_person_cert_no']
        if 'legal_person_face_time' in response:
            self.legal_person_face_time = response['legal_person_face_time']
        if 'legal_person_id_card_back' in response:
            self.legal_person_id_card_back = response['legal_person_id_card_back']
        if 'legal_person_id_card_front' in response:
            self.legal_person_id_card_front = response['legal_person_id_card_front']
        if 'legal_person_name' in response:
            self.legal_person_name = response['legal_person_name']
        if 'li_xin_ep' in response:
            self.li_xin_ep = response['li_xin_ep']
        if 'user_name' in response:
            self.user_name = response['user_name']
