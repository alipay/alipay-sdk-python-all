#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantActivityDetailGetModel(object):

    def __init__(self):
        self._activity_no = None
        self._canceled_callback = None
        self._shop_id = None
        self._sign_success_callback = None
        self._user_id = None

    @property
    def activity_no(self):
        return self._activity_no

    @activity_no.setter
    def activity_no(self, value):
        self._activity_no = value
    @property
    def canceled_callback(self):
        return self._canceled_callback

    @canceled_callback.setter
    def canceled_callback(self, value):
        self._canceled_callback = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sign_success_callback(self):
        return self._sign_success_callback

    @sign_success_callback.setter
    def sign_success_callback(self, value):
        self._sign_success_callback = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_no:
            if hasattr(self.activity_no, 'to_alipay_dict'):
                params['activity_no'] = self.activity_no.to_alipay_dict()
            else:
                params['activity_no'] = self.activity_no
        if self.canceled_callback:
            if hasattr(self.canceled_callback, 'to_alipay_dict'):
                params['canceled_callback'] = self.canceled_callback.to_alipay_dict()
            else:
                params['canceled_callback'] = self.canceled_callback
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sign_success_callback:
            if hasattr(self.sign_success_callback, 'to_alipay_dict'):
                params['sign_success_callback'] = self.sign_success_callback.to_alipay_dict()
            else:
                params['sign_success_callback'] = self.sign_success_callback
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
        o = ZhimaMerchantActivityDetailGetModel()
        if 'activity_no' in d:
            o.activity_no = d['activity_no']
        if 'canceled_callback' in d:
            o.canceled_callback = d['canceled_callback']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sign_success_callback' in d:
            o.sign_success_callback = d['sign_success_callback']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


