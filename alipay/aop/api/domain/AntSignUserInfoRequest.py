#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CaSystemSignFileRequest import CaSystemSignFileRequest


class AntSignUserInfoRequest(object):

    def __init__(self):
        self._auth_signer_cert_number = None
        self._auth_signer_cert_type = None
        self._auth_signer_name = None
        self._authorized = None
        self._auto_sign = None
        self._ca_system_sign_file_request_list = None
        self._email = None
        self._mobile = None
        self._order = None
        self._our_corp = None
        self._send_link_flag = None
        self._sign_sub_type = None
        self._sign_user_id = None
        self._sign_user_type = None
        self._signer_cert_number = None
        self._signer_cert_type = None
        self._signer_name = None

    @property
    def auth_signer_cert_number(self):
        return self._auth_signer_cert_number

    @auth_signer_cert_number.setter
    def auth_signer_cert_number(self, value):
        self._auth_signer_cert_number = value
    @property
    def auth_signer_cert_type(self):
        return self._auth_signer_cert_type

    @auth_signer_cert_type.setter
    def auth_signer_cert_type(self, value):
        self._auth_signer_cert_type = value
    @property
    def auth_signer_name(self):
        return self._auth_signer_name

    @auth_signer_name.setter
    def auth_signer_name(self, value):
        self._auth_signer_name = value
    @property
    def authorized(self):
        return self._authorized

    @authorized.setter
    def authorized(self, value):
        self._authorized = value
    @property
    def auto_sign(self):
        return self._auto_sign

    @auto_sign.setter
    def auto_sign(self, value):
        self._auto_sign = value
    @property
    def ca_system_sign_file_request_list(self):
        return self._ca_system_sign_file_request_list

    @ca_system_sign_file_request_list.setter
    def ca_system_sign_file_request_list(self, value):
        if isinstance(value, list):
            self._ca_system_sign_file_request_list = list()
            for i in value:
                if isinstance(i, CaSystemSignFileRequest):
                    self._ca_system_sign_file_request_list.append(i)
                else:
                    self._ca_system_sign_file_request_list.append(CaSystemSignFileRequest.from_alipay_dict(i))
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value
    @property
    def our_corp(self):
        return self._our_corp

    @our_corp.setter
    def our_corp(self, value):
        self._our_corp = value
    @property
    def send_link_flag(self):
        return self._send_link_flag

    @send_link_flag.setter
    def send_link_flag(self, value):
        self._send_link_flag = value
    @property
    def sign_sub_type(self):
        return self._sign_sub_type

    @sign_sub_type.setter
    def sign_sub_type(self, value):
        self._sign_sub_type = value
    @property
    def sign_user_id(self):
        return self._sign_user_id

    @sign_user_id.setter
    def sign_user_id(self, value):
        self._sign_user_id = value
    @property
    def sign_user_type(self):
        return self._sign_user_type

    @sign_user_type.setter
    def sign_user_type(self, value):
        self._sign_user_type = value
    @property
    def signer_cert_number(self):
        return self._signer_cert_number

    @signer_cert_number.setter
    def signer_cert_number(self, value):
        self._signer_cert_number = value
    @property
    def signer_cert_type(self):
        return self._signer_cert_type

    @signer_cert_type.setter
    def signer_cert_type(self, value):
        self._signer_cert_type = value
    @property
    def signer_name(self):
        return self._signer_name

    @signer_name.setter
    def signer_name(self, value):
        self._signer_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_signer_cert_number:
            if hasattr(self.auth_signer_cert_number, 'to_alipay_dict'):
                params['auth_signer_cert_number'] = self.auth_signer_cert_number.to_alipay_dict()
            else:
                params['auth_signer_cert_number'] = self.auth_signer_cert_number
        if self.auth_signer_cert_type:
            if hasattr(self.auth_signer_cert_type, 'to_alipay_dict'):
                params['auth_signer_cert_type'] = self.auth_signer_cert_type.to_alipay_dict()
            else:
                params['auth_signer_cert_type'] = self.auth_signer_cert_type
        if self.auth_signer_name:
            if hasattr(self.auth_signer_name, 'to_alipay_dict'):
                params['auth_signer_name'] = self.auth_signer_name.to_alipay_dict()
            else:
                params['auth_signer_name'] = self.auth_signer_name
        if self.authorized:
            if hasattr(self.authorized, 'to_alipay_dict'):
                params['authorized'] = self.authorized.to_alipay_dict()
            else:
                params['authorized'] = self.authorized
        if self.auto_sign:
            if hasattr(self.auto_sign, 'to_alipay_dict'):
                params['auto_sign'] = self.auto_sign.to_alipay_dict()
            else:
                params['auto_sign'] = self.auto_sign
        if self.ca_system_sign_file_request_list:
            if isinstance(self.ca_system_sign_file_request_list, list):
                for i in range(0, len(self.ca_system_sign_file_request_list)):
                    element = self.ca_system_sign_file_request_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ca_system_sign_file_request_list[i] = element.to_alipay_dict()
            if hasattr(self.ca_system_sign_file_request_list, 'to_alipay_dict'):
                params['ca_system_sign_file_request_list'] = self.ca_system_sign_file_request_list.to_alipay_dict()
            else:
                params['ca_system_sign_file_request_list'] = self.ca_system_sign_file_request_list
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        if self.our_corp:
            if hasattr(self.our_corp, 'to_alipay_dict'):
                params['our_corp'] = self.our_corp.to_alipay_dict()
            else:
                params['our_corp'] = self.our_corp
        if self.send_link_flag:
            if hasattr(self.send_link_flag, 'to_alipay_dict'):
                params['send_link_flag'] = self.send_link_flag.to_alipay_dict()
            else:
                params['send_link_flag'] = self.send_link_flag
        if self.sign_sub_type:
            if hasattr(self.sign_sub_type, 'to_alipay_dict'):
                params['sign_sub_type'] = self.sign_sub_type.to_alipay_dict()
            else:
                params['sign_sub_type'] = self.sign_sub_type
        if self.sign_user_id:
            if hasattr(self.sign_user_id, 'to_alipay_dict'):
                params['sign_user_id'] = self.sign_user_id.to_alipay_dict()
            else:
                params['sign_user_id'] = self.sign_user_id
        if self.sign_user_type:
            if hasattr(self.sign_user_type, 'to_alipay_dict'):
                params['sign_user_type'] = self.sign_user_type.to_alipay_dict()
            else:
                params['sign_user_type'] = self.sign_user_type
        if self.signer_cert_number:
            if hasattr(self.signer_cert_number, 'to_alipay_dict'):
                params['signer_cert_number'] = self.signer_cert_number.to_alipay_dict()
            else:
                params['signer_cert_number'] = self.signer_cert_number
        if self.signer_cert_type:
            if hasattr(self.signer_cert_type, 'to_alipay_dict'):
                params['signer_cert_type'] = self.signer_cert_type.to_alipay_dict()
            else:
                params['signer_cert_type'] = self.signer_cert_type
        if self.signer_name:
            if hasattr(self.signer_name, 'to_alipay_dict'):
                params['signer_name'] = self.signer_name.to_alipay_dict()
            else:
                params['signer_name'] = self.signer_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntSignUserInfoRequest()
        if 'auth_signer_cert_number' in d:
            o.auth_signer_cert_number = d['auth_signer_cert_number']
        if 'auth_signer_cert_type' in d:
            o.auth_signer_cert_type = d['auth_signer_cert_type']
        if 'auth_signer_name' in d:
            o.auth_signer_name = d['auth_signer_name']
        if 'authorized' in d:
            o.authorized = d['authorized']
        if 'auto_sign' in d:
            o.auto_sign = d['auto_sign']
        if 'ca_system_sign_file_request_list' in d:
            o.ca_system_sign_file_request_list = d['ca_system_sign_file_request_list']
        if 'email' in d:
            o.email = d['email']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'order' in d:
            o.order = d['order']
        if 'our_corp' in d:
            o.our_corp = d['our_corp']
        if 'send_link_flag' in d:
            o.send_link_flag = d['send_link_flag']
        if 'sign_sub_type' in d:
            o.sign_sub_type = d['sign_sub_type']
        if 'sign_user_id' in d:
            o.sign_user_id = d['sign_user_id']
        if 'sign_user_type' in d:
            o.sign_user_type = d['sign_user_type']
        if 'signer_cert_number' in d:
            o.signer_cert_number = d['signer_cert_number']
        if 'signer_cert_type' in d:
            o.signer_cert_type = d['signer_cert_type']
        if 'signer_name' in d:
            o.signer_name = d['signer_name']
        return o


