#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchBoxAppInfo import SearchBoxAppInfo
from alipay.aop.api.domain.SearchBoxServiceInfo import SearchBoxServiceInfo


class AlipayOpenSearchBoxModifyModel(object):

    def __init__(self):
        self._box_desc = None
        self._box_id = None
        self._brand_id = None
        self._custom_keywords = None
        self._image_id = None
        self._image_name = None
        self._merchant_id = None
        self._module_id = None
        self._module_type = None
        self._related_accounts = None
        self._service_infos = None
        self._target_appid = None

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
    def custom_keywords(self):
        return self._custom_keywords

    @custom_keywords.setter
    def custom_keywords(self, value):
        self._custom_keywords = value
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
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def module_id(self):
        return self._module_id

    @module_id.setter
    def module_id(self, value):
        self._module_id = value
    @property
    def module_type(self):
        return self._module_type

    @module_type.setter
    def module_type(self, value):
        self._module_type = value
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
    @property
    def target_appid(self):
        return self._target_appid

    @target_appid.setter
    def target_appid(self, value):
        self._target_appid = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.custom_keywords:
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
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.module_id:
            if hasattr(self.module_id, 'to_alipay_dict'):
                params['module_id'] = self.module_id.to_alipay_dict()
            else:
                params['module_id'] = self.module_id
        if self.module_type:
            if hasattr(self.module_type, 'to_alipay_dict'):
                params['module_type'] = self.module_type.to_alipay_dict()
            else:
                params['module_type'] = self.module_type
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
        if self.target_appid:
            if hasattr(self.target_appid, 'to_alipay_dict'):
                params['target_appid'] = self.target_appid.to_alipay_dict()
            else:
                params['target_appid'] = self.target_appid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSearchBoxModifyModel()
        if 'box_desc' in d:
            o.box_desc = d['box_desc']
        if 'box_id' in d:
            o.box_id = d['box_id']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'custom_keywords' in d:
            o.custom_keywords = d['custom_keywords']
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'image_name' in d:
            o.image_name = d['image_name']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'module_id' in d:
            o.module_id = d['module_id']
        if 'module_type' in d:
            o.module_type = d['module_type']
        if 'related_accounts' in d:
            o.related_accounts = d['related_accounts']
        if 'service_infos' in d:
            o.service_infos = d['service_infos']
        if 'target_appid' in d:
            o.target_appid = d['target_appid']
        return o


