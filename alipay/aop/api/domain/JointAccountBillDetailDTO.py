#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JointAccountBillDetailDTO(object):

    def __init__(self):
        self._account_id = None
        self._amount = None
        self._biz_date = None
        self._biz_no = None
        self._in_out = None
        self._title = None
        self._user_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def in_out(self):
        return self._in_out

    @in_out.setter
    def in_out(self, value):
        self._in_out = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.in_out:
            if hasattr(self.in_out, 'to_alipay_dict'):
                params['in_out'] = self.in_out.to_alipay_dict()
            else:
                params['in_out'] = self.in_out
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
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
        o = JointAccountBillDetailDTO()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'in_out' in d:
            o.in_out = d['in_out']
        if 'title' in d:
            o.title = d['title']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


