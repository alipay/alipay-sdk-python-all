#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyIdentifyinfoInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyIdentifyinfoInfoQueryResponse, self).__init__()
        self._org_address = None
        self._org_cert_name = None
        self._org_cert_no = None
        self._org_cert_type = None
        self._org_expire_date = None
        self._org_legal_cert_name = None
        self._org_legal_cert_no = None
        self._org_legal_cert_type = None
        self._org_legal_expire_date = None
        self._org_legal_pictures = None
        self._org_pictures = None
        self._person_cert_name = None
        self._person_cert_no = None
        self._person_cert_type = None
        self._person_expire_date = None
        self._person_pictures = None
        self._user_id = None
        self._user_type = None

    @property
    def org_address(self):
        return self._org_address

    @org_address.setter
    def org_address(self, value):
        self._org_address = value
    @property
    def org_cert_name(self):
        return self._org_cert_name

    @org_cert_name.setter
    def org_cert_name(self, value):
        self._org_cert_name = value
    @property
    def org_cert_no(self):
        return self._org_cert_no

    @org_cert_no.setter
    def org_cert_no(self, value):
        self._org_cert_no = value
    @property
    def org_cert_type(self):
        return self._org_cert_type

    @org_cert_type.setter
    def org_cert_type(self, value):
        self._org_cert_type = value
    @property
    def org_expire_date(self):
        return self._org_expire_date

    @org_expire_date.setter
    def org_expire_date(self, value):
        self._org_expire_date = value
    @property
    def org_legal_cert_name(self):
        return self._org_legal_cert_name

    @org_legal_cert_name.setter
    def org_legal_cert_name(self, value):
        self._org_legal_cert_name = value
    @property
    def org_legal_cert_no(self):
        return self._org_legal_cert_no

    @org_legal_cert_no.setter
    def org_legal_cert_no(self, value):
        self._org_legal_cert_no = value
    @property
    def org_legal_cert_type(self):
        return self._org_legal_cert_type

    @org_legal_cert_type.setter
    def org_legal_cert_type(self, value):
        self._org_legal_cert_type = value
    @property
    def org_legal_expire_date(self):
        return self._org_legal_expire_date

    @org_legal_expire_date.setter
    def org_legal_expire_date(self, value):
        self._org_legal_expire_date = value
    @property
    def org_legal_pictures(self):
        return self._org_legal_pictures

    @org_legal_pictures.setter
    def org_legal_pictures(self, value):
        if isinstance(value, list):
            self._org_legal_pictures = list()
            for i in value:
                self._org_legal_pictures.append(i)
    @property
    def org_pictures(self):
        return self._org_pictures

    @org_pictures.setter
    def org_pictures(self, value):
        if isinstance(value, list):
            self._org_pictures = list()
            for i in value:
                self._org_pictures.append(i)
    @property
    def person_cert_name(self):
        return self._person_cert_name

    @person_cert_name.setter
    def person_cert_name(self, value):
        self._person_cert_name = value
    @property
    def person_cert_no(self):
        return self._person_cert_no

    @person_cert_no.setter
    def person_cert_no(self, value):
        self._person_cert_no = value
    @property
    def person_cert_type(self):
        return self._person_cert_type

    @person_cert_type.setter
    def person_cert_type(self, value):
        self._person_cert_type = value
    @property
    def person_expire_date(self):
        return self._person_expire_date

    @person_expire_date.setter
    def person_expire_date(self, value):
        self._person_expire_date = value
    @property
    def person_pictures(self):
        return self._person_pictures

    @person_pictures.setter
    def person_pictures(self, value):
        if isinstance(value, list):
            self._person_pictures = list()
            for i in value:
                self._person_pictures.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyIdentifyinfoInfoQueryResponse, self).parse_response_content(response_content)
        if 'org_address' in response:
            self.org_address = response['org_address']
        if 'org_cert_name' in response:
            self.org_cert_name = response['org_cert_name']
        if 'org_cert_no' in response:
            self.org_cert_no = response['org_cert_no']
        if 'org_cert_type' in response:
            self.org_cert_type = response['org_cert_type']
        if 'org_expire_date' in response:
            self.org_expire_date = response['org_expire_date']
        if 'org_legal_cert_name' in response:
            self.org_legal_cert_name = response['org_legal_cert_name']
        if 'org_legal_cert_no' in response:
            self.org_legal_cert_no = response['org_legal_cert_no']
        if 'org_legal_cert_type' in response:
            self.org_legal_cert_type = response['org_legal_cert_type']
        if 'org_legal_expire_date' in response:
            self.org_legal_expire_date = response['org_legal_expire_date']
        if 'org_legal_pictures' in response:
            self.org_legal_pictures = response['org_legal_pictures']
        if 'org_pictures' in response:
            self.org_pictures = response['org_pictures']
        if 'person_cert_name' in response:
            self.person_cert_name = response['person_cert_name']
        if 'person_cert_no' in response:
            self.person_cert_no = response['person_cert_no']
        if 'person_cert_type' in response:
            self.person_cert_type = response['person_cert_type']
        if 'person_expire_date' in response:
            self.person_expire_date = response['person_expire_date']
        if 'person_pictures' in response:
            self.person_pictures = response['person_pictures']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_type' in response:
            self.user_type = response['user_type']
