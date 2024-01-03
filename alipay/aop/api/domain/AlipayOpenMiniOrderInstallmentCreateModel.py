#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniOrderInstallmentCreateModel(object):

    def __init__(self):
        self._addon_period_num = None
        self._installment_no = None
        self._installment_no_type = None
        self._installment_price = None
        self._is_finish_performance = None
        self._open_id = None
        self._order_id = None
        self._out_installment_order_id = None
        self._out_order_id = None
        self._period_num = None
        self._trade_no = None
        self._type = None
        self._user_id = None

    @property
    def addon_period_num(self):
        return self._addon_period_num

    @addon_period_num.setter
    def addon_period_num(self, value):
        self._addon_period_num = value
    @property
    def installment_no(self):
        return self._installment_no

    @installment_no.setter
    def installment_no(self, value):
        self._installment_no = value
    @property
    def installment_no_type(self):
        return self._installment_no_type

    @installment_no_type.setter
    def installment_no_type(self, value):
        self._installment_no_type = value
    @property
    def installment_price(self):
        return self._installment_price

    @installment_price.setter
    def installment_price(self, value):
        self._installment_price = value
    @property
    def is_finish_performance(self):
        return self._is_finish_performance

    @is_finish_performance.setter
    def is_finish_performance(self, value):
        self._is_finish_performance = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_installment_order_id(self):
        return self._out_installment_order_id

    @out_installment_order_id.setter
    def out_installment_order_id(self, value):
        self._out_installment_order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def period_num(self):
        return self._period_num

    @period_num.setter
    def period_num(self, value):
        self._period_num = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.addon_period_num:
            if hasattr(self.addon_period_num, 'to_alipay_dict'):
                params['addon_period_num'] = self.addon_period_num.to_alipay_dict()
            else:
                params['addon_period_num'] = self.addon_period_num
        if self.installment_no:
            if hasattr(self.installment_no, 'to_alipay_dict'):
                params['installment_no'] = self.installment_no.to_alipay_dict()
            else:
                params['installment_no'] = self.installment_no
        if self.installment_no_type:
            if hasattr(self.installment_no_type, 'to_alipay_dict'):
                params['installment_no_type'] = self.installment_no_type.to_alipay_dict()
            else:
                params['installment_no_type'] = self.installment_no_type
        if self.installment_price:
            if hasattr(self.installment_price, 'to_alipay_dict'):
                params['installment_price'] = self.installment_price.to_alipay_dict()
            else:
                params['installment_price'] = self.installment_price
        if self.is_finish_performance:
            if hasattr(self.is_finish_performance, 'to_alipay_dict'):
                params['is_finish_performance'] = self.is_finish_performance.to_alipay_dict()
            else:
                params['is_finish_performance'] = self.is_finish_performance
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_installment_order_id:
            if hasattr(self.out_installment_order_id, 'to_alipay_dict'):
                params['out_installment_order_id'] = self.out_installment_order_id.to_alipay_dict()
            else:
                params['out_installment_order_id'] = self.out_installment_order_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.period_num:
            if hasattr(self.period_num, 'to_alipay_dict'):
                params['period_num'] = self.period_num.to_alipay_dict()
            else:
                params['period_num'] = self.period_num
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = AlipayOpenMiniOrderInstallmentCreateModel()
        if 'addon_period_num' in d:
            o.addon_period_num = d['addon_period_num']
        if 'installment_no' in d:
            o.installment_no = d['installment_no']
        if 'installment_no_type' in d:
            o.installment_no_type = d['installment_no_type']
        if 'installment_price' in d:
            o.installment_price = d['installment_price']
        if 'is_finish_performance' in d:
            o.is_finish_performance = d['is_finish_performance']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_installment_order_id' in d:
            o.out_installment_order_id = d['out_installment_order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'period_num' in d:
            o.period_num = d['period_num']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


