#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZmEpAePrepayExtParam import ZmEpAePrepayExtParam


class ZhimaCreditEpAeprepayOrderPrepayModel(object):

    def __init__(self):
        self._ext_param = None
        self._make_loan_success = None
        self._order_num = None
        self._order_time_millis = None
        self._seller_login_id = None
        self._sub_order_amt = None
        self._sub_order_ccy = None
        self._sub_order_loan_amt = None
        self._sub_order_loan_ccy = None
        self._sub_order_num = None

    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        if isinstance(value, ZmEpAePrepayExtParam):
            self._ext_param = value
        else:
            self._ext_param = ZmEpAePrepayExtParam.from_alipay_dict(value)
    @property
    def make_loan_success(self):
        return self._make_loan_success

    @make_loan_success.setter
    def make_loan_success(self, value):
        self._make_loan_success = value
    @property
    def order_num(self):
        return self._order_num

    @order_num.setter
    def order_num(self, value):
        self._order_num = value
    @property
    def order_time_millis(self):
        return self._order_time_millis

    @order_time_millis.setter
    def order_time_millis(self, value):
        self._order_time_millis = value
    @property
    def seller_login_id(self):
        return self._seller_login_id

    @seller_login_id.setter
    def seller_login_id(self, value):
        self._seller_login_id = value
    @property
    def sub_order_amt(self):
        return self._sub_order_amt

    @sub_order_amt.setter
    def sub_order_amt(self, value):
        self._sub_order_amt = value
    @property
    def sub_order_ccy(self):
        return self._sub_order_ccy

    @sub_order_ccy.setter
    def sub_order_ccy(self, value):
        self._sub_order_ccy = value
    @property
    def sub_order_loan_amt(self):
        return self._sub_order_loan_amt

    @sub_order_loan_amt.setter
    def sub_order_loan_amt(self, value):
        self._sub_order_loan_amt = value
    @property
    def sub_order_loan_ccy(self):
        return self._sub_order_loan_ccy

    @sub_order_loan_ccy.setter
    def sub_order_loan_ccy(self, value):
        self._sub_order_loan_ccy = value
    @property
    def sub_order_num(self):
        return self._sub_order_num

    @sub_order_num.setter
    def sub_order_num(self, value):
        self._sub_order_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.make_loan_success:
            if hasattr(self.make_loan_success, 'to_alipay_dict'):
                params['make_loan_success'] = self.make_loan_success.to_alipay_dict()
            else:
                params['make_loan_success'] = self.make_loan_success
        if self.order_num:
            if hasattr(self.order_num, 'to_alipay_dict'):
                params['order_num'] = self.order_num.to_alipay_dict()
            else:
                params['order_num'] = self.order_num
        if self.order_time_millis:
            if hasattr(self.order_time_millis, 'to_alipay_dict'):
                params['order_time_millis'] = self.order_time_millis.to_alipay_dict()
            else:
                params['order_time_millis'] = self.order_time_millis
        if self.seller_login_id:
            if hasattr(self.seller_login_id, 'to_alipay_dict'):
                params['seller_login_id'] = self.seller_login_id.to_alipay_dict()
            else:
                params['seller_login_id'] = self.seller_login_id
        if self.sub_order_amt:
            if hasattr(self.sub_order_amt, 'to_alipay_dict'):
                params['sub_order_amt'] = self.sub_order_amt.to_alipay_dict()
            else:
                params['sub_order_amt'] = self.sub_order_amt
        if self.sub_order_ccy:
            if hasattr(self.sub_order_ccy, 'to_alipay_dict'):
                params['sub_order_ccy'] = self.sub_order_ccy.to_alipay_dict()
            else:
                params['sub_order_ccy'] = self.sub_order_ccy
        if self.sub_order_loan_amt:
            if hasattr(self.sub_order_loan_amt, 'to_alipay_dict'):
                params['sub_order_loan_amt'] = self.sub_order_loan_amt.to_alipay_dict()
            else:
                params['sub_order_loan_amt'] = self.sub_order_loan_amt
        if self.sub_order_loan_ccy:
            if hasattr(self.sub_order_loan_ccy, 'to_alipay_dict'):
                params['sub_order_loan_ccy'] = self.sub_order_loan_ccy.to_alipay_dict()
            else:
                params['sub_order_loan_ccy'] = self.sub_order_loan_ccy
        if self.sub_order_num:
            if hasattr(self.sub_order_num, 'to_alipay_dict'):
                params['sub_order_num'] = self.sub_order_num.to_alipay_dict()
            else:
                params['sub_order_num'] = self.sub_order_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAeprepayOrderPrepayModel()
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'make_loan_success' in d:
            o.make_loan_success = d['make_loan_success']
        if 'order_num' in d:
            o.order_num = d['order_num']
        if 'order_time_millis' in d:
            o.order_time_millis = d['order_time_millis']
        if 'seller_login_id' in d:
            o.seller_login_id = d['seller_login_id']
        if 'sub_order_amt' in d:
            o.sub_order_amt = d['sub_order_amt']
        if 'sub_order_ccy' in d:
            o.sub_order_ccy = d['sub_order_ccy']
        if 'sub_order_loan_amt' in d:
            o.sub_order_loan_amt = d['sub_order_loan_amt']
        if 'sub_order_loan_ccy' in d:
            o.sub_order_loan_ccy = d['sub_order_loan_ccy']
        if 'sub_order_num' in d:
            o.sub_order_num = d['sub_order_num']
        return o


