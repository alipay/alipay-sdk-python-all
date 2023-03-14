#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntSignOperatorResult(object):

    def __init__(self):
        self._auth_person_cert_name = None
        self._auth_person_cert_no = None
        self._auth_person_cert_type = None
        self._authorize_time = None
        self._authorized = None
        self._email_address = None
        self._fail_info = None
        self._mobile_number = None
        self._our_corp = None
        self._sign_cert_name = None
        self._sign_cert_no = None
        self._sign_cert_type = None
        self._sign_time = None
        self._sign_user_id = None
        self._status = None

    @property
    def auth_person_cert_name(self):
        return self._auth_person_cert_name

    @auth_person_cert_name.setter
    def auth_person_cert_name(self, value):
        self._auth_person_cert_name = value
    @property
    def auth_person_cert_no(self):
        return self._auth_person_cert_no

    @auth_person_cert_no.setter
    def auth_person_cert_no(self, value):
        self._auth_person_cert_no = value
    @property
    def auth_person_cert_type(self):
        return self._auth_person_cert_type

    @auth_person_cert_type.setter
    def auth_person_cert_type(self, value):
        self._auth_person_cert_type = value
    @property
    def authorize_time(self):
        return self._authorize_time

    @authorize_time.setter
    def authorize_time(self, value):
        self._authorize_time = value
    @property
    def authorized(self):
        return self._authorized

    @authorized.setter
    def authorized(self, value):
        self._authorized = value
    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        self._email_address = value
    @property
    def fail_info(self):
        return self._fail_info

    @fail_info.setter
    def fail_info(self, value):
        self._fail_info = value
    @property
    def mobile_number(self):
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, value):
        self._mobile_number = value
    @property
    def our_corp(self):
        return self._our_corp

    @our_corp.setter
    def our_corp(self, value):
        self._our_corp = value
    @property
    def sign_cert_name(self):
        return self._sign_cert_name

    @sign_cert_name.setter
    def sign_cert_name(self, value):
        self._sign_cert_name = value
    @property
    def sign_cert_no(self):
        return self._sign_cert_no

    @sign_cert_no.setter
    def sign_cert_no(self, value):
        self._sign_cert_no = value
    @property
    def sign_cert_type(self):
        return self._sign_cert_type

    @sign_cert_type.setter
    def sign_cert_type(self, value):
        self._sign_cert_type = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def sign_user_id(self):
        return self._sign_user_id

    @sign_user_id.setter
    def sign_user_id(self, value):
        self._sign_user_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_person_cert_name:
            if hasattr(self.auth_person_cert_name, 'to_alipay_dict'):
                params['auth_person_cert_name'] = self.auth_person_cert_name.to_alipay_dict()
            else:
                params['auth_person_cert_name'] = self.auth_person_cert_name
        if self.auth_person_cert_no:
            if hasattr(self.auth_person_cert_no, 'to_alipay_dict'):
                params['auth_person_cert_no'] = self.auth_person_cert_no.to_alipay_dict()
            else:
                params['auth_person_cert_no'] = self.auth_person_cert_no
        if self.auth_person_cert_type:
            if hasattr(self.auth_person_cert_type, 'to_alipay_dict'):
                params['auth_person_cert_type'] = self.auth_person_cert_type.to_alipay_dict()
            else:
                params['auth_person_cert_type'] = self.auth_person_cert_type
        if self.authorize_time:
            if hasattr(self.authorize_time, 'to_alipay_dict'):
                params['authorize_time'] = self.authorize_time.to_alipay_dict()
            else:
                params['authorize_time'] = self.authorize_time
        if self.authorized:
            if hasattr(self.authorized, 'to_alipay_dict'):
                params['authorized'] = self.authorized.to_alipay_dict()
            else:
                params['authorized'] = self.authorized
        if self.email_address:
            if hasattr(self.email_address, 'to_alipay_dict'):
                params['email_address'] = self.email_address.to_alipay_dict()
            else:
                params['email_address'] = self.email_address
        if self.fail_info:
            if hasattr(self.fail_info, 'to_alipay_dict'):
                params['fail_info'] = self.fail_info.to_alipay_dict()
            else:
                params['fail_info'] = self.fail_info
        if self.mobile_number:
            if hasattr(self.mobile_number, 'to_alipay_dict'):
                params['mobile_number'] = self.mobile_number.to_alipay_dict()
            else:
                params['mobile_number'] = self.mobile_number
        if self.our_corp:
            if hasattr(self.our_corp, 'to_alipay_dict'):
                params['our_corp'] = self.our_corp.to_alipay_dict()
            else:
                params['our_corp'] = self.our_corp
        if self.sign_cert_name:
            if hasattr(self.sign_cert_name, 'to_alipay_dict'):
                params['sign_cert_name'] = self.sign_cert_name.to_alipay_dict()
            else:
                params['sign_cert_name'] = self.sign_cert_name
        if self.sign_cert_no:
            if hasattr(self.sign_cert_no, 'to_alipay_dict'):
                params['sign_cert_no'] = self.sign_cert_no.to_alipay_dict()
            else:
                params['sign_cert_no'] = self.sign_cert_no
        if self.sign_cert_type:
            if hasattr(self.sign_cert_type, 'to_alipay_dict'):
                params['sign_cert_type'] = self.sign_cert_type.to_alipay_dict()
            else:
                params['sign_cert_type'] = self.sign_cert_type
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        if self.sign_user_id:
            if hasattr(self.sign_user_id, 'to_alipay_dict'):
                params['sign_user_id'] = self.sign_user_id.to_alipay_dict()
            else:
                params['sign_user_id'] = self.sign_user_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntSignOperatorResult()
        if 'auth_person_cert_name' in d:
            o.auth_person_cert_name = d['auth_person_cert_name']
        if 'auth_person_cert_no' in d:
            o.auth_person_cert_no = d['auth_person_cert_no']
        if 'auth_person_cert_type' in d:
            o.auth_person_cert_type = d['auth_person_cert_type']
        if 'authorize_time' in d:
            o.authorize_time = d['authorize_time']
        if 'authorized' in d:
            o.authorized = d['authorized']
        if 'email_address' in d:
            o.email_address = d['email_address']
        if 'fail_info' in d:
            o.fail_info = d['fail_info']
        if 'mobile_number' in d:
            o.mobile_number = d['mobile_number']
        if 'our_corp' in d:
            o.our_corp = d['our_corp']
        if 'sign_cert_name' in d:
            o.sign_cert_name = d['sign_cert_name']
        if 'sign_cert_no' in d:
            o.sign_cert_no = d['sign_cert_no']
        if 'sign_cert_type' in d:
            o.sign_cert_type = d['sign_cert_type']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'sign_user_id' in d:
            o.sign_user_id = d['sign_user_id']
        if 'status' in d:
            o.status = d['status']
        return o


