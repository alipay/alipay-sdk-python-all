#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiscountByDayModel import DiscountByDayModel
from alipay.aop.api.domain.DiscountModel import DiscountModel


class PrizeModel(object):

    def __init__(self):
        self._active_time = None
        self._available_amount = None
        self._available_count = None
        self._description = None
        self._discount_by_day_list = None
        self._discount_list = None
        self._expired_time = None
        self._ext_info = None
        self._name = None
        self._prize_id = None
        self._status = None
        self._total_amount = None
        self._type = None
        self._used_count = None

    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def available_count(self):
        return self._available_count

    @available_count.setter
    def available_count(self, value):
        self._available_count = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def discount_by_day_list(self):
        return self._discount_by_day_list

    @discount_by_day_list.setter
    def discount_by_day_list(self, value):
        if isinstance(value, list):
            self._discount_by_day_list = list()
            for i in value:
                if isinstance(i, DiscountByDayModel):
                    self._discount_by_day_list.append(i)
                else:
                    self._discount_by_day_list.append(DiscountByDayModel.from_alipay_dict(i))
    @property
    def discount_list(self):
        return self._discount_list

    @discount_list.setter
    def discount_list(self, value):
        if isinstance(value, list):
            self._discount_list = list()
            for i in value:
                if isinstance(i, DiscountModel):
                    self._discount_list.append(i)
                else:
                    self._discount_list.append(DiscountModel.from_alipay_dict(i))
    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def used_count(self):
        return self._used_count

    @used_count.setter
    def used_count(self, value):
        self._used_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
        if self.available_amount:
            if hasattr(self.available_amount, 'to_alipay_dict'):
                params['available_amount'] = self.available_amount.to_alipay_dict()
            else:
                params['available_amount'] = self.available_amount
        if self.available_count:
            if hasattr(self.available_count, 'to_alipay_dict'):
                params['available_count'] = self.available_count.to_alipay_dict()
            else:
                params['available_count'] = self.available_count
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.discount_by_day_list:
            if isinstance(self.discount_by_day_list, list):
                for i in range(0, len(self.discount_by_day_list)):
                    element = self.discount_by_day_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_by_day_list[i] = element.to_alipay_dict()
            if hasattr(self.discount_by_day_list, 'to_alipay_dict'):
                params['discount_by_day_list'] = self.discount_by_day_list.to_alipay_dict()
            else:
                params['discount_by_day_list'] = self.discount_by_day_list
        if self.discount_list:
            if isinstance(self.discount_list, list):
                for i in range(0, len(self.discount_list)):
                    element = self.discount_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_list[i] = element.to_alipay_dict()
            if hasattr(self.discount_list, 'to_alipay_dict'):
                params['discount_list'] = self.discount_list.to_alipay_dict()
            else:
                params['discount_list'] = self.discount_list
        if self.expired_time:
            if hasattr(self.expired_time, 'to_alipay_dict'):
                params['expired_time'] = self.expired_time.to_alipay_dict()
            else:
                params['expired_time'] = self.expired_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.used_count:
            if hasattr(self.used_count, 'to_alipay_dict'):
                params['used_count'] = self.used_count.to_alipay_dict()
            else:
                params['used_count'] = self.used_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrizeModel()
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'available_amount' in d:
            o.available_amount = d['available_amount']
        if 'available_count' in d:
            o.available_count = d['available_count']
        if 'description' in d:
            o.description = d['description']
        if 'discount_by_day_list' in d:
            o.discount_by_day_list = d['discount_by_day_list']
        if 'discount_list' in d:
            o.discount_list = d['discount_list']
        if 'expired_time' in d:
            o.expired_time = d['expired_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'name' in d:
            o.name = d['name']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'status' in d:
            o.status = d['status']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'type' in d:
            o.type = d['type']
        if 'used_count' in d:
            o.used_count = d['used_count']
        return o


