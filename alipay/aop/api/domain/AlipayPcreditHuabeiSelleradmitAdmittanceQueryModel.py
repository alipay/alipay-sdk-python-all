#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiSelleradmitAdmittanceQueryModel(object):

    def __init__(self):
        self._from_app = None
        self._partner_id = None
        self._payee_alipay_user_id = None
        self._request_id = None
        self._seller_admit_scene = None
        self._stall_code = None
        self._sub_merchant_id = None

    @property
    def from_app(self):
        return self._from_app

    @from_app.setter
    def from_app(self, value):
        self._from_app = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def payee_alipay_user_id(self):
        return self._payee_alipay_user_id

    @payee_alipay_user_id.setter
    def payee_alipay_user_id(self, value):
        self._payee_alipay_user_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def seller_admit_scene(self):
        return self._seller_admit_scene

    @seller_admit_scene.setter
    def seller_admit_scene(self, value):
        self._seller_admit_scene = value
    @property
    def stall_code(self):
        return self._stall_code

    @stall_code.setter
    def stall_code(self, value):
        self._stall_code = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.from_app:
            if hasattr(self.from_app, 'to_alipay_dict'):
                params['from_app'] = self.from_app.to_alipay_dict()
            else:
                params['from_app'] = self.from_app
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.payee_alipay_user_id:
            if hasattr(self.payee_alipay_user_id, 'to_alipay_dict'):
                params['payee_alipay_user_id'] = self.payee_alipay_user_id.to_alipay_dict()
            else:
                params['payee_alipay_user_id'] = self.payee_alipay_user_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.seller_admit_scene:
            if hasattr(self.seller_admit_scene, 'to_alipay_dict'):
                params['seller_admit_scene'] = self.seller_admit_scene.to_alipay_dict()
            else:
                params['seller_admit_scene'] = self.seller_admit_scene
        if self.stall_code:
            if hasattr(self.stall_code, 'to_alipay_dict'):
                params['stall_code'] = self.stall_code.to_alipay_dict()
            else:
                params['stall_code'] = self.stall_code
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiSelleradmitAdmittanceQueryModel()
        if 'from_app' in d:
            o.from_app = d['from_app']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'payee_alipay_user_id' in d:
            o.payee_alipay_user_id = d['payee_alipay_user_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'seller_admit_scene' in d:
            o.seller_admit_scene = d['seller_admit_scene']
        if 'stall_code' in d:
            o.stall_code = d['stall_code']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        return o


