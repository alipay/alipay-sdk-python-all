#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssuranceInfo import AssuranceInfo
from alipay.aop.api.domain.CommonDescInfo import CommonDescInfo
from alipay.aop.api.domain.CommonDescInfo import CommonDescInfo
from alipay.aop.api.domain.CommonDescInfo import CommonDescInfo
from alipay.aop.api.domain.CommonDescInfo import CommonDescInfo
from alipay.aop.api.domain.SkuPropertyInfo import SkuPropertyInfo
from alipay.aop.api.domain.SkuDescInfo import SkuDescInfo


class AlipayDaoweiServiceModifyModel(object):

    def __init__(self):
        self._assurance_desc = None
        self._attention = None
        self._category_code = None
        self._city_code = None
        self._desc = None
        self._district_code_list = None
        self._image_urls = None
        self._latitude = None
        self._longitude = None
        self._mode = None
        self._out_service_id = None
        self._out_sp_id = None
        self._price_desc = None
        self._price_dim_type = None
        self._process_desc = None
        self._property = None
        self._quantity = None
        self._service_name = None
        self._service_range = None
        self._sku = None
        self._status = None
        self._tags = None
        self._type = None
        self._unit = None
        self._unit_price = None

    @property
    def assurance_desc(self):
        return self._assurance_desc

    @assurance_desc.setter
    def assurance_desc(self, value):
        if isinstance(value, list):
            self._assurance_desc = list()
            for i in value:
                if isinstance(i, AssuranceInfo):
                    self._assurance_desc.append(i)
                else:
                    self._assurance_desc.append(AssuranceInfo.from_alipay_dict(i))
    @property
    def attention(self):
        return self._attention

    @attention.setter
    def attention(self, value):
        if isinstance(value, list):
            self._attention = list()
            for i in value:
                if isinstance(i, CommonDescInfo):
                    self._attention.append(i)
                else:
                    self._attention.append(CommonDescInfo.from_alipay_dict(i))
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        if isinstance(value, list):
            self._desc = list()
            for i in value:
                if isinstance(i, CommonDescInfo):
                    self._desc.append(i)
                else:
                    self._desc.append(CommonDescInfo.from_alipay_dict(i))
    @property
    def district_code_list(self):
        return self._district_code_list

    @district_code_list.setter
    def district_code_list(self, value):
        if isinstance(value, list):
            self._district_code_list = list()
            for i in value:
                self._district_code_list.append(i)
    @property
    def image_urls(self):
        return self._image_urls

    @image_urls.setter
    def image_urls(self, value):
        if isinstance(value, list):
            self._image_urls = list()
            for i in value:
                self._image_urls.append(i)
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def out_service_id(self):
        return self._out_service_id

    @out_service_id.setter
    def out_service_id(self, value):
        self._out_service_id = value
    @property
    def out_sp_id(self):
        return self._out_sp_id

    @out_sp_id.setter
    def out_sp_id(self, value):
        self._out_sp_id = value
    @property
    def price_desc(self):
        return self._price_desc

    @price_desc.setter
    def price_desc(self, value):
        if isinstance(value, list):
            self._price_desc = list()
            for i in value:
                if isinstance(i, CommonDescInfo):
                    self._price_desc.append(i)
                else:
                    self._price_desc.append(CommonDescInfo.from_alipay_dict(i))
    @property
    def price_dim_type(self):
        return self._price_dim_type

    @price_dim_type.setter
    def price_dim_type(self, value):
        self._price_dim_type = value
    @property
    def process_desc(self):
        return self._process_desc

    @process_desc.setter
    def process_desc(self, value):
        if isinstance(value, list):
            self._process_desc = list()
            for i in value:
                if isinstance(i, CommonDescInfo):
                    self._process_desc.append(i)
                else:
                    self._process_desc.append(CommonDescInfo.from_alipay_dict(i))
    @property
    def property(self):
        return self._property

    @property.setter
    def property(self, value):
        if isinstance(value, list):
            self._property = list()
            for i in value:
                if isinstance(i, SkuPropertyInfo):
                    self._property.append(i)
                else:
                    self._property.append(SkuPropertyInfo.from_alipay_dict(i))
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_range(self):
        return self._service_range

    @service_range.setter
    def service_range(self, value):
        self._service_range = value
    @property
    def sku(self):
        return self._sku

    @sku.setter
    def sku(self, value):
        if isinstance(value, list):
            self._sku = list()
            for i in value:
                if isinstance(i, SkuDescInfo):
                    self._sku.append(i)
                else:
                    self._sku.append(SkuDescInfo.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.assurance_desc:
            if isinstance(self.assurance_desc, list):
                for i in range(0, len(self.assurance_desc)):
                    element = self.assurance_desc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.assurance_desc[i] = element.to_alipay_dict()
            if hasattr(self.assurance_desc, 'to_alipay_dict'):
                params['assurance_desc'] = self.assurance_desc.to_alipay_dict()
            else:
                params['assurance_desc'] = self.assurance_desc
        if self.attention:
            if isinstance(self.attention, list):
                for i in range(0, len(self.attention)):
                    element = self.attention[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attention[i] = element.to_alipay_dict()
            if hasattr(self.attention, 'to_alipay_dict'):
                params['attention'] = self.attention.to_alipay_dict()
            else:
                params['attention'] = self.attention
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.desc:
            if isinstance(self.desc, list):
                for i in range(0, len(self.desc)):
                    element = self.desc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.desc[i] = element.to_alipay_dict()
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.district_code_list:
            if isinstance(self.district_code_list, list):
                for i in range(0, len(self.district_code_list)):
                    element = self.district_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.district_code_list[i] = element.to_alipay_dict()
            if hasattr(self.district_code_list, 'to_alipay_dict'):
                params['district_code_list'] = self.district_code_list.to_alipay_dict()
            else:
                params['district_code_list'] = self.district_code_list
        if self.image_urls:
            if isinstance(self.image_urls, list):
                for i in range(0, len(self.image_urls)):
                    element = self.image_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_urls[i] = element.to_alipay_dict()
            if hasattr(self.image_urls, 'to_alipay_dict'):
                params['image_urls'] = self.image_urls.to_alipay_dict()
            else:
                params['image_urls'] = self.image_urls
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.out_service_id:
            if hasattr(self.out_service_id, 'to_alipay_dict'):
                params['out_service_id'] = self.out_service_id.to_alipay_dict()
            else:
                params['out_service_id'] = self.out_service_id
        if self.out_sp_id:
            if hasattr(self.out_sp_id, 'to_alipay_dict'):
                params['out_sp_id'] = self.out_sp_id.to_alipay_dict()
            else:
                params['out_sp_id'] = self.out_sp_id
        if self.price_desc:
            if isinstance(self.price_desc, list):
                for i in range(0, len(self.price_desc)):
                    element = self.price_desc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.price_desc[i] = element.to_alipay_dict()
            if hasattr(self.price_desc, 'to_alipay_dict'):
                params['price_desc'] = self.price_desc.to_alipay_dict()
            else:
                params['price_desc'] = self.price_desc
        if self.price_dim_type:
            if hasattr(self.price_dim_type, 'to_alipay_dict'):
                params['price_dim_type'] = self.price_dim_type.to_alipay_dict()
            else:
                params['price_dim_type'] = self.price_dim_type
        if self.process_desc:
            if isinstance(self.process_desc, list):
                for i in range(0, len(self.process_desc)):
                    element = self.process_desc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.process_desc[i] = element.to_alipay_dict()
            if hasattr(self.process_desc, 'to_alipay_dict'):
                params['process_desc'] = self.process_desc.to_alipay_dict()
            else:
                params['process_desc'] = self.process_desc
        if self.property:
            if isinstance(self.property, list):
                for i in range(0, len(self.property)):
                    element = self.property[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.property[i] = element.to_alipay_dict()
            if hasattr(self.property, 'to_alipay_dict'):
                params['property'] = self.property.to_alipay_dict()
            else:
                params['property'] = self.property
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_range:
            if hasattr(self.service_range, 'to_alipay_dict'):
                params['service_range'] = self.service_range.to_alipay_dict()
            else:
                params['service_range'] = self.service_range
        if self.sku:
            if isinstance(self.sku, list):
                for i in range(0, len(self.sku)):
                    element = self.sku[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku[i] = element.to_alipay_dict()
            if hasattr(self.sku, 'to_alipay_dict'):
                params['sku'] = self.sku.to_alipay_dict()
            else:
                params['sku'] = self.sku
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tags:
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDaoweiServiceModifyModel()
        if 'assurance_desc' in d:
            o.assurance_desc = d['assurance_desc']
        if 'attention' in d:
            o.attention = d['attention']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'desc' in d:
            o.desc = d['desc']
        if 'district_code_list' in d:
            o.district_code_list = d['district_code_list']
        if 'image_urls' in d:
            o.image_urls = d['image_urls']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'mode' in d:
            o.mode = d['mode']
        if 'out_service_id' in d:
            o.out_service_id = d['out_service_id']
        if 'out_sp_id' in d:
            o.out_sp_id = d['out_sp_id']
        if 'price_desc' in d:
            o.price_desc = d['price_desc']
        if 'price_dim_type' in d:
            o.price_dim_type = d['price_dim_type']
        if 'process_desc' in d:
            o.process_desc = d['process_desc']
        if 'property' in d:
            o.property = d['property']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_range' in d:
            o.service_range = d['service_range']
        if 'sku' in d:
            o.sku = d['sku']
        if 'status' in d:
            o.status = d['status']
        if 'tags' in d:
            o.tags = d['tags']
        if 'type' in d:
            o.type = d['type']
        if 'unit' in d:
            o.unit = d['unit']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


