#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtHrhealthKdysPersoninfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtHrhealthKdysPersoninfoQueryResponse, self).__init__()
        self._birthday = None
        self._cert_no = None
        self._cert_type = None
        self._mobile = None
        self._name = None
        self._person_type = None
        self._sex = None
        self._union_id = None
        self._user_id = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
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
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def person_type(self):
        return self._person_type

    @person_type.setter
    def person_type(self, value):
        self._person_type = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def union_id(self):
        return self._union_id

    @union_id.setter
    def union_id(self, value):
        self._union_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtHrhealthKdysPersoninfoQueryResponse, self).parse_response_content(response_content)
        if 'birthday' in response:
            self.birthday = response['birthday']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'name' in response:
            self.name = response['name']
        if 'person_type' in response:
            self.person_type = response['person_type']
        if 'sex' in response:
            self.sex = response['sex']
        if 'union_id' in response:
            self.union_id = response['union_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
