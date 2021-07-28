#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserElectronicidUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserElectronicidUserQueryResponse, self).__init__()
        self._address = None
        self._birthday = None
        self._cert_no = None
        self._cert_picture = None
        self._gender = None
        self._name = None
        self._nation = None
        self._picture = None
        self._secret_key = None
        self._sign_org = None
        self._valid_begin_date = None
        self._valid_end_date = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
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
    def cert_picture(self):
        return self._cert_picture

    @cert_picture.setter
    def cert_picture(self, value):
        self._cert_picture = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nation(self):
        return self._nation

    @nation.setter
    def nation(self, value):
        self._nation = value
    @property
    def picture(self):
        return self._picture

    @picture.setter
    def picture(self, value):
        self._picture = value
    @property
    def secret_key(self):
        return self._secret_key

    @secret_key.setter
    def secret_key(self, value):
        self._secret_key = value
    @property
    def sign_org(self):
        return self._sign_org

    @sign_org.setter
    def sign_org(self, value):
        self._sign_org = value
    @property
    def valid_begin_date(self):
        return self._valid_begin_date

    @valid_begin_date.setter
    def valid_begin_date(self, value):
        self._valid_begin_date = value
    @property
    def valid_end_date(self):
        return self._valid_end_date

    @valid_end_date.setter
    def valid_end_date(self, value):
        self._valid_end_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserElectronicidUserQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'birthday' in response:
            self.birthday = response['birthday']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_picture' in response:
            self.cert_picture = response['cert_picture']
        if 'gender' in response:
            self.gender = response['gender']
        if 'name' in response:
            self.name = response['name']
        if 'nation' in response:
            self.nation = response['nation']
        if 'picture' in response:
            self.picture = response['picture']
        if 'secret_key' in response:
            self.secret_key = response['secret_key']
        if 'sign_org' in response:
            self.sign_org = response['sign_org']
        if 'valid_begin_date' in response:
            self.valid_begin_date = response['valid_begin_date']
        if 'valid_end_date' in response:
            self.valid_end_date = response['valid_end_date']
