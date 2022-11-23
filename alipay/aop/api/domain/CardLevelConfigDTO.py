#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardQuickServiceDTO import CardQuickServiceDTO


class CardLevelConfigDTO(object):

    def __init__(self):
        self._background_url = None
        self._banner_image_url = None
        self._banner_url = None
        self._level = None
        self._logo_url = None
        self._quick_services = None
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
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
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
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
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
        o = CardLevelConfigDTO()
        if 'background_url' in d:
            o.background_url = d['background_url']
        if 'banner_image_url' in d:
            o.banner_image_url = d['banner_image_url']
        if 'banner_url' in d:
            o.banner_url = d['banner_url']
        if 'level' in d:
            o.level = d['level']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'quick_services' in d:
            o.quick_services = d['quick_services']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        return o


