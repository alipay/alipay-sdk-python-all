#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineTrade(object):

    def __init__(self):
        self._actual_order_time = None
        self._amount = None
        self._card_type = None
        self._order_biz_context = None
        self._out_trade_no = None
        self._records = None
        self._seller_login_name = None
        self._subject = None
        self._user_id = None

    @property
    def actual_order_time(self):
        return self._actual_order_time

    @actual_order_time.setter
    def actual_order_time(self, value):
        self._actual_order_time = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def order_biz_context(self):
        return self._order_biz_context

    @order_biz_context.setter
    def order_biz_context(self, value):
        self._order_biz_context = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        if isinstance(value, list):
            self._records = list()
            for i in value:
                self._records.append(i)
    @property
    def seller_login_name(self):
        return self._seller_login_name

    @seller_login_name.setter
    def seller_login_name(self, value):
        self._seller_login_name = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_order_time:
            if hasattr(self.actual_order_time, 'to_alipay_dict'):
                params['actual_order_time'] = self.actual_order_time.to_alipay_dict()
            else:
                params['actual_order_time'] = self.actual_order_time
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.order_biz_context:
            if hasattr(self.order_biz_context, 'to_alipay_dict'):
                params['order_biz_context'] = self.order_biz_context.to_alipay_dict()
            else:
                params['order_biz_context'] = self.order_biz_context
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.records:
            if isinstance(self.records, list):
                for i in range(0, len(self.records)):
                    element = self.records[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.records[i] = element.to_alipay_dict()
            if hasattr(self.records, 'to_alipay_dict'):
                params['records'] = self.records.to_alipay_dict()
            else:
                params['records'] = self.records
        if self.seller_login_name:
            if hasattr(self.seller_login_name, 'to_alipay_dict'):
                params['seller_login_name'] = self.seller_login_name.to_alipay_dict()
            else:
                params['seller_login_name'] = self.seller_login_name
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
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
        o = AlipayOfflineTrade()
        if 'actual_order_time' in d:
            o.actual_order_time = d['actual_order_time']
        if 'amount' in d:
            o.amount = d['amount']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'order_biz_context' in d:
            o.order_biz_context = d['order_biz_context']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'records' in d:
            o.records = d['records']
        if 'seller_login_name' in d:
            o.seller_login_name = d['seller_login_name']
        if 'subject' in d:
            o.subject = d['subject']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


