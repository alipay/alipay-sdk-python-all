#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PosDiscountDetail import PosDiscountDetail
from alipay.aop.api.domain.KbPosBillDishDetail import KbPosBillDishDetail
from alipay.aop.api.domain.PosBillPayChannel import PosBillPayChannel
from alipay.aop.api.domain.PosOrderKey import PosOrderKey


class KoubeiCateringOrderBillApplyModel(object):

    def __init__(self):
        self._bill_amount = None
        self._discount_details = None
        self._dish_details = None
        self._ext_info = None
        self._member_flag = None
        self._memo = None
        self._pay_amount = None
        self._pay_channels = None
        self._people_list = None
        self._pos_order_key = None
        self._receipt_amount = None
        self._settle_time = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def discount_details(self):
        return self._discount_details

    @discount_details.setter
    def discount_details(self, value):
        if isinstance(value, list):
            self._discount_details = list()
            for i in value:
                if isinstance(i, PosDiscountDetail):
                    self._discount_details.append(i)
                else:
                    self._discount_details.append(PosDiscountDetail.from_alipay_dict(i))
    @property
    def dish_details(self):
        return self._dish_details

    @dish_details.setter
    def dish_details(self, value):
        if isinstance(value, list):
            self._dish_details = list()
            for i in value:
                if isinstance(i, KbPosBillDishDetail):
                    self._dish_details.append(i)
                else:
                    self._dish_details.append(KbPosBillDishDetail.from_alipay_dict(i))
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def member_flag(self):
        return self._member_flag

    @member_flag.setter
    def member_flag(self, value):
        self._member_flag = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_channels(self):
        return self._pay_channels

    @pay_channels.setter
    def pay_channels(self, value):
        if isinstance(value, list):
            self._pay_channels = list()
            for i in value:
                if isinstance(i, PosBillPayChannel):
                    self._pay_channels.append(i)
                else:
                    self._pay_channels.append(PosBillPayChannel.from_alipay_dict(i))
    @property
    def people_list(self):
        return self._people_list

    @people_list.setter
    def people_list(self, value):
        self._people_list = value
    @property
    def pos_order_key(self):
        return self._pos_order_key

    @pos_order_key.setter
    def pos_order_key(self, value):
        if isinstance(value, PosOrderKey):
            self._pos_order_key = value
        else:
            self._pos_order_key = PosOrderKey.from_alipay_dict(value)
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def settle_time(self):
        return self._settle_time

    @settle_time.setter
    def settle_time(self, value):
        self._settle_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.discount_details:
            if isinstance(self.discount_details, list):
                for i in range(0, len(self.discount_details)):
                    element = self.discount_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_details[i] = element.to_alipay_dict()
            if hasattr(self.discount_details, 'to_alipay_dict'):
                params['discount_details'] = self.discount_details.to_alipay_dict()
            else:
                params['discount_details'] = self.discount_details
        if self.dish_details:
            if isinstance(self.dish_details, list):
                for i in range(0, len(self.dish_details)):
                    element = self.dish_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_details[i] = element.to_alipay_dict()
            if hasattr(self.dish_details, 'to_alipay_dict'):
                params['dish_details'] = self.dish_details.to_alipay_dict()
            else:
                params['dish_details'] = self.dish_details
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.member_flag:
            if hasattr(self.member_flag, 'to_alipay_dict'):
                params['member_flag'] = self.member_flag.to_alipay_dict()
            else:
                params['member_flag'] = self.member_flag
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_channels:
            if isinstance(self.pay_channels, list):
                for i in range(0, len(self.pay_channels)):
                    element = self.pay_channels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_channels[i] = element.to_alipay_dict()
            if hasattr(self.pay_channels, 'to_alipay_dict'):
                params['pay_channels'] = self.pay_channels.to_alipay_dict()
            else:
                params['pay_channels'] = self.pay_channels
        if self.people_list:
            if hasattr(self.people_list, 'to_alipay_dict'):
                params['people_list'] = self.people_list.to_alipay_dict()
            else:
                params['people_list'] = self.people_list
        if self.pos_order_key:
            if hasattr(self.pos_order_key, 'to_alipay_dict'):
                params['pos_order_key'] = self.pos_order_key.to_alipay_dict()
            else:
                params['pos_order_key'] = self.pos_order_key
        if self.receipt_amount:
            if hasattr(self.receipt_amount, 'to_alipay_dict'):
                params['receipt_amount'] = self.receipt_amount.to_alipay_dict()
            else:
                params['receipt_amount'] = self.receipt_amount
        if self.settle_time:
            if hasattr(self.settle_time, 'to_alipay_dict'):
                params['settle_time'] = self.settle_time.to_alipay_dict()
            else:
                params['settle_time'] = self.settle_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringOrderBillApplyModel()
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'discount_details' in d:
            o.discount_details = d['discount_details']
        if 'dish_details' in d:
            o.dish_details = d['dish_details']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'member_flag' in d:
            o.member_flag = d['member_flag']
        if 'memo' in d:
            o.memo = d['memo']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_channels' in d:
            o.pay_channels = d['pay_channels']
        if 'people_list' in d:
            o.people_list = d['people_list']
        if 'pos_order_key' in d:
            o.pos_order_key = d['pos_order_key']
        if 'receipt_amount' in d:
            o.receipt_amount = d['receipt_amount']
        if 'settle_time' in d:
            o.settle_time = d['settle_time']
        return o


