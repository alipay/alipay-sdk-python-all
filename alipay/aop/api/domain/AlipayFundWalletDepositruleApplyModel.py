#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DepositRuleBizParam import DepositRuleBizParam
from alipay.aop.api.domain.ParticipantForm import ParticipantForm


class AlipayFundWalletDepositruleApplyModel(object):

    def __init__(self):
        self._biz_scene = None
        self._deposit_notify_url = None
        self._deposit_rule_biz_param = None
        self._deposit_rule_type = None
        self._out_biz_no = None
        self._principal_info = None
        self._product_code = None
        self._user_wallet_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def deposit_notify_url(self):
        return self._deposit_notify_url

    @deposit_notify_url.setter
    def deposit_notify_url(self, value):
        self._deposit_notify_url = value
    @property
    def deposit_rule_biz_param(self):
        return self._deposit_rule_biz_param

    @deposit_rule_biz_param.setter
    def deposit_rule_biz_param(self, value):
        if isinstance(value, DepositRuleBizParam):
            self._deposit_rule_biz_param = value
        else:
            self._deposit_rule_biz_param = DepositRuleBizParam.from_alipay_dict(value)
    @property
    def deposit_rule_type(self):
        return self._deposit_rule_type

    @deposit_rule_type.setter
    def deposit_rule_type(self, value):
        self._deposit_rule_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def principal_info(self):
        return self._principal_info

    @principal_info.setter
    def principal_info(self, value):
        if isinstance(value, ParticipantForm):
            self._principal_info = value
        else:
            self._principal_info = ParticipantForm.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.deposit_notify_url:
            if hasattr(self.deposit_notify_url, 'to_alipay_dict'):
                params['deposit_notify_url'] = self.deposit_notify_url.to_alipay_dict()
            else:
                params['deposit_notify_url'] = self.deposit_notify_url
        if self.deposit_rule_biz_param:
            if hasattr(self.deposit_rule_biz_param, 'to_alipay_dict'):
                params['deposit_rule_biz_param'] = self.deposit_rule_biz_param.to_alipay_dict()
            else:
                params['deposit_rule_biz_param'] = self.deposit_rule_biz_param
        if self.deposit_rule_type:
            if hasattr(self.deposit_rule_type, 'to_alipay_dict'):
                params['deposit_rule_type'] = self.deposit_rule_type.to_alipay_dict()
            else:
                params['deposit_rule_type'] = self.deposit_rule_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.principal_info:
            if hasattr(self.principal_info, 'to_alipay_dict'):
                params['principal_info'] = self.principal_info.to_alipay_dict()
            else:
                params['principal_info'] = self.principal_info
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.user_wallet_id:
            if hasattr(self.user_wallet_id, 'to_alipay_dict'):
                params['user_wallet_id'] = self.user_wallet_id.to_alipay_dict()
            else:
                params['user_wallet_id'] = self.user_wallet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundWalletDepositruleApplyModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'deposit_notify_url' in d:
            o.deposit_notify_url = d['deposit_notify_url']
        if 'deposit_rule_biz_param' in d:
            o.deposit_rule_biz_param = d['deposit_rule_biz_param']
        if 'deposit_rule_type' in d:
            o.deposit_rule_type = d['deposit_rule_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'principal_info' in d:
            o.principal_info = d['principal_info']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'user_wallet_id' in d:
            o.user_wallet_id = d['user_wallet_id']
        return o


