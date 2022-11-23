#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardQuickServiceDTO import CardQuickServiceDTO


class AlipayUserCardTemplateCreateModel(object):

    def __init__(self):
        self._background_url = None
        self._banner_image_url = None
        self._banner_url = None
        self._code_type = None
        self._date_type = None
        self._description = None
        self._logo_url = None
        self._need_balance = None
        self._need_level = None
        self._need_point = None
        self._point_display_name = None
        self._private_card_page_url = None
        self._quick_services = None
        self._service_phone = None
        self._sub_title = None
        self._title = None

    @property
    def background_url(self):
        return self._background_url

    @background_url.setter
    def background_url(self, value):
        self._background_url = value
    @property
    def banner_image_url(self):
        return self._banner_image_url

    @banner_image_url.setter
    def banner_image_url(self, value):
        self._banner_image_url = value
    @property
    def banner_url(self):
        return self._banner_url

    @banner_url.setter
    def banner_url(self, value):
        self._banner_url = value
    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def date_type(self):
        return self._date_type

    @date_type.setter
    def date_type(self, value):
        self._date_type = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def need_balance(self):
        return self._need_balance

    @need_balance.setter
    def need_balance(self, value):
        self._need_balance = value
    @property
    def need_level(self):
        return self._need_level

    @need_level.setter
    def need_level(self, value):
        self._need_level = value
    @property
    def need_point(self):
        return self._need_point

    @need_point.setter
    def need_point(self, value):
        self._need_point = value
    @property
    def point_display_name(self):
        return self._point_display_name

    @point_display_name.setter
    def point_display_name(self, value):
        self._point_display_name = value
    @property
    def private_card_page_url(self):
        return self._private_card_page_url

    @private_card_page_url.setter
    def private_card_page_url(self, value):
        self._private_card_page_url = value
    @property
    def quick_services(self):
        return self._quick_services

    @quick_services.setter
    def quick_services(self, value):
        if isinstance(value, list):
            self._quick_services = list()
            for i in value:
                if isinstance(i, CardQuickServiceDTO):
                    self._quick_services.append(i)
                else:
                    self._quick_services.append(CardQuickServiceDTO.from_alipay_dict(i))
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.background_url:
            if hasattr(self.background_url, 'to_alipay_dict'):
                params['background_url'] = self.background_url.to_alipay_dict()
            else:
                params['background_url'] = self.background_url
        if self.banner_image_url:
            if hasattr(self.banner_image_url, 'to_alipay_dict'):
                params['banner_image_url'] = self.banner_image_url.to_alipay_dict()
            else:
                params['banner_image_url'] = self.banner_image_url
        if self.banner_url:
            if hasattr(self.banner_url, 'to_alipay_dict'):
                params['banner_url'] = self.banner_url.to_alipay_dict()
            else:
                params['banner_url'] = self.banner_url
        if self.code_type:
            if hasattr(self.code_type, 'to_alipay_dict'):
                params['code_type'] = self.code_type.to_alipay_dict()
            else:
                params['code_type'] = self.code_type
        if self.date_type:
            if hasattr(self.date_type, 'to_alipay_dict'):
                params['date_type'] = self.date_type.to_alipay_dict()
            else:
                params['date_type'] = self.date_type
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.need_balance:
            if hasattr(self.need_balance, 'to_alipay_dict'):
                params['need_balance'] = self.need_balance.to_alipay_dict()
            else:
                params['need_balance'] = self.need_balance
        if self.need_level:
            if hasattr(self.need_level, 'to_alipay_dict'):
                params['need_level'] = self.need_level.to_alipay_dict()
            else:
                params['need_level'] = self.need_level
        if self.need_point:
            if hasattr(self.need_point, 'to_alipay_dict'):
                params['need_point'] = self.need_point.to_alipay_dict()
            else:
                params['need_point'] = self.need_point
        if self.point_display_name:
            if hasattr(self.point_display_name, 'to_alipay_dict'):
                params['point_display_name'] = self.point_display_name.to_alipay_dict()
            else:
                params['point_display_name'] = self.point_display_name
        if self.private_card_page_url:
            if hasattr(self.private_card_page_url, 'to_alipay_dict'):
                params['private_card_page_url'] = self.private_card_page_url.to_alipay_dict()
            else:
                params['private_card_page_url'] = self.private_card_page_url
        if self.quick_services:
            if isinstance(self.quick_services, list):
                for i in range(0, len(self.quick_services)):
                    element = self.quick_services[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.quick_services[i] = element.to_alipay_dict()
            if hasattr(self.quick_services, 'to_alipay_dict'):
                params['quick_services'] = self.quick_services.to_alipay_dict()
            else:
                params['quick_services'] = self.quick_services
        if self.service_phone:
            if hasattr(self.service_phone, 'to_alipay_dict'):
                params['service_phone'] = self.service_phone.to_alipay_dict()
            else:
                params['service_phone'] = self.service_phone
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCardTemplateCreateModel()
        if 'background_url' in d:
            o.background_url = d['background_url']
        if 'banner_image_url' in d:
            o.banner_image_url = d['banner_image_url']
        if 'banner_url' in d:
            o.banner_url = d['banner_url']
        if 'code_type' in d:
            o.code_type = d['code_type']
        if 'date_type' in d:
            o.date_type = d['date_type']
        if 'description' in d:
            o.description = d['description']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'need_balance' in d:
            o.need_balance = d['need_balance']
        if 'need_level' in d:
            o.need_level = d['need_level']
        if 'need_point' in d:
            o.need_point = d['need_point']
        if 'point_display_name' in d:
            o.point_display_name = d['point_display_name']
        if 'private_card_page_url' in d:
            o.private_card_page_url = d['private_card_page_url']
        if 'quick_services' in d:
            o.quick_services = d['quick_services']
        if 'service_phone' in d:
            o.service_phone = d['service_phone']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        return o


