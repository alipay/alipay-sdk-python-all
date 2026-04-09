#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HotelThemeVO import HotelThemeVO


class AlipayCommerceHotelBasicinfoSetModel(object):

    def __init__(self):
        self._enable_member = None
        self._hotel_code = None
        self._hotel_group_code = None
        self._hotel_name = None
        self._registration_agreement = None
        self._registration_sub_title = None
        self._room_no_pattern_type = None
        self._theme = None

    @property
    def enable_member(self):
        return self._enable_member

    @enable_member.setter
    def enable_member(self, value):
        self._enable_member = value
    @property
    def hotel_code(self):
        return self._hotel_code

    @hotel_code.setter
    def hotel_code(self, value):
        self._hotel_code = value
    @property
    def hotel_group_code(self):
        return self._hotel_group_code

    @hotel_group_code.setter
    def hotel_group_code(self, value):
        self._hotel_group_code = value
    @property
    def hotel_name(self):
        return self._hotel_name

    @hotel_name.setter
    def hotel_name(self, value):
        self._hotel_name = value
    @property
    def registration_agreement(self):
        return self._registration_agreement

    @registration_agreement.setter
    def registration_agreement(self, value):
        if isinstance(value, list):
            self._registration_agreement = list()
            for i in value:
                self._registration_agreement.append(i)
    @property
    def registration_sub_title(self):
        return self._registration_sub_title

    @registration_sub_title.setter
    def registration_sub_title(self, value):
        self._registration_sub_title = value
    @property
    def room_no_pattern_type(self):
        return self._room_no_pattern_type

    @room_no_pattern_type.setter
    def room_no_pattern_type(self, value):
        self._room_no_pattern_type = value
    @property
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, value):
        if isinstance(value, HotelThemeVO):
            self._theme = value
        else:
            self._theme = HotelThemeVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.enable_member:
            if hasattr(self.enable_member, 'to_alipay_dict'):
                params['enable_member'] = self.enable_member.to_alipay_dict()
            else:
                params['enable_member'] = self.enable_member
        if self.hotel_code:
            if hasattr(self.hotel_code, 'to_alipay_dict'):
                params['hotel_code'] = self.hotel_code.to_alipay_dict()
            else:
                params['hotel_code'] = self.hotel_code
        if self.hotel_group_code:
            if hasattr(self.hotel_group_code, 'to_alipay_dict'):
                params['hotel_group_code'] = self.hotel_group_code.to_alipay_dict()
            else:
                params['hotel_group_code'] = self.hotel_group_code
        if self.hotel_name:
            if hasattr(self.hotel_name, 'to_alipay_dict'):
                params['hotel_name'] = self.hotel_name.to_alipay_dict()
            else:
                params['hotel_name'] = self.hotel_name
        if self.registration_agreement:
            if isinstance(self.registration_agreement, list):
                for i in range(0, len(self.registration_agreement)):
                    element = self.registration_agreement[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.registration_agreement[i] = element.to_alipay_dict()
            if hasattr(self.registration_agreement, 'to_alipay_dict'):
                params['registration_agreement'] = self.registration_agreement.to_alipay_dict()
            else:
                params['registration_agreement'] = self.registration_agreement
        if self.registration_sub_title:
            if hasattr(self.registration_sub_title, 'to_alipay_dict'):
                params['registration_sub_title'] = self.registration_sub_title.to_alipay_dict()
            else:
                params['registration_sub_title'] = self.registration_sub_title
        if self.room_no_pattern_type:
            if hasattr(self.room_no_pattern_type, 'to_alipay_dict'):
                params['room_no_pattern_type'] = self.room_no_pattern_type.to_alipay_dict()
            else:
                params['room_no_pattern_type'] = self.room_no_pattern_type
        if self.theme:
            if hasattr(self.theme, 'to_alipay_dict'):
                params['theme'] = self.theme.to_alipay_dict()
            else:
                params['theme'] = self.theme
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHotelBasicinfoSetModel()
        if 'enable_member' in d:
            o.enable_member = d['enable_member']
        if 'hotel_code' in d:
            o.hotel_code = d['hotel_code']
        if 'hotel_group_code' in d:
            o.hotel_group_code = d['hotel_group_code']
        if 'hotel_name' in d:
            o.hotel_name = d['hotel_name']
        if 'registration_agreement' in d:
            o.registration_agreement = d['registration_agreement']
        if 'registration_sub_title' in d:
            o.registration_sub_title = d['registration_sub_title']
        if 'room_no_pattern_type' in d:
            o.room_no_pattern_type = d['room_no_pattern_type']
        if 'theme' in d:
            o.theme = d['theme']
        return o


