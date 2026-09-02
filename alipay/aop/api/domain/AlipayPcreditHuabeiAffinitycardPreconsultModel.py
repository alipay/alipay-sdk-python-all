#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiAffinitycardPreconsultModel(object):

    def __init__(self):
        self._account_type = None
        self._alipay_user_id = None
        self._biz_scene = None
        self._merchant_partner_id = None
        self._open_id = None

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def merchant_partner_id(self):
        return self._merchant_partner_id

    @merchant_partner_id.setter
    def merchant_partner_id(self, value):
        self._merchant_partner_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.merchant_partner_id:
            if hasattr(self.merchant_partner_id, 'to_alipay_dict'):
                params['merchant_partner_id'] = self.merchant_partner_id.to_alipay_dict()
            else:
                params['merchant_partner_id'] = self.merchant_partner_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiAffinitycardPreconsultModel()
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'merchant_partner_id' in d:
            o.merchant_partner_id = d['merchant_partner_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        return o


