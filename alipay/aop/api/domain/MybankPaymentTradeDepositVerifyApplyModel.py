#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankPaymentTradeDepositVerifyApplyModel(object):

    def __init__(self):
        self._bank_card_name = None
        self._bank_card_no = None
        self._bank_code = None
        self._callback_url = None
        self._credit_code = None
        self._legal_person_cert_no = None
        self._legal_person_cert_type = None
        self._legal_person_name = None
        self._member_id = None
        self._mobile = None
        self._request_no = None
        self._scene = None

    @property
    def bank_card_name(self):
        return self._bank_card_name

    @bank_card_name.setter
    def bank_card_name(self, value):
        self._bank_card_name = value
    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def legal_person_cert_no(self):
        return self._legal_person_cert_no

    @legal_person_cert_no.setter
    def legal_person_cert_no(self, value):
        self._legal_person_cert_no = value
    @property
    def legal_person_cert_type(self):
        return self._legal_person_cert_type

    @legal_person_cert_type.setter
    def legal_person_cert_type(self, value):
        self._legal_person_cert_type = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_name:
            if hasattr(self.bank_card_name, 'to_alipay_dict'):
                params['bank_card_name'] = self.bank_card_name.to_alipay_dict()
            else:
                params['bank_card_name'] = self.bank_card_name
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
        if self.credit_code:
            if hasattr(self.credit_code, 'to_alipay_dict'):
                params['credit_code'] = self.credit_code.to_alipay_dict()
            else:
                params['credit_code'] = self.credit_code
        if self.legal_person_cert_no:
            if hasattr(self.legal_person_cert_no, 'to_alipay_dict'):
                params['legal_person_cert_no'] = self.legal_person_cert_no.to_alipay_dict()
            else:
                params['legal_person_cert_no'] = self.legal_person_cert_no
        if self.legal_person_cert_type:
            if hasattr(self.legal_person_cert_type, 'to_alipay_dict'):
                params['legal_person_cert_type'] = self.legal_person_cert_type.to_alipay_dict()
            else:
                params['legal_person_cert_type'] = self.legal_person_cert_type
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankPaymentTradeDepositVerifyApplyModel()
        if 'bank_card_name' in d:
            o.bank_card_name = d['bank_card_name']
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'credit_code' in d:
            o.credit_code = d['credit_code']
        if 'legal_person_cert_no' in d:
            o.legal_person_cert_no = d['legal_person_cert_no']
        if 'legal_person_cert_type' in d:
            o.legal_person_cert_type = d['legal_person_cert_type']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'scene' in d:
            o.scene = d['scene']
        return o


