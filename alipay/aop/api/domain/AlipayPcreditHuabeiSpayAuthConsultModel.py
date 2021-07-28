#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtInfos import ExtInfos
from alipay.aop.api.domain.MerchantIDInfo import MerchantIDInfo
from alipay.aop.api.domain.UserDInfo import UserDInfo


class AlipayPcreditHuabeiSpayAuthConsultModel(object):

    def __init__(self):
        self._asset_type_code = None
        self._biz_type = None
        self._business_code = None
        self._ext_infos = None
        self._fee_rate_percent = None
        self._fee_taker_role = None
        self._link_mode = None
        self._merchant = None
        self._payment_mode = None
        self._receive_mode = None
        self._total_install_num = None
        self._total_payment_amount = None
        self._user = None
        self._user_id = None

    @property
    def asset_type_code(self):
        return self._asset_type_code

    @asset_type_code.setter
    def asset_type_code(self, value):
        self._asset_type_code = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        if isinstance(value, ExtInfos):
            self._ext_infos = value
        else:
            self._ext_infos = ExtInfos.from_alipay_dict(value)
    @property
    def fee_rate_percent(self):
        return self._fee_rate_percent

    @fee_rate_percent.setter
    def fee_rate_percent(self, value):
        self._fee_rate_percent = value
    @property
    def fee_taker_role(self):
        return self._fee_taker_role

    @fee_taker_role.setter
    def fee_taker_role(self, value):
        self._fee_taker_role = value
    @property
    def link_mode(self):
        return self._link_mode

    @link_mode.setter
    def link_mode(self, value):
        self._link_mode = value
    @property
    def merchant(self):
        return self._merchant

    @merchant.setter
    def merchant(self, value):
        if isinstance(value, MerchantIDInfo):
            self._merchant = value
        else:
            self._merchant = MerchantIDInfo.from_alipay_dict(value)
    @property
    def payment_mode(self):
        return self._payment_mode

    @payment_mode.setter
    def payment_mode(self, value):
        self._payment_mode = value
    @property
    def receive_mode(self):
        return self._receive_mode

    @receive_mode.setter
    def receive_mode(self, value):
        self._receive_mode = value
    @property
    def total_install_num(self):
        return self._total_install_num

    @total_install_num.setter
    def total_install_num(self, value):
        self._total_install_num = value
    @property
    def total_payment_amount(self):
        return self._total_payment_amount

    @total_payment_amount.setter
    def total_payment_amount(self, value):
        self._total_payment_amount = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, UserDInfo):
            self._user = value
        else:
            self._user = UserDInfo.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_type_code:
            if hasattr(self.asset_type_code, 'to_alipay_dict'):
                params['asset_type_code'] = self.asset_type_code.to_alipay_dict()
            else:
                params['asset_type_code'] = self.asset_type_code
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.fee_rate_percent:
            if hasattr(self.fee_rate_percent, 'to_alipay_dict'):
                params['fee_rate_percent'] = self.fee_rate_percent.to_alipay_dict()
            else:
                params['fee_rate_percent'] = self.fee_rate_percent
        if self.fee_taker_role:
            if hasattr(self.fee_taker_role, 'to_alipay_dict'):
                params['fee_taker_role'] = self.fee_taker_role.to_alipay_dict()
            else:
                params['fee_taker_role'] = self.fee_taker_role
        if self.link_mode:
            if hasattr(self.link_mode, 'to_alipay_dict'):
                params['link_mode'] = self.link_mode.to_alipay_dict()
            else:
                params['link_mode'] = self.link_mode
        if self.merchant:
            if hasattr(self.merchant, 'to_alipay_dict'):
                params['merchant'] = self.merchant.to_alipay_dict()
            else:
                params['merchant'] = self.merchant
        if self.payment_mode:
            if hasattr(self.payment_mode, 'to_alipay_dict'):
                params['payment_mode'] = self.payment_mode.to_alipay_dict()
            else:
                params['payment_mode'] = self.payment_mode
        if self.receive_mode:
            if hasattr(self.receive_mode, 'to_alipay_dict'):
                params['receive_mode'] = self.receive_mode.to_alipay_dict()
            else:
                params['receive_mode'] = self.receive_mode
        if self.total_install_num:
            if hasattr(self.total_install_num, 'to_alipay_dict'):
                params['total_install_num'] = self.total_install_num.to_alipay_dict()
            else:
                params['total_install_num'] = self.total_install_num
        if self.total_payment_amount:
            if hasattr(self.total_payment_amount, 'to_alipay_dict'):
                params['total_payment_amount'] = self.total_payment_amount.to_alipay_dict()
            else:
                params['total_payment_amount'] = self.total_payment_amount
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
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
        o = AlipayPcreditHuabeiSpayAuthConsultModel()
        if 'asset_type_code' in d:
            o.asset_type_code = d['asset_type_code']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'fee_rate_percent' in d:
            o.fee_rate_percent = d['fee_rate_percent']
        if 'fee_taker_role' in d:
            o.fee_taker_role = d['fee_taker_role']
        if 'link_mode' in d:
            o.link_mode = d['link_mode']
        if 'merchant' in d:
            o.merchant = d['merchant']
        if 'payment_mode' in d:
            o.payment_mode = d['payment_mode']
        if 'receive_mode' in d:
            o.receive_mode = d['receive_mode']
        if 'total_install_num' in d:
            o.total_install_num = d['total_install_num']
        if 'total_payment_amount' in d:
            o.total_payment_amount = d['total_payment_amount']
        if 'user' in d:
            o.user = d['user']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


