#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseMarketingPayinstCouponSendModel(object):

    def __init__(self):
        self._campaign_id = None
        self._encrypt_type = None
        self._login_id = None
        self._out_request_id = None
        self._phone_id = None
        self._send_voucher_type = None
        self._weixin_id = None

    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def encrypt_type(self):
        return self._encrypt_type

    @encrypt_type.setter
    def encrypt_type(self, value):
        self._encrypt_type = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def out_request_id(self):
        return self._out_request_id

    @out_request_id.setter
    def out_request_id(self, value):
        self._out_request_id = value
    @property
    def phone_id(self):
        return self._phone_id

    @phone_id.setter
    def phone_id(self, value):
        self._phone_id = value
    @property
    def send_voucher_type(self):
        return self._send_voucher_type

    @send_voucher_type.setter
    def send_voucher_type(self, value):
        self._send_voucher_type = value
    @property
    def weixin_id(self):
        return self._weixin_id

    @weixin_id.setter
    def weixin_id(self, value):
        self._weixin_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.campaign_id:
            if hasattr(self.campaign_id, 'to_alipay_dict'):
                params['campaign_id'] = self.campaign_id.to_alipay_dict()
            else:
                params['campaign_id'] = self.campaign_id
        if self.encrypt_type:
            if hasattr(self.encrypt_type, 'to_alipay_dict'):
                params['encrypt_type'] = self.encrypt_type.to_alipay_dict()
            else:
                params['encrypt_type'] = self.encrypt_type
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.out_request_id:
            if hasattr(self.out_request_id, 'to_alipay_dict'):
                params['out_request_id'] = self.out_request_id.to_alipay_dict()
            else:
                params['out_request_id'] = self.out_request_id
        if self.phone_id:
            if hasattr(self.phone_id, 'to_alipay_dict'):
                params['phone_id'] = self.phone_id.to_alipay_dict()
            else:
                params['phone_id'] = self.phone_id
        if self.send_voucher_type:
            if hasattr(self.send_voucher_type, 'to_alipay_dict'):
                params['send_voucher_type'] = self.send_voucher_type.to_alipay_dict()
            else:
                params['send_voucher_type'] = self.send_voucher_type
        if self.weixin_id:
            if hasattr(self.weixin_id, 'to_alipay_dict'):
                params['weixin_id'] = self.weixin_id.to_alipay_dict()
            else:
                params['weixin_id'] = self.weixin_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechMorseMarketingPayinstCouponSendModel()
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'encrypt_type' in d:
            o.encrypt_type = d['encrypt_type']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'out_request_id' in d:
            o.out_request_id = d['out_request_id']
        if 'phone_id' in d:
            o.phone_id = d['phone_id']
        if 'send_voucher_type' in d:
            o.send_voucher_type = d['send_voucher_type']
        if 'weixin_id' in d:
            o.weixin_id = d['weixin_id']
        return o


