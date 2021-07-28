#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StructureServiceInfo(object):

    def __init__(self):
        self._alcohol = None
        self._booking = None
        self._box = None
        self._byo = None
        self._chinese_svc = None
        self._parking = None
        self._takeout = None
        self._tel_rsvt = None
        self._tips = None
        self._wifi = None

    @property
    def alcohol(self):
        return self._alcohol

    @alcohol.setter
    def alcohol(self, value):
        self._alcohol = value
    @property
    def booking(self):
        return self._booking

    @booking.setter
    def booking(self, value):
        self._booking = value
    @property
    def box(self):
        return self._box

    @box.setter
    def box(self, value):
        self._box = value
    @property
    def byo(self):
        return self._byo

    @byo.setter
    def byo(self, value):
        self._byo = value
    @property
    def chinese_svc(self):
        return self._chinese_svc

    @chinese_svc.setter
    def chinese_svc(self, value):
        self._chinese_svc = value
    @property
    def parking(self):
        return self._parking

    @parking.setter
    def parking(self, value):
        self._parking = value
    @property
    def takeout(self):
        return self._takeout

    @takeout.setter
    def takeout(self, value):
        self._takeout = value
    @property
    def tel_rsvt(self):
        return self._tel_rsvt

    @tel_rsvt.setter
    def tel_rsvt(self, value):
        self._tel_rsvt = value
    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        self._tips = value
    @property
    def wifi(self):
        return self._wifi

    @wifi.setter
    def wifi(self, value):
        self._wifi = value


    def to_alipay_dict(self):
        params = dict()
        if self.alcohol:
            if hasattr(self.alcohol, 'to_alipay_dict'):
                params['alcohol'] = self.alcohol.to_alipay_dict()
            else:
                params['alcohol'] = self.alcohol
        if self.booking:
            if hasattr(self.booking, 'to_alipay_dict'):
                params['booking'] = self.booking.to_alipay_dict()
            else:
                params['booking'] = self.booking
        if self.box:
            if hasattr(self.box, 'to_alipay_dict'):
                params['box'] = self.box.to_alipay_dict()
            else:
                params['box'] = self.box
        if self.byo:
            if hasattr(self.byo, 'to_alipay_dict'):
                params['byo'] = self.byo.to_alipay_dict()
            else:
                params['byo'] = self.byo
        if self.chinese_svc:
            if hasattr(self.chinese_svc, 'to_alipay_dict'):
                params['chinese_svc'] = self.chinese_svc.to_alipay_dict()
            else:
                params['chinese_svc'] = self.chinese_svc
        if self.parking:
            if hasattr(self.parking, 'to_alipay_dict'):
                params['parking'] = self.parking.to_alipay_dict()
            else:
                params['parking'] = self.parking
        if self.takeout:
            if hasattr(self.takeout, 'to_alipay_dict'):
                params['takeout'] = self.takeout.to_alipay_dict()
            else:
                params['takeout'] = self.takeout
        if self.tel_rsvt:
            if hasattr(self.tel_rsvt, 'to_alipay_dict'):
                params['tel_rsvt'] = self.tel_rsvt.to_alipay_dict()
            else:
                params['tel_rsvt'] = self.tel_rsvt
        if self.tips:
            if hasattr(self.tips, 'to_alipay_dict'):
                params['tips'] = self.tips.to_alipay_dict()
            else:
                params['tips'] = self.tips
        if self.wifi:
            if hasattr(self.wifi, 'to_alipay_dict'):
                params['wifi'] = self.wifi.to_alipay_dict()
            else:
                params['wifi'] = self.wifi
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StructureServiceInfo()
        if 'alcohol' in d:
            o.alcohol = d['alcohol']
        if 'booking' in d:
            o.booking = d['booking']
        if 'box' in d:
            o.box = d['box']
        if 'byo' in d:
            o.byo = d['byo']
        if 'chinese_svc' in d:
            o.chinese_svc = d['chinese_svc']
        if 'parking' in d:
            o.parking = d['parking']
        if 'takeout' in d:
            o.takeout = d['takeout']
        if 'tel_rsvt' in d:
            o.tel_rsvt = d['tel_rsvt']
        if 'tips' in d:
            o.tips = d['tips']
        if 'wifi' in d:
            o.wifi = d['wifi']
        return o


