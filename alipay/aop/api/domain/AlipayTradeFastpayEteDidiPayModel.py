#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeFastpayEteDidiPayModel(object):

    def __init__(self):
        self._body = None
        self._extend_params = None
        self._login_id = None
        self._login_passwd = None
        self._mc_notify_url = None
        self._out_trade_no = None
        self._partner_id = None
        self._pay_passwd = None
        self._product_code = None
        self._seller_id = None
        self._subject = None
        self._total_fee = None
        self._user_id = None

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def login_passwd(self):
        return self._login_passwd

    @login_passwd.setter
    def login_passwd(self, value):
        self._login_passwd = value
    @property
    def mc_notify_url(self):
        return self._mc_notify_url

    @mc_notify_url.setter
    def mc_notify_url(self, value):
        self._mc_notify_url = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_passwd(self):
        return self._pay_passwd

    @pay_passwd.setter
    def pay_passwd(self, value):
        self._pay_passwd = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_fee(self):
        return self._total_fee

    @total_fee.setter
    def total_fee(self, value):
        self._total_fee = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.login_passwd:
            if hasattr(self.login_passwd, 'to_alipay_dict'):
                params['login_passwd'] = self.login_passwd.to_alipay_dict()
            else:
                params['login_passwd'] = self.login_passwd
        if self.mc_notify_url:
            if hasattr(self.mc_notify_url, 'to_alipay_dict'):
                params['mc_notify_url'] = self.mc_notify_url.to_alipay_dict()
            else:
                params['mc_notify_url'] = self.mc_notify_url
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_passwd:
            if hasattr(self.pay_passwd, 'to_alipay_dict'):
                params['pay_passwd'] = self.pay_passwd.to_alipay_dict()
            else:
                params['pay_passwd'] = self.pay_passwd
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_fee:
            if hasattr(self.total_fee, 'to_alipay_dict'):
                params['total_fee'] = self.total_fee.to_alipay_dict()
            else:
                params['total_fee'] = self.total_fee
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeFastpayEteDidiPayModel()
        if 'body' in d:
            o.body = d['body']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'login_passwd' in d:
            o.login_passwd = d['login_passwd']
        if 'mc_notify_url' in d:
            o.mc_notify_url = d['mc_notify_url']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_passwd' in d:
            o.pay_passwd = d['pay_passwd']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_fee' in d:
            o.total_fee = d['total_fee']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


