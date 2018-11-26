#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopPosSchedule import ShopPosSchedule


class KoubeiCateringPosShiftSyncModel(object):

    def __init__(self):
        self._schedules = None
        self._shop_id = None

    @property
    def schedules(self):
        return self._schedules

    @schedules.setter
    def schedules(self, value):
        if isinstance(value, list):
            self._schedules = list()
            for i in value:
                if isinstance(i, ShopPosSchedule):
                    self._schedules.append(i)
                else:
                    self._schedules.append(ShopPosSchedule.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.schedules:
            if isinstance(self.schedules, list):
                for i in range(0, len(self.schedules)):
                    element = self.schedules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.schedules[i] = element.to_alipay_dict()
            if hasattr(self.schedules, 'to_alipay_dict'):
                params['schedules'] = self.schedules.to_alipay_dict()
            else:
                params['schedules'] = self.schedules
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosShiftSyncModel()
        if 'schedules' in d:
            o.schedules = d['schedules']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


