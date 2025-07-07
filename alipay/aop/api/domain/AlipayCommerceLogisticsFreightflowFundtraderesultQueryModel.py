#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsFreightflowFundtraderesultQueryModel(object):

    def __init__(self):
        self._biz_no = None
        self._logistics_code = None
        self._mode = None
        self._mybank_app_id = None
        self._order_no = None
        self._partner_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
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
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
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
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFreightflowFundtraderesultQueryModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'mode' in d:
            o.mode = d['mode']
        if 'mybank_app_id' in d:
            o.mybank_app_id = d['mybank_app_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        return o


