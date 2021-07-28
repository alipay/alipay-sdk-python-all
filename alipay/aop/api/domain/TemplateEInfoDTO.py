#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateEInfoUnitDTO import TemplateEInfoUnitDTO
from alipay.aop.api.domain.TemplateEInfoUnitDTO import TemplateEInfoUnitDTO
from alipay.aop.api.domain.TemplateBannerDTO import TemplateBannerDTO
from alipay.aop.api.domain.TemplateEInfoUnitDTO import TemplateEInfoUnitDTO


class TemplateEInfoDTO(object):

    def __init__(self):
        self._auxiliary_fields = None
        self._available_item_ids = None
        self._available_item_source = None
        self._back_fields = None
        self._banner = None
        self._custom_fields = None
        self._logo_text = None
        self._origin_price = None
        self._pass_img = None
        self._pass_img_ratio = None
        self._second_logo_text = None
        self._use_condition = None
        self._use_limit_city = None
        self._use_limit_desc = None
        self._use_limit_scene = None

    @property
    def auxiliary_fields(self):
        return self._auxiliary_fields

    @auxiliary_fields.setter
    def auxiliary_fields(self, value):
        if isinstance(value, list):
            self._auxiliary_fields = list()
            for i in value:
                if isinstance(i, TemplateEInfoUnitDTO):
                    self._auxiliary_fields.append(i)
                else:
                    self._auxiliary_fields.append(TemplateEInfoUnitDTO.from_alipay_dict(i))
    @property
    def available_item_ids(self):
        return self._available_item_ids

    @available_item_ids.setter
    def available_item_ids(self, value):
        if isinstance(value, list):
            self._available_item_ids = list()
            for i in value:
                self._available_item_ids.append(i)
    @property
    def available_item_source(self):
        return self._available_item_source

    @available_item_source.setter
    def available_item_source(self, value):
        self._available_item_source = value
    @property
    def back_fields(self):
        return self._back_fields

    @back_fields.setter
    def back_fields(self, value):
        if isinstance(value, list):
            self._back_fields = list()
            for i in value:
                if isinstance(i, TemplateEInfoUnitDTO):
                    self._back_fields.append(i)
                else:
                    self._back_fields.append(TemplateEInfoUnitDTO.from_alipay_dict(i))
    @property
    def banner(self):
        return self._banner

    @banner.setter
    def banner(self, value):
        if isinstance(value, TemplateBannerDTO):
            self._banner = value
        else:
            self._banner = TemplateBannerDTO.from_alipay_dict(value)
    @property
    def custom_fields(self):
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, value):
        if isinstance(value, list):
            self._custom_fields = list()
            for i in value:
                if isinstance(i, TemplateEInfoUnitDTO):
                    self._custom_fields.append(i)
                else:
                    self._custom_fields.append(TemplateEInfoUnitDTO.from_alipay_dict(i))
    @property
    def logo_text(self):
        return self._logo_text

    @logo_text.setter
    def logo_text(self, value):
        self._logo_text = value
    @property
    def origin_price(self):
        return self._origin_price

    @origin_price.setter
    def origin_price(self, value):
        self._origin_price = value
    @property
    def pass_img(self):
        return self._pass_img

    @pass_img.setter
    def pass_img(self, value):
        self._pass_img = value
    @property
    def pass_img_ratio(self):
        return self._pass_img_ratio

    @pass_img_ratio.setter
    def pass_img_ratio(self, value):
        self._pass_img_ratio = value
    @property
    def second_logo_text(self):
        return self._second_logo_text

    @second_logo_text.setter
    def second_logo_text(self, value):
        self._second_logo_text = value
    @property
    def use_condition(self):
        return self._use_condition

    @use_condition.setter
    def use_condition(self, value):
        self._use_condition = value
    @property
    def use_limit_city(self):
        return self._use_limit_city

    @use_limit_city.setter
    def use_limit_city(self, value):
        self._use_limit_city = value
    @property
    def use_limit_desc(self):
        return self._use_limit_desc

    @use_limit_desc.setter
    def use_limit_desc(self, value):
        self._use_limit_desc = value
    @property
    def use_limit_scene(self):
        return self._use_limit_scene

    @use_limit_scene.setter
    def use_limit_scene(self, value):
        self._use_limit_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.auxiliary_fields:
            if isinstance(self.auxiliary_fields, list):
                for i in range(0, len(self.auxiliary_fields)):
                    element = self.auxiliary_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.auxiliary_fields[i] = element.to_alipay_dict()
            if hasattr(self.auxiliary_fields, 'to_alipay_dict'):
                params['auxiliary_fields'] = self.auxiliary_fields.to_alipay_dict()
            else:
                params['auxiliary_fields'] = self.auxiliary_fields
        if self.available_item_ids:
            if isinstance(self.available_item_ids, list):
                for i in range(0, len(self.available_item_ids)):
                    element = self.available_item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_item_ids[i] = element.to_alipay_dict()
            if hasattr(self.available_item_ids, 'to_alipay_dict'):
                params['available_item_ids'] = self.available_item_ids.to_alipay_dict()
            else:
                params['available_item_ids'] = self.available_item_ids
        if self.available_item_source:
            if hasattr(self.available_item_source, 'to_alipay_dict'):
                params['available_item_source'] = self.available_item_source.to_alipay_dict()
            else:
                params['available_item_source'] = self.available_item_source
        if self.back_fields:
            if isinstance(self.back_fields, list):
                for i in range(0, len(self.back_fields)):
                    element = self.back_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.back_fields[i] = element.to_alipay_dict()
            if hasattr(self.back_fields, 'to_alipay_dict'):
                params['back_fields'] = self.back_fields.to_alipay_dict()
            else:
                params['back_fields'] = self.back_fields
        if self.banner:
            if hasattr(self.banner, 'to_alipay_dict'):
                params['banner'] = self.banner.to_alipay_dict()
            else:
                params['banner'] = self.banner
        if self.custom_fields:
            if isinstance(self.custom_fields, list):
                for i in range(0, len(self.custom_fields)):
                    element = self.custom_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.custom_fields[i] = element.to_alipay_dict()
            if hasattr(self.custom_fields, 'to_alipay_dict'):
                params['custom_fields'] = self.custom_fields.to_alipay_dict()
            else:
                params['custom_fields'] = self.custom_fields
        if self.logo_text:
            if hasattr(self.logo_text, 'to_alipay_dict'):
                params['logo_text'] = self.logo_text.to_alipay_dict()
            else:
                params['logo_text'] = self.logo_text
        if self.origin_price:
            if hasattr(self.origin_price, 'to_alipay_dict'):
                params['origin_price'] = self.origin_price.to_alipay_dict()
            else:
                params['origin_price'] = self.origin_price
        if self.pass_img:
            if hasattr(self.pass_img, 'to_alipay_dict'):
                params['pass_img'] = self.pass_img.to_alipay_dict()
            else:
                params['pass_img'] = self.pass_img
        if self.pass_img_ratio:
            if hasattr(self.pass_img_ratio, 'to_alipay_dict'):
                params['pass_img_ratio'] = self.pass_img_ratio.to_alipay_dict()
            else:
                params['pass_img_ratio'] = self.pass_img_ratio
        if self.second_logo_text:
            if hasattr(self.second_logo_text, 'to_alipay_dict'):
                params['second_logo_text'] = self.second_logo_text.to_alipay_dict()
            else:
                params['second_logo_text'] = self.second_logo_text
        if self.use_condition:
            if hasattr(self.use_condition, 'to_alipay_dict'):
                params['use_condition'] = self.use_condition.to_alipay_dict()
            else:
                params['use_condition'] = self.use_condition
        if self.use_limit_city:
            if hasattr(self.use_limit_city, 'to_alipay_dict'):
                params['use_limit_city'] = self.use_limit_city.to_alipay_dict()
            else:
                params['use_limit_city'] = self.use_limit_city
        if self.use_limit_desc:
            if hasattr(self.use_limit_desc, 'to_alipay_dict'):
                params['use_limit_desc'] = self.use_limit_desc.to_alipay_dict()
            else:
                params['use_limit_desc'] = self.use_limit_desc
        if self.use_limit_scene:
            if hasattr(self.use_limit_scene, 'to_alipay_dict'):
                params['use_limit_scene'] = self.use_limit_scene.to_alipay_dict()
            else:
                params['use_limit_scene'] = self.use_limit_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateEInfoDTO()
        if 'auxiliary_fields' in d:
            o.auxiliary_fields = d['auxiliary_fields']
        if 'available_item_ids' in d:
            o.available_item_ids = d['available_item_ids']
        if 'available_item_source' in d:
            o.available_item_source = d['available_item_source']
        if 'back_fields' in d:
            o.back_fields = d['back_fields']
        if 'banner' in d:
            o.banner = d['banner']
        if 'custom_fields' in d:
            o.custom_fields = d['custom_fields']
        if 'logo_text' in d:
            o.logo_text = d['logo_text']
        if 'origin_price' in d:
            o.origin_price = d['origin_price']
        if 'pass_img' in d:
            o.pass_img = d['pass_img']
        if 'pass_img_ratio' in d:
            o.pass_img_ratio = d['pass_img_ratio']
        if 'second_logo_text' in d:
            o.second_logo_text = d['second_logo_text']
        if 'use_condition' in d:
            o.use_condition = d['use_condition']
        if 'use_limit_city' in d:
            o.use_limit_city = d['use_limit_city']
        if 'use_limit_desc' in d:
            o.use_limit_desc = d['use_limit_desc']
        if 'use_limit_scene' in d:
            o.use_limit_scene = d['use_limit_scene']
        return o


