#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeliverAddress import DeliverAddress


class AlipayUserUserinfoShareResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserUserinfoShareResponse, self).__init__()
        self._address = None
        self._address_code = None
        self._alipay_user_id = None
        self._area = None
        self._avatar = None
        self._balance_freeze_type = None
        self._birthday = None
        self._cert_no = None
        self._cert_type_value = None
        self._city = None
        self._default_deliver_address = None
        self._deliver_address_list = None
        self._deliver_area = None
        self._deliver_city = None
        self._deliver_fullname = None
        self._deliver_mobile = None
        self._deliver_phone = None
        self._deliver_province = None
        self._email = None
        self._family_name = None
        self._firm_name = None
        self._gender = None
        self._is_balance_frozen = None
        self._is_bank_auth = None
        self._is_certified = None
        self._is_certify_grade_a = None
        self._is_id_auth = None
        self._is_licence_auth = None
        self._is_mobile_auth = None
        self._is_student_certified = None
        self._mobile = None
        self._nick_name = None
        self._phone = None
        self._province = None
        self._real_name = None
        self._reduced_birthday = None
        self._user_id = None
        self._user_status = None
        self._user_type_value = None
        self._zip = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def address_code(self):
        return self._address_code

    @address_code.setter
    def address_code(self, value):
        self._address_code = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
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
    def balance_freeze_type(self):
        return self._balance_freeze_type

    @balance_freeze_type.setter
    def balance_freeze_type(self, value):
        self._balance_freeze_type = value
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
    def cert_type_value(self):
        return self._cert_type_value

    @cert_type_value.setter
    def cert_type_value(self, value):
        self._cert_type_value = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def default_deliver_address(self):
        return self._default_deliver_address

    @default_deliver_address.setter
    def default_deliver_address(self, value):
        self._default_deliver_address = value
    @property
    def deliver_address_list(self):
        return self._deliver_address_list

    @deliver_address_list.setter
    def deliver_address_list(self, value):
        if isinstance(value, list):
            self._deliver_address_list = list()
            for i in value:
                if isinstance(i, DeliverAddress):
                    self._deliver_address_list.append(i)
                else:
                    self._deliver_address_list.append(DeliverAddress.from_alipay_dict(i))
    @property
    def deliver_area(self):
        return self._deliver_area

    @deliver_area.setter
    def deliver_area(self, value):
        self._deliver_area = value
    @property
    def deliver_city(self):
        return self._deliver_city

    @deliver_city.setter
    def deliver_city(self, value):
        self._deliver_city = value
    @property
    def deliver_fullname(self):
        return self._deliver_fullname

    @deliver_fullname.setter
    def deliver_fullname(self, value):
        self._deliver_fullname = value
    @property
    def deliver_mobile(self):
        return self._deliver_mobile

    @deliver_mobile.setter
    def deliver_mobile(self, value):
        self._deliver_mobile = value
    @property
    def deliver_phone(self):
        return self._deliver_phone

    @deliver_phone.setter
    def deliver_phone(self, value):
        self._deliver_phone = value
    @property
    def deliver_province(self):
        return self._deliver_province

    @deliver_province.setter
    def deliver_province(self, value):
        self._deliver_province = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def family_name(self):
        return self._family_name

    @family_name.setter
    def family_name(self, value):
        self._family_name = value
    @property
    def firm_name(self):
        return self._firm_name

    @firm_name.setter
    def firm_name(self, value):
        self._firm_name = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def is_balance_frozen(self):
        return self._is_balance_frozen

    @is_balance_frozen.setter
    def is_balance_frozen(self, value):
        self._is_balance_frozen = value
    @property
    def is_bank_auth(self):
        return self._is_bank_auth

    @is_bank_auth.setter
    def is_bank_auth(self, value):
        self._is_bank_auth = value
    @property
    def is_certified(self):
        return self._is_certified

    @is_certified.setter
    def is_certified(self, value):
        self._is_certified = value
    @property
    def is_certify_grade_a(self):
        return self._is_certify_grade_a

    @is_certify_grade_a.setter
    def is_certify_grade_a(self, value):
        self._is_certify_grade_a = value
    @property
    def is_id_auth(self):
        return self._is_id_auth

    @is_id_auth.setter
    def is_id_auth(self, value):
        self._is_id_auth = value
    @property
    def is_licence_auth(self):
        return self._is_licence_auth

    @is_licence_auth.setter
    def is_licence_auth(self, value):
        self._is_licence_auth = value
    @property
    def is_mobile_auth(self):
        return self._is_mobile_auth

    @is_mobile_auth.setter
    def is_mobile_auth(self, value):
        self._is_mobile_auth = value
    @property
    def is_student_certified(self):
        return self._is_student_certified

    @is_student_certified.setter
    def is_student_certified(self, value):
        self._is_student_certified = value
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
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def reduced_birthday(self):
        return self._reduced_birthday

    @reduced_birthday.setter
    def reduced_birthday(self, value):
        self._reduced_birthday = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_status(self):
        return self._user_status

    @user_status.setter
    def user_status(self, value):
        self._user_status = value
    @property
    def user_type_value(self):
        return self._user_type_value

    @user_type_value.setter
    def user_type_value(self, value):
        self._user_type_value = value
    @property
    def zip(self):
        return self._zip

    @zip.setter
    def zip(self, value):
        self._zip = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserUserinfoShareResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'address_code' in response:
            self.address_code = response['address_code']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'area' in response:
            self.area = response['area']
        if 'avatar' in response:
            self.avatar = response['avatar']
        if 'balance_freeze_type' in response:
            self.balance_freeze_type = response['balance_freeze_type']
        if 'birthday' in response:
            self.birthday = response['birthday']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type_value' in response:
            self.cert_type_value = response['cert_type_value']
        if 'city' in response:
            self.city = response['city']
        if 'default_deliver_address' in response:
            self.default_deliver_address = response['default_deliver_address']
        if 'deliver_address_list' in response:
            self.deliver_address_list = response['deliver_address_list']
        if 'deliver_area' in response:
            self.deliver_area = response['deliver_area']
        if 'deliver_city' in response:
            self.deliver_city = response['deliver_city']
        if 'deliver_fullname' in response:
            self.deliver_fullname = response['deliver_fullname']
        if 'deliver_mobile' in response:
            self.deliver_mobile = response['deliver_mobile']
        if 'deliver_phone' in response:
            self.deliver_phone = response['deliver_phone']
        if 'deliver_province' in response:
            self.deliver_province = response['deliver_province']
        if 'email' in response:
            self.email = response['email']
        if 'family_name' in response:
            self.family_name = response['family_name']
        if 'firm_name' in response:
            self.firm_name = response['firm_name']
        if 'gender' in response:
            self.gender = response['gender']
        if 'is_balance_frozen' in response:
            self.is_balance_frozen = response['is_balance_frozen']
        if 'is_bank_auth' in response:
            self.is_bank_auth = response['is_bank_auth']
        if 'is_certified' in response:
            self.is_certified = response['is_certified']
        if 'is_certify_grade_a' in response:
            self.is_certify_grade_a = response['is_certify_grade_a']
        if 'is_id_auth' in response:
            self.is_id_auth = response['is_id_auth']
        if 'is_licence_auth' in response:
            self.is_licence_auth = response['is_licence_auth']
        if 'is_mobile_auth' in response:
            self.is_mobile_auth = response['is_mobile_auth']
        if 'is_student_certified' in response:
            self.is_student_certified = response['is_student_certified']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'nick_name' in response:
            self.nick_name = response['nick_name']
        if 'phone' in response:
            self.phone = response['phone']
        if 'province' in response:
            self.province = response['province']
        if 'real_name' in response:
            self.real_name = response['real_name']
        if 'reduced_birthday' in response:
            self.reduced_birthday = response['reduced_birthday']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_status' in response:
            self.user_status = response['user_status']
        if 'user_type_value' in response:
            self.user_type_value = response['user_type_value']
        if 'zip' in response:
            self.zip = response['zip']
