#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateStyleInfoDTO(object):

    def __init__(self):
        self._background_id = None
        self._banner_img_id = None
        self._banner_url = None
        self._bg_color = None
        self._brand_name = None
        self._card_show_name = None
        self._color = None
        self._column_info_layout = None
        self._feature_descriptions = None
        self._front_image_enable = None
        self._front_text_list_enable = None
        self._logo_id = None
        self._slogan = None
        self._slogan_img_id = None

    @property
    def background_id(self):
        return self._background_id

    @background_id.setter
    def background_id(self, value):
        self._background_id = value
    @property
    def banner_img_id(self):
        return self._banner_img_id

    @banner_img_id.setter
    def banner_img_id(self, value):
        self._banner_img_id = value
    @property
    def banner_url(self):
        return self._banner_url

    @banner_url.setter
    def banner_url(self, value):
        self._banner_url = value
    @property
    def bg_color(self):
        return self._bg_color

    @bg_color.setter
    def bg_color(self, value):
        self._bg_color = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def card_show_name(self):
        return self._card_show_name

    @card_show_name.setter
    def card_show_name(self, value):
        self._card_show_name = value
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
    @property
    def column_info_layout(self):
        return self._column_info_layout

    @column_info_layout.setter
    def column_info_layout(self, value):
        self._column_info_layout = value
    @property
    def feature_descriptions(self):
        return self._feature_descriptions

    @feature_descriptions.setter
    def feature_descriptions(self, value):
        if isinstance(value, list):
            self._feature_descriptions = list()
            for i in value:
                self._feature_descriptions.append(i)
    @property
    def front_image_enable(self):
        return self._front_image_enable

    @front_image_enable.setter
    def front_image_enable(self, value):
        self._front_image_enable = value
    @property
    def front_text_list_enable(self):
        return self._front_text_list_enable

    @front_text_list_enable.setter
    def front_text_list_enable(self, value):
        self._front_text_list_enable = value
    @property
    def logo_id(self):
        return self._logo_id

    @logo_id.setter
    def logo_id(self, value):
        self._logo_id = value
    @property
    def slogan(self):
        return self._slogan

    @slogan.setter
    def slogan(self, value):
        self._slogan = value
    @property
    def slogan_img_id(self):
        return self._slogan_img_id

    @slogan_img_id.setter
    def slogan_img_id(self, value):
        self._slogan_img_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.background_id:
            if hasattr(self.background_id, 'to_alipay_dict'):
                params['background_id'] = self.background_id.to_alipay_dict()
            else:
                params['background_id'] = self.background_id
        if self.banner_img_id:
            if hasattr(self.banner_img_id, 'to_alipay_dict'):
                params['banner_img_id'] = self.banner_img_id.to_alipay_dict()
            else:
                params['banner_img_id'] = self.banner_img_id
        if self.banner_url:
            if hasattr(self.banner_url, 'to_alipay_dict'):
                params['banner_url'] = self.banner_url.to_alipay_dict()
            else:
                params['banner_url'] = self.banner_url
        if self.bg_color:
            if hasattr(self.bg_color, 'to_alipay_dict'):
                params['bg_color'] = self.bg_color.to_alipay_dict()
            else:
                params['bg_color'] = self.bg_color
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.card_show_name:
            if hasattr(self.card_show_name, 'to_alipay_dict'):
                params['card_show_name'] = self.card_show_name.to_alipay_dict()
            else:
                params['card_show_name'] = self.card_show_name
        if self.color:
            if hasattr(self.color, 'to_alipay_dict'):
                params['color'] = self.color.to_alipay_dict()
            else:
                params['color'] = self.color
        if self.column_info_layout:
            if hasattr(self.column_info_layout, 'to_alipay_dict'):
                params['column_info_layout'] = self.column_info_layout.to_alipay_dict()
            else:
                params['column_info_layout'] = self.column_info_layout
        if self.feature_descriptions:
            if isinstance(self.feature_descriptions, list):
                for i in range(0, len(self.feature_descriptions)):
                    element = self.feature_descriptions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.feature_descriptions[i] = element.to_alipay_dict()
            if hasattr(self.feature_descriptions, 'to_alipay_dict'):
                params['feature_descriptions'] = self.feature_descriptions.to_alipay_dict()
            else:
                params['feature_descriptions'] = self.feature_descriptions
        if self.front_image_enable:
            if hasattr(self.front_image_enable, 'to_alipay_dict'):
                params['front_image_enable'] = self.front_image_enable.to_alipay_dict()
            else:
                params['front_image_enable'] = self.front_image_enable
        if self.front_text_list_enable:
            if hasattr(self.front_text_list_enable, 'to_alipay_dict'):
                params['front_text_list_enable'] = self.front_text_list_enable.to_alipay_dict()
            else:
                params['front_text_list_enable'] = self.front_text_list_enable
        if self.logo_id:
            if hasattr(self.logo_id, 'to_alipay_dict'):
                params['logo_id'] = self.logo_id.to_alipay_dict()
            else:
                params['logo_id'] = self.logo_id
        if self.slogan:
            if hasattr(self.slogan, 'to_alipay_dict'):
                params['slogan'] = self.slogan.to_alipay_dict()
            else:
                params['slogan'] = self.slogan
        if self.slogan_img_id:
            if hasattr(self.slogan_img_id, 'to_alipay_dict'):
                params['slogan_img_id'] = self.slogan_img_id.to_alipay_dict()
            else:
                params['slogan_img_id'] = self.slogan_img_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateStyleInfoDTO()
        if 'background_id' in d:
            o.background_id = d['background_id']
        if 'banner_img_id' in d:
            o.banner_img_id = d['banner_img_id']
        if 'banner_url' in d:
            o.banner_url = d['banner_url']
        if 'bg_color' in d:
            o.bg_color = d['bg_color']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'card_show_name' in d:
            o.card_show_name = d['card_show_name']
        if 'color' in d:
            o.color = d['color']
        if 'column_info_layout' in d:
            o.column_info_layout = d['column_info_layout']
        if 'feature_descriptions' in d:
            o.feature_descriptions = d['feature_descriptions']
        if 'front_image_enable' in d:
            o.front_image_enable = d['front_image_enable']
        if 'front_text_list_enable' in d:
            o.front_text_list_enable = d['front_text_list_enable']
        if 'logo_id' in d:
            o.logo_id = d['logo_id']
        if 'slogan' in d:
            o.slogan = d['slogan']
        if 'slogan_img_id' in d:
            o.slogan_img_id = d['slogan_img_id']
        return o


