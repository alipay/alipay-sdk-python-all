#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchBoxAppInfo import SearchBoxAppInfo
from alipay.aop.api.domain.SearchBoxServiceInfo import SearchBoxServiceInfo


class AlipayOpenSearchboxUpgradeSaveModel(object):

    def __init__(self):
        self._area_keywords = None
        self._box_desc = None
        self._box_id = None
        self._brand_id = None
        self._business_benefit_switch = None
        self._business_district_ids = None
        self._custom_keywords = None
        self._image_id = None
        self._image_name = None
        self._related_accounts = None
        self._service_infos = None

    @property
    def area_keywords(self):
        return self._area_keywords

    @area_keywords.setter
    def area_keywords(self, value):
        if isinstance(value, list):
            self._area_keywords = list()
            for i in value:
                self._area_keywords.append(i)
    @property
    def box_desc(self):
        return self._box_desc

    @box_desc.setter
    def box_desc(self, value):
        self._box_desc = value
    @property
    def box_id(self):
        return self._box_id

    @box_id.setter
    def box_id(self, value):
        self._box_id = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def business_benefit_switch(self):
        return self._business_benefit_switch

    @business_benefit_switch.setter
    def business_benefit_switch(self, value):
        self._business_benefit_switch = value
    @property
    def business_district_ids(self):
        return self._business_district_ids

    @business_district_ids.setter
    def business_district_ids(self, value):
        if isinstance(value, list):
            self._business_district_ids = list()
            for i in value:
                self._business_district_ids.append(i)
    @property
    def custom_keywords(self):
        return self._custom_keywords

    @custom_keywords.setter
    def custom_keywords(self, value):
        if isinstance(value, list):
            self._custom_keywords = list()
            for i in value:
                self._custom_keywords.append(i)
    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def image_name(self):
        return self._image_name

    @image_name.setter
    def image_name(self, value):
        self._image_name = value
    @property
    def related_accounts(self):
        return self._related_accounts

    @related_accounts.setter
    def related_accounts(self, value):
        if isinstance(value, list):
            self._related_accounts = list()
            for i in value:
                if isinstance(i, SearchBoxAppInfo):
                    self._related_accounts.append(i)
                else:
                    self._related_accounts.append(SearchBoxAppInfo.from_alipay_dict(i))
    @property
    def service_infos(self):
        return self._service_infos

    @service_infos.setter
    def service_infos(self, value):
        if isinstance(value, list):
            self._service_infos = list()
            for i in value:
                if isinstance(i, SearchBoxServiceInfo):
                    self._service_infos.append(i)
                else:
                    self._service_infos.append(SearchBoxServiceInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.area_keywords:
            if isinstance(self.area_keywords, list):
                for i in range(0, len(self.area_keywords)):
                    element = self.area_keywords[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.area_keywords[i] = element.to_alipay_dict()
            if hasattr(self.area_keywords, 'to_alipay_dict'):
                params['area_keywords'] = self.area_keywords.to_alipay_dict()
            else:
                params['area_keywords'] = self.area_keywords
        if self.box_desc:
            if hasattr(self.box_desc, 'to_alipay_dict'):
                params['box_desc'] = self.box_desc.to_alipay_dict()
            else:
                params['box_desc'] = self.box_desc
        if self.box_id:
            if hasattr(self.box_id, 'to_alipay_dict'):
                params['box_id'] = self.box_id.to_alipay_dict()
            else:
                params['box_id'] = self.box_id
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.business_benefit_switch:
            if hasattr(self.business_benefit_switch, 'to_alipay_dict'):
                params['business_benefit_switch'] = self.business_benefit_switch.to_alipay_dict()
            else:
                params['business_benefit_switch'] = self.business_benefit_switch
        if self.business_district_ids:
            if isinstance(self.business_district_ids, list):
                for i in range(0, len(self.business_district_ids)):
                    element = self.business_district_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_district_ids[i] = element.to_alipay_dict()
            if hasattr(self.business_district_ids, 'to_alipay_dict'):
                params['business_district_ids'] = self.business_district_ids.to_alipay_dict()
            else:
                params['business_district_ids'] = self.business_district_ids
        if self.custom_keywords:
            if isinstance(self.custom_keywords, list):
                for i in range(0, len(self.custom_keywords)):
                    element = self.custom_keywords[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.custom_keywords[i] = element.to_alipay_dict()
            if hasattr(self.custom_keywords, 'to_alipay_dict'):
                params['custom_keywords'] = self.custom_keywords.to_alipay_dict()
            else:
                params['custom_keywords'] = self.custom_keywords
        if self.image_id:
            if hasattr(self.image_id, 'to_alipay_dict'):
                params['image_id'] = self.image_id.to_alipay_dict()
            else:
                params['image_id'] = self.image_id
        if self.image_name:
            if hasattr(self.image_name, 'to_alipay_dict'):
                params['image_name'] = self.image_name.to_alipay_dict()
            else:
                params['image_name'] = self.image_name
        if self.related_accounts:
            if isinstance(self.related_accounts, list):
                for i in range(0, len(self.related_accounts)):
                    element = self.related_accounts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_accounts[i] = element.to_alipay_dict()
            if hasattr(self.related_accounts, 'to_alipay_dict'):
                params['related_accounts'] = self.related_accounts.to_alipay_dict()
            else:
                params['related_accounts'] = self.related_accounts
        if self.service_infos:
            if isinstance(self.service_infos, list):
                for i in range(0, len(self.service_infos)):
                    element = self.service_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_infos[i] = element.to_alipay_dict()
            if hasattr(self.service_infos, 'to_alipay_dict'):
                params['service_infos'] = self.service_infos.to_alipay_dict()
            else:
                params['service_infos'] = self.service_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSearchboxUpgradeSaveModel()
        if 'area_keywords' in d:
            o.area_keywords = d['area_keywords']
        if 'box_desc' in d:
            o.box_desc = d['box_desc']
        if 'box_id' in d:
            o.box_id = d['box_id']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'business_benefit_switch' in d:
            o.business_benefit_switch = d['business_benefit_switch']
        if 'business_district_ids' in d:
            o.business_district_ids = d['business_district_ids']
        if 'custom_keywords' in d:
            o.custom_keywords = d['custom_keywords']
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'image_name' in d:
            o.image_name = d['image_name']
        if 'related_accounts' in d:
            o.related_accounts = d['related_accounts']
        if 'service_infos' in d:
            o.service_infos = d['service_infos']
        return o


