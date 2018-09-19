#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PointAccountLog(object):

    def __init__(self):
        self._account_log_id = None
        self._balance = None
        self._order_no = None
        self._out_biz_no = None
        self._point_amount = None
        self._sub_trans_code = None
        self._sub_trans_code_cn = None
        self._trans_code = None
        self._trans_date = None
        self._trans_memo = None

    @property
    def account_log_id(self):
        return self._account_log_id

    @account_log_id.setter
    def account_log_id(self, value):
        self._account_log_id = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def point_amount(self):
        return self._point_amount

    @point_amount.setter
    def point_amount(self, value):
        self._point_amount = value
    @property
    def sub_trans_code(self):
        return self._sub_trans_code

    @sub_trans_code.setter
    def sub_trans_code(self, value):
        self._sub_trans_code = value
    @property
    def sub_trans_code_cn(self):
        return self._sub_trans_code_cn

    @sub_trans_code_cn.setter
    def sub_trans_code_cn(self, value):
        self._sub_trans_code_cn = value
    @property
    def trans_code(self):
        return self._trans_code

    @trans_code.setter
    def trans_code(self, value):
        self._trans_code = value
    @property
    def trans_date(self):
        return self._trans_date

    @trans_date.setter
    def trans_date(self, value):
        self._trans_date = value
    @property
    def trans_memo(self):
        return self._trans_memo

    @trans_memo.setter
    def trans_memo(self, value):
        self._trans_memo = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_log_id:
            if hasattr(self.account_log_id, 'to_alipay_dict'):
                params['account_log_id'] = self.account_log_id.to_alipay_dict()
            else:
                params['account_log_id'] = self.account_log_id
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.point_amount:
            if hasattr(self.point_amount, 'to_alipay_dict'):
                params['point_amount'] = self.point_amount.to_alipay_dict()
            else:
                params['point_amount'] = self.point_amount
        if self.sub_trans_code:
            if hasattr(self.sub_trans_code, 'to_alipay_dict'):
                params['sub_trans_code'] = self.sub_trans_code.to_alipay_dict()
            else:
                params['sub_trans_code'] = self.sub_trans_code
        if self.sub_trans_code_cn:
            if hasattr(self.sub_trans_code_cn, 'to_alipay_dict'):
                params['sub_trans_code_cn'] = self.sub_trans_code_cn.to_alipay_dict()
            else:
                params['sub_trans_code_cn'] = self.sub_trans_code_cn
        if self.trans_code:
            if hasattr(self.trans_code, 'to_alipay_dict'):
                params['trans_code'] = self.trans_code.to_alipay_dict()
            else:
                params['trans_code'] = self.trans_code
        if self.trans_date:
            if hasattr(self.trans_date, 'to_alipay_dict'):
                params['trans_date'] = self.trans_date.to_alipay_dict()
            else:
                params['trans_date'] = self.trans_date
        if self.trans_memo:
            if hasattr(self.trans_memo, 'to_alipay_dict'):
                params['trans_memo'] = self.trans_memo.to_alipay_dict()
            else:
                params['trans_memo'] = self.trans_memo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PointAccountLog()
        if 'account_log_id' in d:
            o.account_log_id = d['account_log_id']
        if 'balance' in d:
            o.balance = d['balance']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'point_amount' in d:
            o.point_amount = d['point_amount']
        if 'sub_trans_code' in d:
            o.sub_trans_code = d['sub_trans_code']
        if 'sub_trans_code_cn' in d:
            o.sub_trans_code_cn = d['sub_trans_code_cn']
        if 'trans_code' in d:
            o.trans_code = d['trans_code']
        if 'trans_date' in d:
            o.trans_date = d['trans_date']
        if 'trans_memo' in d:
            o.trans_memo = d['trans_memo']
        return o


