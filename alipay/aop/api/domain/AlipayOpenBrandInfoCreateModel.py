#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BrandTrademarkInfoOpenApi import BrandTrademarkInfoOpenApi
from alipay.aop.api.domain.UnStandardBrandAddInfoOpenApi import UnStandardBrandAddInfoOpenApi


class AlipayOpenBrandInfoCreateModel(object):

    def __init__(self):
        self._brand_chs_name = None
        self._brand_eng_name = None
        self._brand_id = None
        self._brand_story = None
        self._brand_trademark_infos = None
        self._logo_url = None
        self._owner_name = None
        self._standard = None
        self._unstandard_brand_info = None

    @property
    def brand_chs_name(self):
        return self._brand_chs_name

    @brand_chs_name.setter
    def brand_chs_name(self, value):
        self._brand_chs_name = value
    @property
    def brand_eng_name(self):
        return self._brand_eng_name

    @brand_eng_name.setter
    def brand_eng_name(self, value):
        self._brand_eng_name = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_story(self):
        return self._brand_story

    @brand_story.setter
    def brand_story(self, value):
        self._brand_story = value
    @property
    def brand_trademark_infos(self):
        return self._brand_trademark_infos

    @brand_trademark_infos.setter
    def brand_trademark_infos(self, value):
        if isinstance(value, list):
            self._brand_trademark_infos = list()
            for i in value:
                if isinstance(i, BrandTrademarkInfoOpenApi):
                    self._brand_trademark_infos.append(i)
                else:
                    self._brand_trademark_infos.append(BrandTrademarkInfoOpenApi.from_alipay_dict(i))
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def standard(self):
        return self._standard

    @standard.setter
    def standard(self, value):
        self._standard = value
    @property
    def unstandard_brand_info(self):
        return self._unstandard_brand_info

    @unstandard_brand_info.setter
    def unstandard_brand_info(self, value):
        if isinstance(value, UnStandardBrandAddInfoOpenApi):
            self._unstandard_brand_info = value
        else:
            self._unstandard_brand_info = UnStandardBrandAddInfoOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.brand_chs_name:
            if hasattr(self.brand_chs_name, 'to_alipay_dict'):
                params['brand_chs_name'] = self.brand_chs_name.to_alipay_dict()
            else:
                params['brand_chs_name'] = self.brand_chs_name
        if self.brand_eng_name:
            if hasattr(self.brand_eng_name, 'to_alipay_dict'):
                params['brand_eng_name'] = self.brand_eng_name.to_alipay_dict()
            else:
                params['brand_eng_name'] = self.brand_eng_name
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_story:
            if hasattr(self.brand_story, 'to_alipay_dict'):
                params['brand_story'] = self.brand_story.to_alipay_dict()
            else:
                params['brand_story'] = self.brand_story
        if self.brand_trademark_infos:
            if isinstance(self.brand_trademark_infos, list):
                for i in range(0, len(self.brand_trademark_infos)):
                    element = self.brand_trademark_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_trademark_infos[i] = element.to_alipay_dict()
            if hasattr(self.brand_trademark_infos, 'to_alipay_dict'):
                params['brand_trademark_infos'] = self.brand_trademark_infos.to_alipay_dict()
            else:
                params['brand_trademark_infos'] = self.brand_trademark_infos
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.standard:
            if hasattr(self.standard, 'to_alipay_dict'):
                params['standard'] = self.standard.to_alipay_dict()
            else:
                params['standard'] = self.standard
        if self.unstandard_brand_info:
            if hasattr(self.unstandard_brand_info, 'to_alipay_dict'):
                params['unstandard_brand_info'] = self.unstandard_brand_info.to_alipay_dict()
            else:
                params['unstandard_brand_info'] = self.unstandard_brand_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenBrandInfoCreateModel()
        if 'brand_chs_name' in d:
            o.brand_chs_name = d['brand_chs_name']
        if 'brand_eng_name' in d:
            o.brand_eng_name = d['brand_eng_name']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_story' in d:
            o.brand_story = d['brand_story']
        if 'brand_trademark_infos' in d:
            o.brand_trademark_infos = d['brand_trademark_infos']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'standard' in d:
            o.standard = d['standard']
        if 'unstandard_brand_info' in d:
            o.unstandard_brand_info = d['unstandard_brand_info']
        return o


