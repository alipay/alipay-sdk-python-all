#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsFreightflowParentaccountQueryModel(object):

    def __init__(self):
        self._account_card_no = None
        self._logistics_code = None
        self._mode = None
        self._mybank_app_id = None
        self._mybank_scene_code = None

    @property
    def account_card_no(self):
        return self._account_card_no

    @account_card_no.setter
    def account_card_no(self, value):
        self._account_card_no = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def mybank_app_id(self):
        return self._mybank_app_id

    @mybank_app_id.setter
    def mybank_app_id(self, value):
        self._mybank_app_id = value
    @property
    def mybank_scene_code(self):
        return self._mybank_scene_code

    @mybank_scene_code.setter
    def mybank_scene_code(self, value):
        self._mybank_scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_card_no:
            if hasattr(self.account_card_no, 'to_alipay_dict'):
                params['account_card_no'] = self.account_card_no.to_alipay_dict()
            else:
                params['account_card_no'] = self.account_card_no
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.mybank_app_id:
            if hasattr(self.mybank_app_id, 'to_alipay_dict'):
                params['mybank_app_id'] = self.mybank_app_id.to_alipay_dict()
            else:
                params['mybank_app_id'] = self.mybank_app_id
        if self.mybank_scene_code:
            if hasattr(self.mybank_scene_code, 'to_alipay_dict'):
                params['mybank_scene_code'] = self.mybank_scene_code.to_alipay_dict()
            else:
                params['mybank_scene_code'] = self.mybank_scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFreightflowParentaccountQueryModel()
        if 'account_card_no' in d:
            o.account_card_no = d['account_card_no']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'mode' in d:
            o.mode = d['mode']
        if 'mybank_app_id' in d:
            o.mybank_app_id = d['mybank_app_id']
        if 'mybank_scene_code' in d:
            o.mybank_scene_code = d['mybank_scene_code']
        return o


