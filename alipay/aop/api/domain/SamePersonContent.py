#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SamePersonContent(object):

    def __init__(self):
        self._cur_account_login_id = None
        self._pay_account_login_id = None
        self._pay_account_nick_name = None

    @property
    def cur_account_login_id(self):
        return self._cur_account_login_id

    @cur_account_login_id.setter
    def cur_account_login_id(self, value):
        self._cur_account_login_id = value
    @property
    def pay_account_login_id(self):
        return self._pay_account_login_id

    @pay_account_login_id.setter
    def pay_account_login_id(self, value):
        self._pay_account_login_id = value
    @property
    def pay_account_nick_name(self):
        return self._pay_account_nick_name

    @pay_account_nick_name.setter
    def pay_account_nick_name(self, value):
        self._pay_account_nick_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cur_account_login_id:
            if hasattr(self.cur_account_login_id, 'to_alipay_dict'):
                params['cur_account_login_id'] = self.cur_account_login_id.to_alipay_dict()
            else:
                params['cur_account_login_id'] = self.cur_account_login_id
        if self.pay_account_login_id:
            if hasattr(self.pay_account_login_id, 'to_alipay_dict'):
                params['pay_account_login_id'] = self.pay_account_login_id.to_alipay_dict()
            else:
                params['pay_account_login_id'] = self.pay_account_login_id
        if self.pay_account_nick_name:
            if hasattr(self.pay_account_nick_name, 'to_alipay_dict'):
                params['pay_account_nick_name'] = self.pay_account_nick_name.to_alipay_dict()
            else:
                params['pay_account_nick_name'] = self.pay_account_nick_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SamePersonContent()
        if 'cur_account_login_id' in d:
            o.cur_account_login_id = d['cur_account_login_id']
        if 'pay_account_login_id' in d:
            o.pay_account_login_id = d['pay_account_login_id']
        if 'pay_account_nick_name' in d:
            o.pay_account_nick_name = d['pay_account_nick_name']
        return o


