#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserGamecenterCoinPayModel(object):

    def __init__(self):
        self._amt = None
        self._app_remark = None
        self._bill_no = None
        self._open_id = None
        self._pay_item = None
        self._user_id = None

    @property
    def amt(self):
        return self._amt

    @amt.setter
    def amt(self, value):
        self._amt = value
    @property
    def app_remark(self):
        return self._app_remark

    @app_remark.setter
    def app_remark(self, value):
        self._app_remark = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pay_item(self):
        return self._pay_item

    @pay_item.setter
    def pay_item(self, value):
        self._pay_item = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amt:
            if hasattr(self.amt, 'to_alipay_dict'):
                params['amt'] = self.amt.to_alipay_dict()
            else:
                params['amt'] = self.amt
        if self.app_remark:
            if hasattr(self.app_remark, 'to_alipay_dict'):
                params['app_remark'] = self.app_remark.to_alipay_dict()
            else:
                params['app_remark'] = self.app_remark
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pay_item:
            if hasattr(self.pay_item, 'to_alipay_dict'):
                params['pay_item'] = self.pay_item.to_alipay_dict()
            else:
                params['pay_item'] = self.pay_item
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
        o = AlipayUserGamecenterCoinPayModel()
        if 'amt' in d:
            o.amt = d['amt']
        if 'app_remark' in d:
            o.app_remark = d['app_remark']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pay_item' in d:
            o.pay_item = d['pay_item']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


