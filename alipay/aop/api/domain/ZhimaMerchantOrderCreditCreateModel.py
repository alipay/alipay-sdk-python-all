#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantOrderCreditCreateModel(object):

    def __init__(self):
        self._amount = None
        self._category = None
        self._channel = None
        self._deposit = None
        self._from_channel = None
        self._item_id = None
        self._order_process_url = None
        self._out_order_no = None
        self._overdue_time = None
        self._subject = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def deposit(self):
        return self._deposit

    @deposit.setter
    def deposit(self, value):
        self._deposit = value
    @property
    def from_channel(self):
        return self._from_channel

    @from_channel.setter
    def from_channel(self, value):
        self._from_channel = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def order_process_url(self):
        return self._order_process_url

    @order_process_url.setter
    def order_process_url(self, value):
        self._order_process_url = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def overdue_time(self):
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, value):
        self._overdue_time = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.deposit:
            if hasattr(self.deposit, 'to_alipay_dict'):
                params['deposit'] = self.deposit.to_alipay_dict()
            else:
                params['deposit'] = self.deposit
        if self.from_channel:
            if hasattr(self.from_channel, 'to_alipay_dict'):
                params['from_channel'] = self.from_channel.to_alipay_dict()
            else:
                params['from_channel'] = self.from_channel
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.order_process_url:
            if hasattr(self.order_process_url, 'to_alipay_dict'):
                params['order_process_url'] = self.order_process_url.to_alipay_dict()
            else:
                params['order_process_url'] = self.order_process_url
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.overdue_time:
            if hasattr(self.overdue_time, 'to_alipay_dict'):
                params['overdue_time'] = self.overdue_time.to_alipay_dict()
            else:
                params['overdue_time'] = self.overdue_time
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantOrderCreditCreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'category' in d:
            o.category = d['category']
        if 'channel' in d:
            o.channel = d['channel']
        if 'deposit' in d:
            o.deposit = d['deposit']
        if 'from_channel' in d:
            o.from_channel = d['from_channel']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'order_process_url' in d:
            o.order_process_url = d['order_process_url']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'overdue_time' in d:
            o.overdue_time = d['overdue_time']
        if 'subject' in d:
            o.subject = d['subject']
        return o


