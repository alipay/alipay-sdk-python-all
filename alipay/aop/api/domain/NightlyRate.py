#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HotelPromotionDetail import HotelPromotionDetail


class NightlyRate(object):

    def __init__(self):
        self._add_bed = None
        self._basis = None
        self._breakfast = None
        self._cost = None
        self._date = None
        self._inventory = None
        self._member = None
        self._price_discount_value = None
        self._promotion_list = None
        self._promotion_tag = None
        self._promotion_type = None
        self._status = None

    @property
    def add_bed(self):
        return self._add_bed

    @add_bed.setter
    def add_bed(self, value):
        self._add_bed = value
    @property
    def basis(self):
        return self._basis

    @basis.setter
    def basis(self, value):
        self._basis = value
    @property
    def breakfast(self):
        return self._breakfast

    @breakfast.setter
    def breakfast(self, value):
        self._breakfast = value
    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def member(self):
        return self._member

    @member.setter
    def member(self, value):
        self._member = value
    @property
    def price_discount_value(self):
        return self._price_discount_value

    @price_discount_value.setter
    def price_discount_value(self, value):
        self._price_discount_value = value
    @property
    def promotion_list(self):
        return self._promotion_list

    @promotion_list.setter
    def promotion_list(self, value):
        if isinstance(value, list):
            self._promotion_list = list()
            for i in value:
                if isinstance(i, HotelPromotionDetail):
                    self._promotion_list.append(i)
                else:
                    self._promotion_list.append(HotelPromotionDetail.from_alipay_dict(i))
    @property
    def promotion_tag(self):
        return self._promotion_tag

    @promotion_tag.setter
    def promotion_tag(self, value):
        self._promotion_tag = value
    @property
    def promotion_type(self):
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self._promotion_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_bed:
            if hasattr(self.add_bed, 'to_alipay_dict'):
                params['add_bed'] = self.add_bed.to_alipay_dict()
            else:
                params['add_bed'] = self.add_bed
        if self.basis:
            if hasattr(self.basis, 'to_alipay_dict'):
                params['basis'] = self.basis.to_alipay_dict()
            else:
                params['basis'] = self.basis
        if self.breakfast:
            if hasattr(self.breakfast, 'to_alipay_dict'):
                params['breakfast'] = self.breakfast.to_alipay_dict()
            else:
                params['breakfast'] = self.breakfast
        if self.cost:
            if hasattr(self.cost, 'to_alipay_dict'):
                params['cost'] = self.cost.to_alipay_dict()
            else:
                params['cost'] = self.cost
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.member:
            if hasattr(self.member, 'to_alipay_dict'):
                params['member'] = self.member.to_alipay_dict()
            else:
                params['member'] = self.member
        if self.price_discount_value:
            if hasattr(self.price_discount_value, 'to_alipay_dict'):
                params['price_discount_value'] = self.price_discount_value.to_alipay_dict()
            else:
                params['price_discount_value'] = self.price_discount_value
        if self.promotion_list:
            if isinstance(self.promotion_list, list):
                for i in range(0, len(self.promotion_list)):
                    element = self.promotion_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promotion_list[i] = element.to_alipay_dict()
            if hasattr(self.promotion_list, 'to_alipay_dict'):
                params['promotion_list'] = self.promotion_list.to_alipay_dict()
            else:
                params['promotion_list'] = self.promotion_list
        if self.promotion_tag:
            if hasattr(self.promotion_tag, 'to_alipay_dict'):
                params['promotion_tag'] = self.promotion_tag.to_alipay_dict()
            else:
                params['promotion_tag'] = self.promotion_tag
        if self.promotion_type:
            if hasattr(self.promotion_type, 'to_alipay_dict'):
                params['promotion_type'] = self.promotion_type.to_alipay_dict()
            else:
                params['promotion_type'] = self.promotion_type
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
        o = NightlyRate()
        if 'add_bed' in d:
            o.add_bed = d['add_bed']
        if 'basis' in d:
            o.basis = d['basis']
        if 'breakfast' in d:
            o.breakfast = d['breakfast']
        if 'cost' in d:
            o.cost = d['cost']
        if 'date' in d:
            o.date = d['date']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'member' in d:
            o.member = d['member']
        if 'price_discount_value' in d:
            o.price_discount_value = d['price_discount_value']
        if 'promotion_list' in d:
            o.promotion_list = d['promotion_list']
        if 'promotion_tag' in d:
            o.promotion_tag = d['promotion_tag']
        if 'promotion_type' in d:
            o.promotion_type = d['promotion_type']
        if 'status' in d:
            o.status = d['status']
        return o


