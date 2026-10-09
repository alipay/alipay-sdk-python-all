#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeEnterpriseDelegationPayModel(object):

    def __init__(self):
        self._agreement_no = None
        self._authorization_scene = None
        self._authorization_type = None
        self._business_params = None
        self._enable_pay_channels = None
        self._extend_params = None
        self._external_order_no = None
        self._open_id = None
        self._order_str = None
        self._prepay_id = None
        self._user_id = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def authorization_scene(self):
        return self._authorization_scene

    @authorization_scene.setter
    def authorization_scene(self, value):
        self._authorization_scene = value
    @property
    def authorization_type(self):
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, value):
        self._authorization_type = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        self._business_params = value
    @property
    def enable_pay_channels(self):
        return self._enable_pay_channels

    @enable_pay_channels.setter
    def enable_pay_channels(self, value):
        self._enable_pay_channels = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def external_order_no(self):
        return self._external_order_no

    @external_order_no.setter
    def external_order_no(self, value):
        self._external_order_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_str(self):
        return self._order_str

    @order_str.setter
    def order_str(self, value):
        self._order_str = value
    @property
    def prepay_id(self):
        return self._prepay_id

    @prepay_id.setter
    def prepay_id(self, value):
        self._prepay_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.authorization_scene:
            if hasattr(self.authorization_scene, 'to_alipay_dict'):
                params['authorization_scene'] = self.authorization_scene.to_alipay_dict()
            else:
                params['authorization_scene'] = self.authorization_scene
        if self.authorization_type:
            if hasattr(self.authorization_type, 'to_alipay_dict'):
                params['authorization_type'] = self.authorization_type.to_alipay_dict()
            else:
                params['authorization_type'] = self.authorization_type
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.enable_pay_channels:
            if hasattr(self.enable_pay_channels, 'to_alipay_dict'):
                params['enable_pay_channels'] = self.enable_pay_channels.to_alipay_dict()
            else:
                params['enable_pay_channels'] = self.enable_pay_channels
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.external_order_no:
            if hasattr(self.external_order_no, 'to_alipay_dict'):
                params['external_order_no'] = self.external_order_no.to_alipay_dict()
            else:
                params['external_order_no'] = self.external_order_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_str:
            if hasattr(self.order_str, 'to_alipay_dict'):
                params['order_str'] = self.order_str.to_alipay_dict()
            else:
                params['order_str'] = self.order_str
        if self.prepay_id:
            if hasattr(self.prepay_id, 'to_alipay_dict'):
                params['prepay_id'] = self.prepay_id.to_alipay_dict()
            else:
                params['prepay_id'] = self.prepay_id
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
        o = AlipayTradeEnterpriseDelegationPayModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'authorization_scene' in d:
            o.authorization_scene = d['authorization_scene']
        if 'authorization_type' in d:
            o.authorization_type = d['authorization_type']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'enable_pay_channels' in d:
            o.enable_pay_channels = d['enable_pay_channels']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'external_order_no' in d:
            o.external_order_no = d['external_order_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_str' in d:
            o.order_str = d['order_str']
        if 'prepay_id' in d:
            o.prepay_id = d['prepay_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


