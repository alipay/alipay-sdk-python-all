#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchOrderDetailDataServiceItems(object):

    def __init__(self):
        self._area_codes = None
        self._carrier_code = None
        self._carrier_list = None
        self._category_attribute_value = None
        self._category_code = None
        self._category_ids = None
        self._channel_type = None
        self._desc = None
        self._img = None
        self._key_word = None
        self._key_word_list = None
        self._logo = None
        self._name = None
        self._parent_service_code = None
        self._region = None
        self._serv_search_catalogs = None
        self._serv_search_keywords = None
        self._service_code = None
        self._service_name = None
        self._service_time_end = None
        self._service_time_start = None
        self._short_desc = None
        self._spec_code = None
        self._template_id = None

    @property
    def area_codes(self):
        return self._area_codes

    @area_codes.setter
    def area_codes(self, value):
        self._area_codes = value
    @property
    def carrier_code(self):
        return self._carrier_code

    @carrier_code.setter
    def carrier_code(self, value):
        self._carrier_code = value
    @property
    def carrier_list(self):
        return self._carrier_list

    @carrier_list.setter
    def carrier_list(self, value):
        self._carrier_list = value
    @property
    def category_attribute_value(self):
        return self._category_attribute_value

    @category_attribute_value.setter
    def category_attribute_value(self, value):
        self._category_attribute_value = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def category_ids(self):
        return self._category_ids

    @category_ids.setter
    def category_ids(self, value):
        self._category_ids = value
    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        self._img = value
    @property
    def key_word(self):
        return self._key_word

    @key_word.setter
    def key_word(self, value):
        self._key_word = value
    @property
    def key_word_list(self):
        return self._key_word_list

    @key_word_list.setter
    def key_word_list(self, value):
        self._key_word_list = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def parent_service_code(self):
        return self._parent_service_code

    @parent_service_code.setter
    def parent_service_code(self, value):
        self._parent_service_code = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def serv_search_catalogs(self):
        return self._serv_search_catalogs

    @serv_search_catalogs.setter
    def serv_search_catalogs(self, value):
        self._serv_search_catalogs = value
    @property
    def serv_search_keywords(self):
        return self._serv_search_keywords

    @serv_search_keywords.setter
    def serv_search_keywords(self, value):
        self._serv_search_keywords = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_time_end(self):
        return self._service_time_end

    @service_time_end.setter
    def service_time_end(self, value):
        self._service_time_end = value
    @property
    def service_time_start(self):
        return self._service_time_start

    @service_time_start.setter
    def service_time_start(self, value):
        self._service_time_start = value
    @property
    def short_desc(self):
        return self._short_desc

    @short_desc.setter
    def short_desc(self, value):
        self._short_desc = value
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_codes:
            if hasattr(self.area_codes, 'to_alipay_dict'):
                params['area_codes'] = self.area_codes.to_alipay_dict()
            else:
                params['area_codes'] = self.area_codes
        if self.carrier_code:
            if hasattr(self.carrier_code, 'to_alipay_dict'):
                params['carrier_code'] = self.carrier_code.to_alipay_dict()
            else:
                params['carrier_code'] = self.carrier_code
        if self.carrier_list:
            if hasattr(self.carrier_list, 'to_alipay_dict'):
                params['carrier_list'] = self.carrier_list.to_alipay_dict()
            else:
                params['carrier_list'] = self.carrier_list
        if self.category_attribute_value:
            if hasattr(self.category_attribute_value, 'to_alipay_dict'):
                params['category_attribute_value'] = self.category_attribute_value.to_alipay_dict()
            else:
                params['category_attribute_value'] = self.category_attribute_value
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.category_ids:
            if hasattr(self.category_ids, 'to_alipay_dict'):
                params['category_ids'] = self.category_ids.to_alipay_dict()
            else:
                params['category_ids'] = self.category_ids
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.img:
            if hasattr(self.img, 'to_alipay_dict'):
                params['img'] = self.img.to_alipay_dict()
            else:
                params['img'] = self.img
        if self.key_word:
            if hasattr(self.key_word, 'to_alipay_dict'):
                params['key_word'] = self.key_word.to_alipay_dict()
            else:
                params['key_word'] = self.key_word
        if self.key_word_list:
            if hasattr(self.key_word_list, 'to_alipay_dict'):
                params['key_word_list'] = self.key_word_list.to_alipay_dict()
            else:
                params['key_word_list'] = self.key_word_list
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.parent_service_code:
            if hasattr(self.parent_service_code, 'to_alipay_dict'):
                params['parent_service_code'] = self.parent_service_code.to_alipay_dict()
            else:
                params['parent_service_code'] = self.parent_service_code
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.serv_search_catalogs:
            if hasattr(self.serv_search_catalogs, 'to_alipay_dict'):
                params['serv_search_catalogs'] = self.serv_search_catalogs.to_alipay_dict()
            else:
                params['serv_search_catalogs'] = self.serv_search_catalogs
        if self.serv_search_keywords:
            if hasattr(self.serv_search_keywords, 'to_alipay_dict'):
                params['serv_search_keywords'] = self.serv_search_keywords.to_alipay_dict()
            else:
                params['serv_search_keywords'] = self.serv_search_keywords
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_time_end:
            if hasattr(self.service_time_end, 'to_alipay_dict'):
                params['service_time_end'] = self.service_time_end.to_alipay_dict()
            else:
                params['service_time_end'] = self.service_time_end
        if self.service_time_start:
            if hasattr(self.service_time_start, 'to_alipay_dict'):
                params['service_time_start'] = self.service_time_start.to_alipay_dict()
            else:
                params['service_time_start'] = self.service_time_start
        if self.short_desc:
            if hasattr(self.short_desc, 'to_alipay_dict'):
                params['short_desc'] = self.short_desc.to_alipay_dict()
            else:
                params['short_desc'] = self.short_desc
        if self.spec_code:
            if hasattr(self.spec_code, 'to_alipay_dict'):
                params['spec_code'] = self.spec_code.to_alipay_dict()
            else:
                params['spec_code'] = self.spec_code
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchOrderDetailDataServiceItems()
        if 'area_codes' in d:
            o.area_codes = d['area_codes']
        if 'carrier_code' in d:
            o.carrier_code = d['carrier_code']
        if 'carrier_list' in d:
            o.carrier_list = d['carrier_list']
        if 'category_attribute_value' in d:
            o.category_attribute_value = d['category_attribute_value']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'category_ids' in d:
            o.category_ids = d['category_ids']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'desc' in d:
            o.desc = d['desc']
        if 'img' in d:
            o.img = d['img']
        if 'key_word' in d:
            o.key_word = d['key_word']
        if 'key_word_list' in d:
            o.key_word_list = d['key_word_list']
        if 'logo' in d:
            o.logo = d['logo']
        if 'name' in d:
            o.name = d['name']
        if 'parent_service_code' in d:
            o.parent_service_code = d['parent_service_code']
        if 'region' in d:
            o.region = d['region']
        if 'serv_search_catalogs' in d:
            o.serv_search_catalogs = d['serv_search_catalogs']
        if 'serv_search_keywords' in d:
            o.serv_search_keywords = d['serv_search_keywords']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_time_end' in d:
            o.service_time_end = d['service_time_end']
        if 'service_time_start' in d:
            o.service_time_start = d['service_time_start']
        if 'short_desc' in d:
            o.short_desc = d['short_desc']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


