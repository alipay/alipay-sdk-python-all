#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BillFeeInfo import BillFeeInfo


class MoneyCardUseRecordDetail(object):

    def __init__(self):
        self._amount = None
        self._bill_fee_info_list = None
        self._biz_type = None
        self._card_id = None
        self._cash = None
        self._create_time = None
        self._open_id = None
        self._order_id = None
        self._owner_open_id = None
        self._owner_uid = None
        self._trade_no = None
        self._trade_pid = None
        self._use_shop_id = None
        self._use_shop_name = None
        self._use_shop_note = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bill_fee_info_list(self):
        return self._bill_fee_info_list

    @bill_fee_info_list.setter
    def bill_fee_info_list(self, value):
        if isinstance(value, list):
            self._bill_fee_info_list = list()
            for i in value:
                if isinstance(i, BillFeeInfo):
                    self._bill_fee_info_list.append(i)
                else:
                    self._bill_fee_info_list.append(BillFeeInfo.from_alipay_dict(i))
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):
        self._cash = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
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
    def owner_open_id(self):
        return self._owner_open_id

    @owner_open_id.setter
    def owner_open_id(self, value):
        self._owner_open_id = value
    @property
    def owner_uid(self):
        return self._owner_uid

    @owner_uid.setter
    def owner_uid(self, value):
        self._owner_uid = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_pid(self):
        return self._trade_pid

    @trade_pid.setter
    def trade_pid(self, value):
        self._trade_pid = value
    @property
    def use_shop_id(self):
        return self._use_shop_id

    @use_shop_id.setter
    def use_shop_id(self, value):
        self._use_shop_id = value
    @property
    def use_shop_name(self):
        return self._use_shop_name

    @use_shop_name.setter
    def use_shop_name(self, value):
        self._use_shop_name = value
    @property
    def use_shop_note(self):
        return self._use_shop_note

    @use_shop_note.setter
    def use_shop_note(self, value):
        self._use_shop_note = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bill_fee_info_list:
            if isinstance(self.bill_fee_info_list, list):
                for i in range(0, len(self.bill_fee_info_list)):
                    element = self.bill_fee_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_fee_info_list[i] = element.to_alipay_dict()
            if hasattr(self.bill_fee_info_list, 'to_alipay_dict'):
                params['bill_fee_info_list'] = self.bill_fee_info_list.to_alipay_dict()
            else:
                params['bill_fee_info_list'] = self.bill_fee_info_list
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.cash:
            if hasattr(self.cash, 'to_alipay_dict'):
                params['cash'] = self.cash.to_alipay_dict()
            else:
                params['cash'] = self.cash
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
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
        if self.owner_open_id:
            if hasattr(self.owner_open_id, 'to_alipay_dict'):
                params['owner_open_id'] = self.owner_open_id.to_alipay_dict()
            else:
                params['owner_open_id'] = self.owner_open_id
        if self.owner_uid:
            if hasattr(self.owner_uid, 'to_alipay_dict'):
                params['owner_uid'] = self.owner_uid.to_alipay_dict()
            else:
                params['owner_uid'] = self.owner_uid
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_pid:
            if hasattr(self.trade_pid, 'to_alipay_dict'):
                params['trade_pid'] = self.trade_pid.to_alipay_dict()
            else:
                params['trade_pid'] = self.trade_pid
        if self.use_shop_id:
            if hasattr(self.use_shop_id, 'to_alipay_dict'):
                params['use_shop_id'] = self.use_shop_id.to_alipay_dict()
            else:
                params['use_shop_id'] = self.use_shop_id
        if self.use_shop_name:
            if hasattr(self.use_shop_name, 'to_alipay_dict'):
                params['use_shop_name'] = self.use_shop_name.to_alipay_dict()
            else:
                params['use_shop_name'] = self.use_shop_name
        if self.use_shop_note:
            if hasattr(self.use_shop_note, 'to_alipay_dict'):
                params['use_shop_note'] = self.use_shop_note.to_alipay_dict()
            else:
                params['use_shop_note'] = self.use_shop_note
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
        o = MoneyCardUseRecordDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'bill_fee_info_list' in d:
            o.bill_fee_info_list = d['bill_fee_info_list']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'cash' in d:
            o.cash = d['cash']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'owner_open_id' in d:
            o.owner_open_id = d['owner_open_id']
        if 'owner_uid' in d:
            o.owner_uid = d['owner_uid']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_pid' in d:
            o.trade_pid = d['trade_pid']
        if 'use_shop_id' in d:
            o.use_shop_id = d['use_shop_id']
        if 'use_shop_name' in d:
            o.use_shop_name = d['use_shop_name']
        if 'use_shop_note' in d:
            o.use_shop_note = d['use_shop_note']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


