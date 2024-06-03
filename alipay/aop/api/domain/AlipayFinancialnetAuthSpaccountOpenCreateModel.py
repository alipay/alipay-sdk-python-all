#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetAuthSpaccountOpenCreateModel(object):

    def __init__(self):
        self._bank_card_inst = None
        self._bank_card_no = None
        self._bank_card_type = None
        self._biz_identity = None
        self._inst_id = None
        self._openid = None
        self._sign_product_id = None
        self._user_id = None

    @property
    def bank_card_inst(self):
        return self._bank_card_inst

    @bank_card_inst.setter
    def bank_card_inst(self, value):
        self._bank_card_inst = value
    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def bank_card_type(self):
        return self._bank_card_type

    @bank_card_type.setter
    def bank_card_type(self, value):
        self._bank_card_type = value
    @property
    def biz_identity(self):
        return self._biz_identity

    @biz_identity.setter
    def biz_identity(self, value):
        self._biz_identity = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def openid(self):
        return self._openid

    @openid.setter
    def openid(self, value):
        self._openid = value
    @property
    def sign_product_id(self):
        return self._sign_product_id

    @sign_product_id.setter
    def sign_product_id(self, value):
        self._sign_product_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_inst:
            if hasattr(self.bank_card_inst, 'to_alipay_dict'):
                params['bank_card_inst'] = self.bank_card_inst.to_alipay_dict()
            else:
                params['bank_card_inst'] = self.bank_card_inst
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.bank_card_type:
            if hasattr(self.bank_card_type, 'to_alipay_dict'):
                params['bank_card_type'] = self.bank_card_type.to_alipay_dict()
            else:
                params['bank_card_type'] = self.bank_card_type
        if self.biz_identity:
            if hasattr(self.biz_identity, 'to_alipay_dict'):
                params['biz_identity'] = self.biz_identity.to_alipay_dict()
            else:
                params['biz_identity'] = self.biz_identity
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.openid:
            if hasattr(self.openid, 'to_alipay_dict'):
                params['openid'] = self.openid.to_alipay_dict()
            else:
                params['openid'] = self.openid
        if self.sign_product_id:
            if hasattr(self.sign_product_id, 'to_alipay_dict'):
                params['sign_product_id'] = self.sign_product_id.to_alipay_dict()
            else:
                params['sign_product_id'] = self.sign_product_id
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
        o = AlipayFinancialnetAuthSpaccountOpenCreateModel()
        if 'bank_card_inst' in d:
            o.bank_card_inst = d['bank_card_inst']
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'bank_card_type' in d:
            o.bank_card_type = d['bank_card_type']
        if 'biz_identity' in d:
            o.biz_identity = d['biz_identity']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'openid' in d:
            o.openid = d['openid']
        if 'sign_product_id' in d:
            o.sign_product_id = d['sign_product_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


