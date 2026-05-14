#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankAuthUserInfo(object):

    def __init__(self):
        self._alipay_account_no = None
        self._alipay_nick_name = None
        self._alipay_out_card_no = None
        self._user_cert_no = None
        self._user_name = None

    @property
    def alipay_account_no(self):
        return self._alipay_account_no

    @alipay_account_no.setter
    def alipay_account_no(self, value):
        self._alipay_account_no = value
    @property
    def alipay_nick_name(self):
        return self._alipay_nick_name

    @alipay_nick_name.setter
    def alipay_nick_name(self, value):
        self._alipay_nick_name = value
    @property
    def alipay_out_card_no(self):
        return self._alipay_out_card_no

    @alipay_out_card_no.setter
    def alipay_out_card_no(self, value):
        self._alipay_out_card_no = value
    @property
    def user_cert_no(self):
        return self._user_cert_no

    @user_cert_no.setter
    def user_cert_no(self, value):
        self._user_cert_no = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account_no:
            if hasattr(self.alipay_account_no, 'to_alipay_dict'):
                params['alipay_account_no'] = self.alipay_account_no.to_alipay_dict()
            else:
                params['alipay_account_no'] = self.alipay_account_no
        if self.alipay_nick_name:
            if hasattr(self.alipay_nick_name, 'to_alipay_dict'):
                params['alipay_nick_name'] = self.alipay_nick_name.to_alipay_dict()
            else:
                params['alipay_nick_name'] = self.alipay_nick_name
        if self.alipay_out_card_no:
            if hasattr(self.alipay_out_card_no, 'to_alipay_dict'):
                params['alipay_out_card_no'] = self.alipay_out_card_no.to_alipay_dict()
            else:
                params['alipay_out_card_no'] = self.alipay_out_card_no
        if self.user_cert_no:
            if hasattr(self.user_cert_no, 'to_alipay_dict'):
                params['user_cert_no'] = self.user_cert_no.to_alipay_dict()
            else:
                params['user_cert_no'] = self.user_cert_no
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankAuthUserInfo()
        if 'alipay_account_no' in d:
            o.alipay_account_no = d['alipay_account_no']
        if 'alipay_nick_name' in d:
            o.alipay_nick_name = d['alipay_nick_name']
        if 'alipay_out_card_no' in d:
            o.alipay_out_card_no = d['alipay_out_card_no']
        if 'user_cert_no' in d:
            o.user_cert_no = d['user_cert_no']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


