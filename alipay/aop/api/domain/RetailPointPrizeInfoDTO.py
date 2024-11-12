#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RetailPointPrizeInfoDTO(object):

    def __init__(self):
        self._discount_amount = None
        self._floor_amount = None
        self._nfc_pay = None
        self._point_count = None
        self._prize_id = None
        self._prize_name = None
        self._retail_activity_id = None

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        self._floor_amount = value
    @property
    def nfc_pay(self):
        return self._nfc_pay

    @nfc_pay.setter
    def nfc_pay(self, value):
        self._nfc_pay = value
    @property
    def point_count(self):
        return self._point_count

    @point_count.setter
    def point_count(self, value):
        self._point_count = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def retail_activity_id(self):
        return self._retail_activity_id

    @retail_activity_id.setter
    def retail_activity_id(self, value):
        self._retail_activity_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
        if self.nfc_pay:
            if hasattr(self.nfc_pay, 'to_alipay_dict'):
                params['nfc_pay'] = self.nfc_pay.to_alipay_dict()
            else:
                params['nfc_pay'] = self.nfc_pay
        if self.point_count:
            if hasattr(self.point_count, 'to_alipay_dict'):
                params['point_count'] = self.point_count.to_alipay_dict()
            else:
                params['point_count'] = self.point_count
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.retail_activity_id:
            if hasattr(self.retail_activity_id, 'to_alipay_dict'):
                params['retail_activity_id'] = self.retail_activity_id.to_alipay_dict()
            else:
                params['retail_activity_id'] = self.retail_activity_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RetailPointPrizeInfoDTO()
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        if 'nfc_pay' in d:
            o.nfc_pay = d['nfc_pay']
        if 'point_count' in d:
            o.point_count = d['point_count']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'retail_activity_id' in d:
            o.retail_activity_id = d['retail_activity_id']
        return o


