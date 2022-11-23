#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CardQuickServiceDTO import CardQuickServiceDTO


class AlipayUserCardTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCardTemplateQueryResponse, self).__init__()
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

    def parse_response_content(self, response_content):
        response = super(AlipayUserCardTemplateQueryResponse, self).parse_response_content(response_content)
        if 'background_url' in response:
            self.background_url = response['background_url']
        if 'banner_image_url' in response:
            self.banner_image_url = response['banner_image_url']
        if 'banner_url' in response:
            self.banner_url = response['banner_url']
        if 'code_type' in response:
            self.code_type = response['code_type']
        if 'date_type' in response:
            self.date_type = response['date_type']
        if 'description' in response:
            self.description = response['description']
        if 'logo_url' in response:
            self.logo_url = response['logo_url']
        if 'need_balance' in response:
            self.need_balance = response['need_balance']
        if 'need_level' in response:
            self.need_level = response['need_level']
        if 'need_point' in response:
            self.need_point = response['need_point']
        if 'point_display_name' in response:
            self.point_display_name = response['point_display_name']
        if 'private_card_page_url' in response:
            self.private_card_page_url = response['private_card_page_url']
        if 'quick_services' in response:
            self.quick_services = response['quick_services']
        if 'service_phone' in response:
            self.service_phone = response['service_phone']
        if 'sub_title' in response:
            self.sub_title = response['sub_title']
        if 'title' in response:
            self.title = response['title']
