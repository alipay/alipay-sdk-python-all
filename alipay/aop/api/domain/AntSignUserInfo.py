#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CaSystemSignFile import CaSystemSignFile
from alipay.aop.api.domain.UserCertifyInfo import UserCertifyInfo


class AntSignUserInfo(object):

    def __init__(self):
        self._auto_sign = None
        self._ca_system_sign_file_list = None
        self._order = None
        self._our_corp = None
        self._redirect_url = None
        self._sign_user_type = None
        self._signer_cert_number = None
        self._signer_cert_type = None
        self._signer_name = None
        self._signer_name_style = None
        self._user_certify_info = None

    @property
    def auto_sign(self):
        return self._auto_sign

    @auto_sign.setter
    def auto_sign(self, value):
        self._auto_sign = value
    @property
    def ca_system_sign_file_list(self):
        return self._ca_system_sign_file_list

    @ca_system_sign_file_list.setter
    def ca_system_sign_file_list(self, value):
        if isinstance(value, list):
            self._ca_system_sign_file_list = list()
            for i in value:
                if isinstance(i, CaSystemSignFile):
                    self._ca_system_sign_file_list.append(i)
                else:
                    self._ca_system_sign_file_list.append(CaSystemSignFile.from_alipay_dict(i))
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
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
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
    @property
    def signer_name_style(self):
        return self._signer_name_style

    @signer_name_style.setter
    def signer_name_style(self, value):
        self._signer_name_style = value
    @property
    def user_certify_info(self):
        return self._user_certify_info

    @user_certify_info.setter
    def user_certify_info(self, value):
        if isinstance(value, UserCertifyInfo):
            self._user_certify_info = value
        else:
            self._user_certify_info = UserCertifyInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.auto_sign:
            if hasattr(self.auto_sign, 'to_alipay_dict'):
                params['auto_sign'] = self.auto_sign.to_alipay_dict()
            else:
                params['auto_sign'] = self.auto_sign
        if self.ca_system_sign_file_list:
            if isinstance(self.ca_system_sign_file_list, list):
                for i in range(0, len(self.ca_system_sign_file_list)):
                    element = self.ca_system_sign_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ca_system_sign_file_list[i] = element.to_alipay_dict()
            if hasattr(self.ca_system_sign_file_list, 'to_alipay_dict'):
                params['ca_system_sign_file_list'] = self.ca_system_sign_file_list.to_alipay_dict()
            else:
                params['ca_system_sign_file_list'] = self.ca_system_sign_file_list
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
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
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
        if self.signer_name_style:
            if hasattr(self.signer_name_style, 'to_alipay_dict'):
                params['signer_name_style'] = self.signer_name_style.to_alipay_dict()
            else:
                params['signer_name_style'] = self.signer_name_style
        if self.user_certify_info:
            if hasattr(self.user_certify_info, 'to_alipay_dict'):
                params['user_certify_info'] = self.user_certify_info.to_alipay_dict()
            else:
                params['user_certify_info'] = self.user_certify_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntSignUserInfo()
        if 'auto_sign' in d:
            o.auto_sign = d['auto_sign']
        if 'ca_system_sign_file_list' in d:
            o.ca_system_sign_file_list = d['ca_system_sign_file_list']
        if 'order' in d:
            o.order = d['order']
        if 'our_corp' in d:
            o.our_corp = d['our_corp']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'sign_user_type' in d:
            o.sign_user_type = d['sign_user_type']
        if 'signer_cert_number' in d:
            o.signer_cert_number = d['signer_cert_number']
        if 'signer_cert_type' in d:
            o.signer_cert_type = d['signer_cert_type']
        if 'signer_name' in d:
            o.signer_name = d['signer_name']
        if 'signer_name_style' in d:
            o.signer_name_style = d['signer_name_style']
        if 'user_certify_info' in d:
            o.user_certify_info = d['user_certify_info']
        return o


