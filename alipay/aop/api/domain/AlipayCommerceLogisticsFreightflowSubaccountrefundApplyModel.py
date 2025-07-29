#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsFreightflowSubaccountrefundApplyModel(object):

    def __init__(self):
        self._logistics_code = None
        self._mode = None
        self._mybank_app_id = None
        self._mybank_scene_code = None
        self._out_trade_no = None
        self._partner_id = None
        self._refund_amt = None
        self._trans_no = None

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
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def refund_amt(self):
        return self._refund_amt

    @refund_amt.setter
    def refund_amt(self, value):
        self._refund_amt = value
    @property
    def trans_no(self):
        return self._trans_no

    @trans_no.setter
    def trans_no(self, value):
        self._trans_no = value


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
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.refund_amt:
            if hasattr(self.refund_amt, 'to_alipay_dict'):
                params['refund_amt'] = self.refund_amt.to_alipay_dict()
            else:
                params['refund_amt'] = self.refund_amt
        if self.trans_no:
            if hasattr(self.trans_no, 'to_alipay_dict'):
                params['trans_no'] = self.trans_no.to_alipay_dict()
            else:
                params['trans_no'] = self.trans_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFreightflowSubaccountrefundApplyModel()
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'mode' in d:
            o.mode = d['mode']
        if 'mybank_app_id' in d:
            o.mybank_app_id = d['mybank_app_id']
        if 'mybank_scene_code' in d:
            o.mybank_scene_code = d['mybank_scene_code']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'refund_amt' in d:
            o.refund_amt = d['refund_amt']
        if 'trans_no' in d:
            o.trans_no = d['trans_no']
        return o


