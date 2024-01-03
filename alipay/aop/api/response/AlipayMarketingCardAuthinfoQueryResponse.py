#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCardAuthinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCardAuthinfoQueryResponse, self).__init__()
        self._address = None
        self._cert_no = None
        self._cert_type = None
        self._city = None
        self._email = None
        self._gender = None
        self._is_student_certified = None
        self._member_grade = None
        self._mobile = None
        self._person_birthday = None
        self._person_birthday_without_year = None
        self._user_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
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
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def is_student_certified(self):
        return self._is_student_certified

    @is_student_certified.setter
    def is_student_certified(self, value):
        self._is_student_certified = value
    @property
    def member_grade(self):
        return self._member_grade

    @member_grade.setter
    def member_grade(self, value):
        self._member_grade = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def person_birthday(self):
        return self._person_birthday

    @person_birthday.setter
    def person_birthday(self, value):
        self._person_birthday = value
    @property
    def person_birthday_without_year(self):
        return self._person_birthday_without_year

    @person_birthday_without_year.setter
    def person_birthday_without_year(self, value):
        self._person_birthday_without_year = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCardAuthinfoQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'city' in response:
            self.city = response['city']
        if 'email' in response:
            self.email = response['email']
        if 'gender' in response:
            self.gender = response['gender']
        if 'is_student_certified' in response:
            self.is_student_certified = response['is_student_certified']
        if 'member_grade' in response:
            self.member_grade = response['member_grade']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'person_birthday' in response:
            self.person_birthday = response['person_birthday']
        if 'person_birthday_without_year' in response:
            self.person_birthday_without_year = response['person_birthday_without_year']
        if 'user_name' in response:
            self.user_name = response['user_name']
