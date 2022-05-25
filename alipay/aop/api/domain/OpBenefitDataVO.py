#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpBenefitDataVO(object):

    def __init__(self):
        self._benefit_logo = None
        self._benefit_main_title = None
        self._benefit_merchant_name = None
        self._benefit_sub_title = None
        self._brand_logo = None
        self._distance_desc = None
        self._floor_amount = None
        self._prize = None
        self._prize_unit = None
        self._status = None

    @property
    def benefit_logo(self):
        return self._benefit_logo

    @benefit_logo.setter
    def benefit_logo(self, value):
        self._benefit_logo = value
    @property
    def benefit_main_title(self):
        return self._benefit_main_title

    @benefit_main_title.setter
    def benefit_main_title(self, value):
        self._benefit_main_title = value
    @property
    def benefit_merchant_name(self):
        return self._benefit_merchant_name

    @benefit_merchant_name.setter
    def benefit_merchant_name(self, value):
        self._benefit_merchant_name = value
    @property
    def benefit_sub_title(self):
        return self._benefit_sub_title

    @benefit_sub_title.setter
    def benefit_sub_title(self, value):
        self._benefit_sub_title = value
    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        self._brand_logo = value
    @property
    def distance_desc(self):
        return self._distance_desc

    @distance_desc.setter
    def distance_desc(self, value):
        self._distance_desc = value
    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        self._floor_amount = value
    @property
    def prize(self):
        return self._prize

    @prize.setter
    def prize(self, value):
        self._prize = value
    @property
    def prize_unit(self):
        return self._prize_unit

    @prize_unit.setter
    def prize_unit(self, value):
        self._prize_unit = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_logo:
            if hasattr(self.benefit_logo, 'to_alipay_dict'):
                params['benefit_logo'] = self.benefit_logo.to_alipay_dict()
            else:
                params['benefit_logo'] = self.benefit_logo
        if self.benefit_main_title:
            if hasattr(self.benefit_main_title, 'to_alipay_dict'):
                params['benefit_main_title'] = self.benefit_main_title.to_alipay_dict()
            else:
                params['benefit_main_title'] = self.benefit_main_title
        if self.benefit_merchant_name:
            if hasattr(self.benefit_merchant_name, 'to_alipay_dict'):
                params['benefit_merchant_name'] = self.benefit_merchant_name.to_alipay_dict()
            else:
                params['benefit_merchant_name'] = self.benefit_merchant_name
        if self.benefit_sub_title:
            if hasattr(self.benefit_sub_title, 'to_alipay_dict'):
                params['benefit_sub_title'] = self.benefit_sub_title.to_alipay_dict()
            else:
                params['benefit_sub_title'] = self.benefit_sub_title
        if self.brand_logo:
            if hasattr(self.brand_logo, 'to_alipay_dict'):
                params['brand_logo'] = self.brand_logo.to_alipay_dict()
            else:
                params['brand_logo'] = self.brand_logo
        if self.distance_desc:
            if hasattr(self.distance_desc, 'to_alipay_dict'):
                params['distance_desc'] = self.distance_desc.to_alipay_dict()
            else:
                params['distance_desc'] = self.distance_desc
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
        if self.prize:
            if hasattr(self.prize, 'to_alipay_dict'):
                params['prize'] = self.prize.to_alipay_dict()
            else:
                params['prize'] = self.prize
        if self.prize_unit:
            if hasattr(self.prize_unit, 'to_alipay_dict'):
                params['prize_unit'] = self.prize_unit.to_alipay_dict()
            else:
                params['prize_unit'] = self.prize_unit
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
        o = OpBenefitDataVO()
        if 'benefit_logo' in d:
            o.benefit_logo = d['benefit_logo']
        if 'benefit_main_title' in d:
            o.benefit_main_title = d['benefit_main_title']
        if 'benefit_merchant_name' in d:
            o.benefit_merchant_name = d['benefit_merchant_name']
        if 'benefit_sub_title' in d:
            o.benefit_sub_title = d['benefit_sub_title']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'distance_desc' in d:
            o.distance_desc = d['distance_desc']
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        if 'prize' in d:
            o.prize = d['prize']
        if 'prize_unit' in d:
            o.prize_unit = d['prize_unit']
        if 'status' in d:
            o.status = d['status']
        return o


