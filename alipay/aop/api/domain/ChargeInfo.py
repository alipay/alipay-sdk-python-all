#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubFee import SubFee


class ChargeInfo(object):

    def __init__(self):
        self._charge_fee = None
        self._charge_type = None
        self._is_rating_on_switch = None
        self._is_rating_on_trade_receiver = None
        self._original_charge_fee = None
        self._sub_fee_detail_list = None
        self._switch_fee_rate = None

    @property
    def charge_fee(self):
        return self._charge_fee

    @charge_fee.setter
    def charge_fee(self, value):
        self._charge_fee = value
    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def is_rating_on_switch(self):
        return self._is_rating_on_switch

    @is_rating_on_switch.setter
    def is_rating_on_switch(self, value):
        self._is_rating_on_switch = value
    @property
    def is_rating_on_trade_receiver(self):
        return self._is_rating_on_trade_receiver

    @is_rating_on_trade_receiver.setter
    def is_rating_on_trade_receiver(self, value):
        self._is_rating_on_trade_receiver = value
    @property
    def original_charge_fee(self):
        return self._original_charge_fee

    @original_charge_fee.setter
    def original_charge_fee(self, value):
        self._original_charge_fee = value
    @property
    def sub_fee_detail_list(self):
        return self._sub_fee_detail_list

    @sub_fee_detail_list.setter
    def sub_fee_detail_list(self, value):
        if isinstance(value, list):
            self._sub_fee_detail_list = list()
            for i in value:
                if isinstance(i, SubFee):
                    self._sub_fee_detail_list.append(i)
                else:
                    self._sub_fee_detail_list.append(SubFee.from_alipay_dict(i))
    @property
    def switch_fee_rate(self):
        return self._switch_fee_rate

    @switch_fee_rate.setter
    def switch_fee_rate(self, value):
        self._switch_fee_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_fee:
            if hasattr(self.charge_fee, 'to_alipay_dict'):
                params['charge_fee'] = self.charge_fee.to_alipay_dict()
            else:
                params['charge_fee'] = self.charge_fee
        if self.charge_type:
            if hasattr(self.charge_type, 'to_alipay_dict'):
                params['charge_type'] = self.charge_type.to_alipay_dict()
            else:
                params['charge_type'] = self.charge_type
        if self.is_rating_on_switch:
            if hasattr(self.is_rating_on_switch, 'to_alipay_dict'):
                params['is_rating_on_switch'] = self.is_rating_on_switch.to_alipay_dict()
            else:
                params['is_rating_on_switch'] = self.is_rating_on_switch
        if self.is_rating_on_trade_receiver:
            if hasattr(self.is_rating_on_trade_receiver, 'to_alipay_dict'):
                params['is_rating_on_trade_receiver'] = self.is_rating_on_trade_receiver.to_alipay_dict()
            else:
                params['is_rating_on_trade_receiver'] = self.is_rating_on_trade_receiver
        if self.original_charge_fee:
            if hasattr(self.original_charge_fee, 'to_alipay_dict'):
                params['original_charge_fee'] = self.original_charge_fee.to_alipay_dict()
            else:
                params['original_charge_fee'] = self.original_charge_fee
        if self.sub_fee_detail_list:
            if isinstance(self.sub_fee_detail_list, list):
                for i in range(0, len(self.sub_fee_detail_list)):
                    element = self.sub_fee_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_fee_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_fee_detail_list, 'to_alipay_dict'):
                params['sub_fee_detail_list'] = self.sub_fee_detail_list.to_alipay_dict()
            else:
                params['sub_fee_detail_list'] = self.sub_fee_detail_list
        if self.switch_fee_rate:
            if hasattr(self.switch_fee_rate, 'to_alipay_dict'):
                params['switch_fee_rate'] = self.switch_fee_rate.to_alipay_dict()
            else:
                params['switch_fee_rate'] = self.switch_fee_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChargeInfo()
        if 'charge_fee' in d:
            o.charge_fee = d['charge_fee']
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'is_rating_on_switch' in d:
            o.is_rating_on_switch = d['is_rating_on_switch']
        if 'is_rating_on_trade_receiver' in d:
            o.is_rating_on_trade_receiver = d['is_rating_on_trade_receiver']
        if 'original_charge_fee' in d:
            o.original_charge_fee = d['original_charge_fee']
        if 'sub_fee_detail_list' in d:
            o.sub_fee_detail_list = d['sub_fee_detail_list']
        if 'switch_fee_rate' in d:
            o.switch_fee_rate = d['switch_fee_rate']
        return o


