#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayUserDeliverAddress import AlipayUserDeliverAddress
from alipay.aop.api.domain.AlipayUserPicture import AlipayUserPicture
from alipay.aop.api.domain.AlipayUserPicture import AlipayUserPicture
from alipay.aop.api.domain.AlipayUserPicture import AlipayUserPicture


class AlipayUserInfoShareResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserInfoShareResponse, self).__init__()
        self._address = None
        self._area = None
        self._avatar = None
        self._business_scope = None
        self._cert_no = None
        self._cert_type = None
        self._city = None
        self._college_name = None
        self._country_code = None
        self._degree = None
        self._deliver_addresses = None
        self._email = None
        self._enrollment_time = None
        self._firm_agent_person_cert_expiry_date = None
        self._firm_agent_person_cert_no = None
        self._firm_agent_person_cert_type = None
        self._firm_agent_person_name = None
        self._firm_legal_person_cert_expiry_date = None
        self._firm_legal_person_cert_no = None
        self._firm_legal_person_cert_type = None
        self._firm_legal_person_name = None
        self._firm_legal_person_pictures = None
        self._firm_pictures = None
        self._firm_type = None
        self._gender = None
        self._graduation_time = None
        self._is_balance_frozen = None
        self._is_certified = None
        self._is_student_certified = None
        self._license_expiry_date = None
        self._license_no = None
        self._member_grade = None
        self._mobile = None
        self._nick_name = None
        self._organization_code = None
        self._person_birthday = None
        self._person_birthday_without_year = None
        self._person_cert_expiry_date = None
        self._person_pictures = None
        self._phone = None
        self._profession = None
        self._province = None
        self._taobao_id = None
        self._user_id = None
        self._user_name = None
        self._user_status = None
        self._user_type = None
        self._zip = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def business_scope(self):
        return self._business_scope

    @business_scope.setter
    def business_scope(self, value):
        self._business_scope = value
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
    def college_name(self):
        return self._college_name

    @college_name.setter
    def college_name(self, value):
        self._college_name = value
    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        self._country_code = value
    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, value):
        self._degree = value
    @property
    def deliver_addresses(self):
        return self._deliver_addresses

    @deliver_addresses.setter
    def deliver_addresses(self, value):
        if isinstance(value, list):
            self._deliver_addresses = list()
            for i in value:
                if isinstance(i, AlipayUserDeliverAddress):
                    self._deliver_addresses.append(i)
                else:
                    self._deliver_addresses.append(AlipayUserDeliverAddress.from_alipay_dict(i))
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def enrollment_time(self):
        return self._enrollment_time

    @enrollment_time.setter
    def enrollment_time(self, value):
        self._enrollment_time = value
    @property
    def firm_agent_person_cert_expiry_date(self):
        return self._firm_agent_person_cert_expiry_date

    @firm_agent_person_cert_expiry_date.setter
    def firm_agent_person_cert_expiry_date(self, value):
        self._firm_agent_person_cert_expiry_date = value
    @property
    def firm_agent_person_cert_no(self):
        return self._firm_agent_person_cert_no

    @firm_agent_person_cert_no.setter
    def firm_agent_person_cert_no(self, value):
        self._firm_agent_person_cert_no = value
    @property
    def firm_agent_person_cert_type(self):
        return self._firm_agent_person_cert_type

    @firm_agent_person_cert_type.setter
    def firm_agent_person_cert_type(self, value):
        self._firm_agent_person_cert_type = value
    @property
    def firm_agent_person_name(self):
        return self._firm_agent_person_name

    @firm_agent_person_name.setter
    def firm_agent_person_name(self, value):
        self._firm_agent_person_name = value
    @property
    def firm_legal_person_cert_expiry_date(self):
        return self._firm_legal_person_cert_expiry_date

    @firm_legal_person_cert_expiry_date.setter
    def firm_legal_person_cert_expiry_date(self, value):
        self._firm_legal_person_cert_expiry_date = value
    @property
    def firm_legal_person_cert_no(self):
        return self._firm_legal_person_cert_no

    @firm_legal_person_cert_no.setter
    def firm_legal_person_cert_no(self, value):
        self._firm_legal_person_cert_no = value
    @property
    def firm_legal_person_cert_type(self):
        return self._firm_legal_person_cert_type

    @firm_legal_person_cert_type.setter
    def firm_legal_person_cert_type(self, value):
        self._firm_legal_person_cert_type = value
    @property
    def firm_legal_person_name(self):
        return self._firm_legal_person_name

    @firm_legal_person_name.setter
    def firm_legal_person_name(self, value):
        self._firm_legal_person_name = value
    @property
    def firm_legal_person_pictures(self):
        return self._firm_legal_person_pictures

    @firm_legal_person_pictures.setter
    def firm_legal_person_pictures(self, value):
        if isinstance(value, list):
            self._firm_legal_person_pictures = list()
            for i in value:
                if isinstance(i, AlipayUserPicture):
                    self._firm_legal_person_pictures.append(i)
                else:
                    self._firm_legal_person_pictures.append(AlipayUserPicture.from_alipay_dict(i))
    @property
    def firm_pictures(self):
        return self._firm_pictures

    @firm_pictures.setter
    def firm_pictures(self, value):
        if isinstance(value, list):
            self._firm_pictures = list()
            for i in value:
                if isinstance(i, AlipayUserPicture):
                    self._firm_pictures.append(i)
                else:
                    self._firm_pictures.append(AlipayUserPicture.from_alipay_dict(i))
    @property
    def firm_type(self):
        return self._firm_type

    @firm_type.setter
    def firm_type(self, value):
        self._firm_type = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def graduation_time(self):
        return self._graduation_time

    @graduation_time.setter
    def graduation_time(self, value):
        self._graduation_time = value
    @property
    def is_balance_frozen(self):
        return self._is_balance_frozen

    @is_balance_frozen.setter
    def is_balance_frozen(self, value):
        self._is_balance_frozen = value
    @property
    def is_certified(self):
        return self._is_certified

    @is_certified.setter
    def is_certified(self, value):
        self._is_certified = value
    @property
    def is_student_certified(self):
        return self._is_student_certified

    @is_student_certified.setter
    def is_student_certified(self, value):
        self._is_student_certified = value
    @property
    def license_expiry_date(self):
        return self._license_expiry_date

    @license_expiry_date.setter
    def license_expiry_date(self, value):
        self._license_expiry_date = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
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
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def organization_code(self):
        return self._organization_code

    @organization_code.setter
    def organization_code(self, value):
        self._organization_code = value
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
    def person_cert_expiry_date(self):
        return self._person_cert_expiry_date

    @person_cert_expiry_date.setter
    def person_cert_expiry_date(self, value):
        self._person_cert_expiry_date = value
    @property
    def person_pictures(self):
        return self._person_pictures

    @person_pictures.setter
    def person_pictures(self, value):
        if isinstance(value, list):
            self._person_pictures = list()
            for i in value:
                if isinstance(i, AlipayUserPicture):
                    self._person_pictures.append(i)
                else:
                    self._person_pictures.append(AlipayUserPicture.from_alipay_dict(i))
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, value):
        self._profession = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def taobao_id(self):
        return self._taobao_id

    @taobao_id.setter
    def taobao_id(self, value):
        self._taobao_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_status(self):
        return self._user_status

    @user_status.setter
    def user_status(self, value):
        self._user_status = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value
    @property
    def zip(self):
        return self._zip

    @zip.setter
    def zip(self, value):
        self._zip = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserInfoShareResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'area' in response:
            self.area = response['area']
        if 'avatar' in response:
            self.avatar = response['avatar']
        if 'business_scope' in response:
            self.business_scope = response['business_scope']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'city' in response:
            self.city = response['city']
        if 'college_name' in response:
            self.college_name = response['college_name']
        if 'country_code' in response:
            self.country_code = response['country_code']
        if 'degree' in response:
            self.degree = response['degree']
        if 'deliver_addresses' in response:
            self.deliver_addresses = response['deliver_addresses']
        if 'email' in response:
            self.email = response['email']
        if 'enrollment_time' in response:
            self.enrollment_time = response['enrollment_time']
        if 'firm_agent_person_cert_expiry_date' in response:
            self.firm_agent_person_cert_expiry_date = response['firm_agent_person_cert_expiry_date']
        if 'firm_agent_person_cert_no' in response:
            self.firm_agent_person_cert_no = response['firm_agent_person_cert_no']
        if 'firm_agent_person_cert_type' in response:
            self.firm_agent_person_cert_type = response['firm_agent_person_cert_type']
        if 'firm_agent_person_name' in response:
            self.firm_agent_person_name = response['firm_agent_person_name']
        if 'firm_legal_person_cert_expiry_date' in response:
            self.firm_legal_person_cert_expiry_date = response['firm_legal_person_cert_expiry_date']
        if 'firm_legal_person_cert_no' in response:
            self.firm_legal_person_cert_no = response['firm_legal_person_cert_no']
        if 'firm_legal_person_cert_type' in response:
            self.firm_legal_person_cert_type = response['firm_legal_person_cert_type']
        if 'firm_legal_person_name' in response:
            self.firm_legal_person_name = response['firm_legal_person_name']
        if 'firm_legal_person_pictures' in response:
            self.firm_legal_person_pictures = response['firm_legal_person_pictures']
        if 'firm_pictures' in response:
            self.firm_pictures = response['firm_pictures']
        if 'firm_type' in response:
            self.firm_type = response['firm_type']
        if 'gender' in response:
            self.gender = response['gender']
        if 'graduation_time' in response:
            self.graduation_time = response['graduation_time']
        if 'is_balance_frozen' in response:
            self.is_balance_frozen = response['is_balance_frozen']
        if 'is_certified' in response:
            self.is_certified = response['is_certified']
        if 'is_student_certified' in response:
            self.is_student_certified = response['is_student_certified']
        if 'license_expiry_date' in response:
            self.license_expiry_date = response['license_expiry_date']
        if 'license_no' in response:
            self.license_no = response['license_no']
        if 'member_grade' in response:
            self.member_grade = response['member_grade']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'nick_name' in response:
            self.nick_name = response['nick_name']
        if 'organization_code' in response:
            self.organization_code = response['organization_code']
        if 'person_birthday' in response:
            self.person_birthday = response['person_birthday']
        if 'person_birthday_without_year' in response:
            self.person_birthday_without_year = response['person_birthday_without_year']
        if 'person_cert_expiry_date' in response:
            self.person_cert_expiry_date = response['person_cert_expiry_date']
        if 'person_pictures' in response:
            self.person_pictures = response['person_pictures']
        if 'phone' in response:
            self.phone = response['phone']
        if 'profession' in response:
            self.profession = response['profession']
        if 'province' in response:
            self.province = response['province']
        if 'taobao_id' in response:
            self.taobao_id = response['taobao_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_name' in response:
            self.user_name = response['user_name']
        if 'user_status' in response:
            self.user_status = response['user_status']
        if 'user_type' in response:
            self.user_type = response['user_type']
        if 'zip' in response:
            self.zip = response['zip']
