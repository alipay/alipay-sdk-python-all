#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentFundAuthFreezeInfoDTO(object):

    def __init__(self):
        self._auth_no = None
        self._freeze_notify_url = None
        self._fund_auth_scene = None
        self._payee_user_id = None
        self._risk_assessment_price = None

    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def freeze_notify_url(self):
        return self._freeze_notify_url

    @freeze_notify_url.setter
    def freeze_notify_url(self, value):
        self._freeze_notify_url = value
    @property
    def fund_auth_scene(self):
        return self._fund_auth_scene

    @fund_auth_scene.setter
    def fund_auth_scene(self, value):
        self._fund_auth_scene = value
    @property
    def payee_user_id(self):
        return self._payee_user_id

    @payee_user_id.setter
    def payee_user_id(self, value):
        self._payee_user_id = value
    @property
    def risk_assessment_price(self):
        return self._risk_assessment_price

    @risk_assessment_price.setter
    def risk_assessment_price(self, value):
        self._risk_assessment_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_no:
            if hasattr(self.auth_no, 'to_alipay_dict'):
                params['auth_no'] = self.auth_no.to_alipay_dict()
            else:
                params['auth_no'] = self.auth_no
        if self.freeze_notify_url:
            if hasattr(self.freeze_notify_url, 'to_alipay_dict'):
                params['freeze_notify_url'] = self.freeze_notify_url.to_alipay_dict()
            else:
                params['freeze_notify_url'] = self.freeze_notify_url
        if self.fund_auth_scene:
            if hasattr(self.fund_auth_scene, 'to_alipay_dict'):
                params['fund_auth_scene'] = self.fund_auth_scene.to_alipay_dict()
            else:
                params['fund_auth_scene'] = self.fund_auth_scene
        if self.payee_user_id:
            if hasattr(self.payee_user_id, 'to_alipay_dict'):
                params['payee_user_id'] = self.payee_user_id.to_alipay_dict()
            else:
                params['payee_user_id'] = self.payee_user_id
        if self.risk_assessment_price:
            if hasattr(self.risk_assessment_price, 'to_alipay_dict'):
                params['risk_assessment_price'] = self.risk_assessment_price.to_alipay_dict()
            else:
                params['risk_assessment_price'] = self.risk_assessment_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentFundAuthFreezeInfoDTO()
        if 'auth_no' in d:
            o.auth_no = d['auth_no']
        if 'freeze_notify_url' in d:
            o.freeze_notify_url = d['freeze_notify_url']
        if 'fund_auth_scene' in d:
            o.fund_auth_scene = d['fund_auth_scene']
        if 'payee_user_id' in d:
            o.payee_user_id = d['payee_user_id']
        if 'risk_assessment_price' in d:
            o.risk_assessment_price = d['risk_assessment_price']
        return o


