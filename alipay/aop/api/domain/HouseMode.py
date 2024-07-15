#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HouseMode(object):

    def __init__(self):
        self._cook_num = None
        self._desc = None
        self._fee = None
        self._floorage = None
        self._hall_num = None
        self._pic_url = None
        self._room_num = None
        self._toilet_num = None

    @property
    def cook_num(self):
        return self._cook_num

    @cook_num.setter
    def cook_num(self, value):
        self._cook_num = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value
    @property
    def floorage(self):
        return self._floorage

    @floorage.setter
    def floorage(self, value):
        self._floorage = value
    @property
    def hall_num(self):
        return self._hall_num

    @hall_num.setter
    def hall_num(self, value):
        self._hall_num = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def room_num(self):
        return self._room_num

    @room_num.setter
    def room_num(self, value):
        self._room_num = value
    @property
    def toilet_num(self):
        return self._toilet_num

    @toilet_num.setter
    def toilet_num(self, value):
        self._toilet_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.cook_num:
            if hasattr(self.cook_num, 'to_alipay_dict'):
                params['cook_num'] = self.cook_num.to_alipay_dict()
            else:
                params['cook_num'] = self.cook_num
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.fee:
            if hasattr(self.fee, 'to_alipay_dict'):
                params['fee'] = self.fee.to_alipay_dict()
            else:
                params['fee'] = self.fee
        if self.floorage:
            if hasattr(self.floorage, 'to_alipay_dict'):
                params['floorage'] = self.floorage.to_alipay_dict()
            else:
                params['floorage'] = self.floorage
        if self.hall_num:
            if hasattr(self.hall_num, 'to_alipay_dict'):
                params['hall_num'] = self.hall_num.to_alipay_dict()
            else:
                params['hall_num'] = self.hall_num
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.room_num:
            if hasattr(self.room_num, 'to_alipay_dict'):
                params['room_num'] = self.room_num.to_alipay_dict()
            else:
                params['room_num'] = self.room_num
        if self.toilet_num:
            if hasattr(self.toilet_num, 'to_alipay_dict'):
                params['toilet_num'] = self.toilet_num.to_alipay_dict()
            else:
                params['toilet_num'] = self.toilet_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HouseMode()
        if 'cook_num' in d:
            o.cook_num = d['cook_num']
        if 'desc' in d:
            o.desc = d['desc']
        if 'fee' in d:
            o.fee = d['fee']
        if 'floorage' in d:
            o.floorage = d['floorage']
        if 'hall_num' in d:
            o.hall_num = d['hall_num']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'room_num' in d:
            o.room_num = d['room_num']
        if 'toilet_num' in d:
            o.toilet_num = d['toilet_num']
        return o


