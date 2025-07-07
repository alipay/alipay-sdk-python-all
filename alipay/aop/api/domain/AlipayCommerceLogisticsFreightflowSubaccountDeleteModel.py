#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsFreightflowSubaccountDeleteModel(object):

    def __init__(self):
        self._logistics_code = None
        self._mode = None
        self._mybank_app_id = None
        self._mybank_scene_code = None
        self._mybank_scene_type = None
        self._mybank_sub_scene = None
        self._out_trade_no = None
        self._out_user_id = None
        self._partner_id = None
        self._sub_bank_card_no = None

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
    @property
    def mybank_scene_type(self):
        return self._mybank_scene_type

    @mybank_scene_type.setter
    def mybank_scene_type(self, value):
        self._mybank_scene_type = value
    @property
    def mybank_sub_scene(self):
        return self._mybank_sub_scene

    @mybank_sub_scene.setter
    def mybank_sub_scene(self, value):
        self._mybank_sub_scene = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def sub_bank_card_no(self):
        return self._sub_bank_card_no

    @sub_bank_card_no.setter
    def sub_bank_card_no(self, value):
        self._sub_bank_card_no = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.mybank_scene_type:
            if hasattr(self.mybank_scene_type, 'to_alipay_dict'):
                params['mybank_scene_type'] = self.mybank_scene_type.to_alipay_dict()
            else:
                params['mybank_scene_type'] = self.mybank_scene_type
        if self.mybank_sub_scene:
            if hasattr(self.mybank_sub_scene, 'to_alipay_dict'):
                params['mybank_sub_scene'] = self.mybank_sub_scene.to_alipay_dict()
            else:
                params['mybank_sub_scene'] = self.mybank_sub_scene
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.sub_bank_card_no:
            if hasattr(self.sub_bank_card_no, 'to_alipay_dict'):
                params['sub_bank_card_no'] = self.sub_bank_card_no.to_alipay_dict()
            else:
                params['sub_bank_card_no'] = self.sub_bank_card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFreightflowSubaccountDeleteModel()
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'mode' in d:
            o.mode = d['mode']
        if 'mybank_app_id' in d:
            o.mybank_app_id = d['mybank_app_id']
        if 'mybank_scene_code' in d:
            o.mybank_scene_code = d['mybank_scene_code']
        if 'mybank_scene_type' in d:
            o.mybank_scene_type = d['mybank_scene_type']
        if 'mybank_sub_scene' in d:
            o.mybank_sub_scene = d['mybank_sub_scene']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'sub_bank_card_no' in d:
            o.sub_bank_card_no = d['sub_bank_card_no']
        return o


