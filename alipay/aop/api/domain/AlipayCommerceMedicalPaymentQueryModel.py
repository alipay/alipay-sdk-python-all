#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalPaymentQueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._chnl_order_sn = None
        self._med_org_ord = None
        self._open_id = None
        self._org_no = None
        self._out_biz_type = None
        self._out_trade_no = None
        self._pay_order_id = None
        self._trade_no = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def chnl_order_sn(self):
        return self._chnl_order_sn

    @chnl_order_sn.setter
    def chnl_order_sn(self, value):
        self._chnl_order_sn = value
    @property
    def med_org_ord(self):
        return self._med_org_ord

    @med_org_ord.setter
    def med_org_ord(self, value):
        self._med_org_ord = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def org_no(self):
        return self._org_no

    @org_no.setter
    def org_no(self, value):
        self._org_no = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_order_id(self):
        return self._pay_order_id

    @pay_order_id.setter
    def pay_order_id(self, value):
        self._pay_order_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.chnl_order_sn:
            if hasattr(self.chnl_order_sn, 'to_alipay_dict'):
                params['chnl_order_sn'] = self.chnl_order_sn.to_alipay_dict()
            else:
                params['chnl_order_sn'] = self.chnl_order_sn
        if self.med_org_ord:
            if hasattr(self.med_org_ord, 'to_alipay_dict'):
                params['med_org_ord'] = self.med_org_ord.to_alipay_dict()
            else:
                params['med_org_ord'] = self.med_org_ord
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.org_no:
            if hasattr(self.org_no, 'to_alipay_dict'):
                params['org_no'] = self.org_no.to_alipay_dict()
            else:
                params['org_no'] = self.org_no
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pay_order_id:
            if hasattr(self.pay_order_id, 'to_alipay_dict'):
                params['pay_order_id'] = self.pay_order_id.to_alipay_dict()
            else:
                params['pay_order_id'] = self.pay_order_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalPaymentQueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'chnl_order_sn' in d:
            o.chnl_order_sn = d['chnl_order_sn']
        if 'med_org_ord' in d:
            o.med_org_ord = d['med_org_ord']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_no' in d:
            o.org_no = d['org_no']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pay_order_id' in d:
            o.pay_order_id = d['pay_order_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


