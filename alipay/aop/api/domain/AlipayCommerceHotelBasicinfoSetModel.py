#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HotelThemeVO import HotelThemeVO


class AlipayCommerceHotelBasicinfoSetModel(object):

    def __init__(self):
        self._checkin_success_image = None
        self._enable_member = None
        self._enable_order_id_query = None
        self._enable_phone_query = None
        self._enable_reservation_no_query = None
        self._hotel_code = None
        self._hotel_description = None
        self._hotel_group_code = None
        self._hotel_name = None
        self._keycard_production_image = None
        self._registration_agreement = None
        self._registration_sub_title = None
        self._room_no_pattern_type = None
        self._theme = None

    @property
    def checkin_success_image(self):
        return self._checkin_success_image

    @checkin_success_image.setter
    def checkin_success_image(self, value):
        self._checkin_success_image = value
    @property
    def enable_member(self):
        return self._enable_member

    @enable_member.setter
    def enable_member(self, value):
        self._enable_member = value
    @property
    def enable_order_id_query(self):
        return self._enable_order_id_query

    @enable_order_id_query.setter
    def enable_order_id_query(self, value):
        self._enable_order_id_query = value
    @property
    def enable_phone_query(self):
        return self._enable_phone_query

    @enable_phone_query.setter
    def enable_phone_query(self, value):
        self._enable_phone_query = value
    @property
    def enable_reservation_no_query(self):
        return self._enable_reservation_no_query

    @enable_reservation_no_query.setter
    def enable_reservation_no_query(self, value):
        self._enable_reservation_no_query = value
    @property
    def hotel_code(self):
        return self._hotel_code

    @hotel_code.setter
    def hotel_code(self, value):
        self._hotel_code = value
    @property
    def hotel_description(self):
        return self._hotel_description

    @hotel_description.setter
    def hotel_description(self, value):
        self._hotel_description = value
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
    def keycard_production_image(self):
        return self._keycard_production_image

    @keycard_production_image.setter
    def keycard_production_image(self, value):
        self._keycard_production_image = value
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
        if self.checkin_success_image:
            if hasattr(self.checkin_success_image, 'to_alipay_dict'):
                params['checkin_success_image'] = self.checkin_success_image.to_alipay_dict()
            else:
                params['checkin_success_image'] = self.checkin_success_image
        if self.enable_member:
            if hasattr(self.enable_member, 'to_alipay_dict'):
                params['enable_member'] = self.enable_member.to_alipay_dict()
            else:
                params['enable_member'] = self.enable_member
        if self.enable_order_id_query:
            if hasattr(self.enable_order_id_query, 'to_alipay_dict'):
                params['enable_order_id_query'] = self.enable_order_id_query.to_alipay_dict()
            else:
                params['enable_order_id_query'] = self.enable_order_id_query
        if self.enable_phone_query:
            if hasattr(self.enable_phone_query, 'to_alipay_dict'):
                params['enable_phone_query'] = self.enable_phone_query.to_alipay_dict()
            else:
                params['enable_phone_query'] = self.enable_phone_query
        if self.enable_reservation_no_query:
            if hasattr(self.enable_reservation_no_query, 'to_alipay_dict'):
                params['enable_reservation_no_query'] = self.enable_reservation_no_query.to_alipay_dict()
            else:
                params['enable_reservation_no_query'] = self.enable_reservation_no_query
        if self.hotel_code:
            if hasattr(self.hotel_code, 'to_alipay_dict'):
                params['hotel_code'] = self.hotel_code.to_alipay_dict()
            else:
                params['hotel_code'] = self.hotel_code
        if self.hotel_description:
            if hasattr(self.hotel_description, 'to_alipay_dict'):
                params['hotel_description'] = self.hotel_description.to_alipay_dict()
            else:
                params['hotel_description'] = self.hotel_description
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
        if self.keycard_production_image:
            if hasattr(self.keycard_production_image, 'to_alipay_dict'):
                params['keycard_production_image'] = self.keycard_production_image.to_alipay_dict()
            else:
                params['keycard_production_image'] = self.keycard_production_image
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
        if 'checkin_success_image' in d:
            o.checkin_success_image = d['checkin_success_image']
        if 'enable_member' in d:
            o.enable_member = d['enable_member']
        if 'enable_order_id_query' in d:
            o.enable_order_id_query = d['enable_order_id_query']
        if 'enable_phone_query' in d:
            o.enable_phone_query = d['enable_phone_query']
        if 'enable_reservation_no_query' in d:
            o.enable_reservation_no_query = d['enable_reservation_no_query']
        if 'hotel_code' in d:
            o.hotel_code = d['hotel_code']
        if 'hotel_description' in d:
            o.hotel_description = d['hotel_description']
        if 'hotel_group_code' in d:
            o.hotel_group_code = d['hotel_group_code']
        if 'hotel_name' in d:
            o.hotel_name = d['hotel_name']
        if 'keycard_production_image' in d:
            o.keycard_production_image = d['keycard_production_image']
        if 'registration_agreement' in d:
            o.registration_agreement = d['registration_agreement']
        if 'registration_sub_title' in d:
            o.registration_sub_title = d['registration_sub_title']
        if 'room_no_pattern_type' in d:
            o.room_no_pattern_type = d['room_no_pattern_type']
        if 'theme' in d:
            o.theme = d['theme']
        return o


