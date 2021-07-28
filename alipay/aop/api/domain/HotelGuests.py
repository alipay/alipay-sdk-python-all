#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HotelGuests(object):

    def __init__(self):
        self._guest_name = None
        self._member_level = None
        self._telephone = None

    @property
    def guest_name(self):
        return self._guest_name

    @guest_name.setter
    def guest_name(self, value):
        self._guest_name = value
    @property
    def member_level(self):
        return self._member_level

    @member_level.setter
    def member_level(self, value):
        self._member_level = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value


    def to_alipay_dict(self):
        params = dict()
        if self.guest_name:
            if hasattr(self.guest_name, 'to_alipay_dict'):
                params['guest_name'] = self.guest_name.to_alipay_dict()
            else:
                params['guest_name'] = self.guest_name
        if self.member_level:
            if hasattr(self.member_level, 'to_alipay_dict'):
                params['member_level'] = self.member_level.to_alipay_dict()
            else:
                params['member_level'] = self.member_level
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HotelGuests()
        if 'guest_name' in d:
            o.guest_name = d['guest_name']
        if 'member_level' in d:
            o.member_level = d['member_level']
        if 'telephone' in d:
            o.telephone = d['telephone']
        return o


