#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeZmgoPaysignConfirmModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._biz_type = None
        self._merchant_app_id = None
        self._partner_id = None
        self._zmgo_opt_no = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def merchant_app_id(self):
        return self._merchant_app_id

    @merchant_app_id.setter
    def merchant_app_id(self, value):
        self._merchant_app_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def zmgo_opt_no(self):
        return self._zmgo_opt_no

    @zmgo_opt_no.setter
    def zmgo_opt_no(self, value):
        self._zmgo_opt_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.merchant_app_id:
            if hasattr(self.merchant_app_id, 'to_alipay_dict'):
                params['merchant_app_id'] = self.merchant_app_id.to_alipay_dict()
            else:
                params['merchant_app_id'] = self.merchant_app_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.zmgo_opt_no:
            if hasattr(self.zmgo_opt_no, 'to_alipay_dict'):
                params['zmgo_opt_no'] = self.zmgo_opt_no.to_alipay_dict()
            else:
                params['zmgo_opt_no'] = self.zmgo_opt_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeZmgoPaysignConfirmModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'merchant_app_id' in d:
            o.merchant_app_id = d['merchant_app_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'zmgo_opt_no' in d:
            o.zmgo_opt_no = d['zmgo_opt_no']
        return o


