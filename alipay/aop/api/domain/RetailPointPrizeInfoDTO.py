#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RetailPointPrizeInfoDTO(object):

    def __init__(self):
        self._discount_amount = None
        self._discount_amount_unit = None
        self._floor_amount = None
        self._join_limit = None
        self._nfc_pay = None
        self._point_count = None
        self._prize_id = None
        self._prize_name = None
        self._prize_type = None
        self._remaining_join_count = None
        self._retail_activity_id = None
        self._status = None

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_amount_unit(self):
        return self._discount_amount_unit

    @discount_amount_unit.setter
    def discount_amount_unit(self, value):
        self._discount_amount_unit = value
    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        self._floor_amount = value
    @property
    def join_limit(self):
        return self._join_limit

    @join_limit.setter
    def join_limit(self, value):
        self._join_limit = value
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
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def remaining_join_count(self):
        return self._remaining_join_count

    @remaining_join_count.setter
    def remaining_join_count(self, value):
        self._remaining_join_count = value
    @property
    def retail_activity_id(self):
        return self._retail_activity_id

    @retail_activity_id.setter
    def retail_activity_id(self, value):
        self._retail_activity_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_amount_unit:
            if hasattr(self.discount_amount_unit, 'to_alipay_dict'):
                params['discount_amount_unit'] = self.discount_amount_unit.to_alipay_dict()
            else:
                params['discount_amount_unit'] = self.discount_amount_unit
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
        if self.join_limit:
            if hasattr(self.join_limit, 'to_alipay_dict'):
                params['join_limit'] = self.join_limit.to_alipay_dict()
            else:
                params['join_limit'] = self.join_limit
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
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        if self.remaining_join_count:
            if hasattr(self.remaining_join_count, 'to_alipay_dict'):
                params['remaining_join_count'] = self.remaining_join_count.to_alipay_dict()
            else:
                params['remaining_join_count'] = self.remaining_join_count
        if self.retail_activity_id:
            if hasattr(self.retail_activity_id, 'to_alipay_dict'):
                params['retail_activity_id'] = self.retail_activity_id.to_alipay_dict()
            else:
                params['retail_activity_id'] = self.retail_activity_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RetailPointPrizeInfoDTO()
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_amount_unit' in d:
            o.discount_amount_unit = d['discount_amount_unit']
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        if 'join_limit' in d:
            o.join_limit = d['join_limit']
        if 'nfc_pay' in d:
            o.nfc_pay = d['nfc_pay']
        if 'point_count' in d:
            o.point_count = d['point_count']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'remaining_join_count' in d:
            o.remaining_join_count = d['remaining_join_count']
        if 'retail_activity_id' in d:
            o.retail_activity_id = d['retail_activity_id']
        if 'status' in d:
            o.status = d['status']
        return o


