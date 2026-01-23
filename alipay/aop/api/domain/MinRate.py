#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MinRate(object):

    def __init__(self):
        self._basis = None
        self._breakfast_meal_count = None
        self._cancel_policy = None
        self._confirm_minutes = None
        self._member = None
        self._order_type = None
        self._room_id = None

    @property
    def basis(self):
        return self._basis

    @basis.setter
    def basis(self, value):
        self._basis = value
    @property
    def breakfast_meal_count(self):
        return self._breakfast_meal_count

    @breakfast_meal_count.setter
    def breakfast_meal_count(self, value):
        self._breakfast_meal_count = value
    @property
    def cancel_policy(self):
        return self._cancel_policy

    @cancel_policy.setter
    def cancel_policy(self, value):
        self._cancel_policy = value
    @property
    def confirm_minutes(self):
        return self._confirm_minutes

    @confirm_minutes.setter
    def confirm_minutes(self, value):
        self._confirm_minutes = value
    @property
    def member(self):
        return self._member

    @member.setter
    def member(self, value):
        self._member = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.basis:
            if hasattr(self.basis, 'to_alipay_dict'):
                params['basis'] = self.basis.to_alipay_dict()
            else:
                params['basis'] = self.basis
        if self.breakfast_meal_count:
            if hasattr(self.breakfast_meal_count, 'to_alipay_dict'):
                params['breakfast_meal_count'] = self.breakfast_meal_count.to_alipay_dict()
            else:
                params['breakfast_meal_count'] = self.breakfast_meal_count
        if self.cancel_policy:
            if hasattr(self.cancel_policy, 'to_alipay_dict'):
                params['cancel_policy'] = self.cancel_policy.to_alipay_dict()
            else:
                params['cancel_policy'] = self.cancel_policy
        if self.confirm_minutes:
            if hasattr(self.confirm_minutes, 'to_alipay_dict'):
                params['confirm_minutes'] = self.confirm_minutes.to_alipay_dict()
            else:
                params['confirm_minutes'] = self.confirm_minutes
        if self.member:
            if hasattr(self.member, 'to_alipay_dict'):
                params['member'] = self.member.to_alipay_dict()
            else:
                params['member'] = self.member
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.room_id:
            if hasattr(self.room_id, 'to_alipay_dict'):
                params['room_id'] = self.room_id.to_alipay_dict()
            else:
                params['room_id'] = self.room_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MinRate()
        if 'basis' in d:
            o.basis = d['basis']
        if 'breakfast_meal_count' in d:
            o.breakfast_meal_count = d['breakfast_meal_count']
        if 'cancel_policy' in d:
            o.cancel_policy = d['cancel_policy']
        if 'confirm_minutes' in d:
            o.confirm_minutes = d['confirm_minutes']
        if 'member' in d:
            o.member = d['member']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'room_id' in d:
            o.room_id = d['room_id']
        return o


