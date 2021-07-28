#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StructureBrandInfo import StructureBrandInfo
from alipay.aop.api.domain.StructureServiceInfo import StructureServiceInfo


class PoiQueryResult(object):

    def __init__(self):
        self._address = None
        self._address_en = None
        self._address_local = None
        self._alternative_phone = None
        self._bios = None
        self._brand_info = None
        self._business_hour = None
        self._category = None
        self._city = None
        self._commercial_circle = None
        self._consumption = None
        self._country_code = None
        self._country_name = None
        self._description = None
        self._extend_map = None
        self._gmt_create = None
        self._gmt_modified = None
        self._lat = None
        self._lng = None
        self._local_language = None
        self._local_name = None
        self._main_phone = None
        self._name = None
        self._name_alias = None
        self._name_en = None
        self._offline_reason_detail = None
        self._open_status = None
        self._open_time = None
        self._operator_type = None
        self._photo_urls = None
        self._poi_id = None
        self._postal_code = None
        self._province = None
        self._recommend_infos = None
        self._seller_id = None
        self._service_info = None
        self._shop_id = None
        self._shop_type = None
        self._source_biz_id = None
        self._store_id = None
        self._sub_seller_id = None
        self._telephone = None
        self._transport = None
        self._type = None
        self._video_url = None
        self._web_site_url = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def address_en(self):
        return self._address_en

    @address_en.setter
    def address_en(self, value):
        self._address_en = value
    @property
    def address_local(self):
        return self._address_local

    @address_local.setter
    def address_local(self, value):
        self._address_local = value
    @property
    def alternative_phone(self):
        return self._alternative_phone

    @alternative_phone.setter
    def alternative_phone(self, value):
        self._alternative_phone = value
    @property
    def bios(self):
        return self._bios

    @bios.setter
    def bios(self, value):
        self._bios = value
    @property
    def brand_info(self):
        return self._brand_info

    @brand_info.setter
    def brand_info(self, value):
        if isinstance(value, StructureBrandInfo):
            self._brand_info = value
        else:
            self._brand_info = StructureBrandInfo.from_alipay_dict(value)
    @property
    def business_hour(self):
        return self._business_hour

    @business_hour.setter
    def business_hour(self, value):
        self._business_hour = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def commercial_circle(self):
        return self._commercial_circle

    @commercial_circle.setter
    def commercial_circle(self, value):
        self._commercial_circle = value
    @property
    def consumption(self):
        return self._consumption

    @consumption.setter
    def consumption(self, value):
        self._consumption = value
    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        self._country_code = value
    @property
    def country_name(self):
        return self._country_name

    @country_name.setter
    def country_name(self, value):
        self._country_name = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def extend_map(self):
        return self._extend_map

    @extend_map.setter
    def extend_map(self, value):
        self._extend_map = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = value
    @property
    def lng(self):
        return self._lng

    @lng.setter
    def lng(self, value):
        self._lng = value
    @property
    def local_language(self):
        return self._local_language

    @local_language.setter
    def local_language(self, value):
        self._local_language = value
    @property
    def local_name(self):
        return self._local_name

    @local_name.setter
    def local_name(self, value):
        self._local_name = value
    @property
    def main_phone(self):
        return self._main_phone

    @main_phone.setter
    def main_phone(self, value):
        self._main_phone = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def name_alias(self):
        return self._name_alias

    @name_alias.setter
    def name_alias(self, value):
        self._name_alias = value
    @property
    def name_en(self):
        return self._name_en

    @name_en.setter
    def name_en(self, value):
        self._name_en = value
    @property
    def offline_reason_detail(self):
        return self._offline_reason_detail

    @offline_reason_detail.setter
    def offline_reason_detail(self, value):
        self._offline_reason_detail = value
    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def photo_urls(self):
        return self._photo_urls

    @photo_urls.setter
    def photo_urls(self, value):
        if isinstance(value, list):
            self._photo_urls = list()
            for i in value:
                self._photo_urls.append(i)
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, value):
        self._postal_code = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def recommend_infos(self):
        return self._recommend_infos

    @recommend_infos.setter
    def recommend_infos(self, value):
        self._recommend_infos = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def service_info(self):
        return self._service_info

    @service_info.setter
    def service_info(self, value):
        if isinstance(value, StructureServiceInfo):
            self._service_info = value
        else:
            self._service_info = StructureServiceInfo.from_alipay_dict(value)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def source_biz_id(self):
        return self._source_biz_id

    @source_biz_id.setter
    def source_biz_id(self, value):
        self._source_biz_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def sub_seller_id(self):
        return self._sub_seller_id

    @sub_seller_id.setter
    def sub_seller_id(self, value):
        self._sub_seller_id = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value
    @property
    def transport(self):
        return self._transport

    @transport.setter
    def transport(self, value):
        self._transport = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def video_url(self):
        return self._video_url

    @video_url.setter
    def video_url(self, value):
        self._video_url = value
    @property
    def web_site_url(self):
        return self._web_site_url

    @web_site_url.setter
    def web_site_url(self, value):
        self._web_site_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.address_en:
            if hasattr(self.address_en, 'to_alipay_dict'):
                params['address_en'] = self.address_en.to_alipay_dict()
            else:
                params['address_en'] = self.address_en
        if self.address_local:
            if hasattr(self.address_local, 'to_alipay_dict'):
                params['address_local'] = self.address_local.to_alipay_dict()
            else:
                params['address_local'] = self.address_local
        if self.alternative_phone:
            if hasattr(self.alternative_phone, 'to_alipay_dict'):
                params['alternative_phone'] = self.alternative_phone.to_alipay_dict()
            else:
                params['alternative_phone'] = self.alternative_phone
        if self.bios:
            if hasattr(self.bios, 'to_alipay_dict'):
                params['bios'] = self.bios.to_alipay_dict()
            else:
                params['bios'] = self.bios
        if self.brand_info:
            if hasattr(self.brand_info, 'to_alipay_dict'):
                params['brand_info'] = self.brand_info.to_alipay_dict()
            else:
                params['brand_info'] = self.brand_info
        if self.business_hour:
            if hasattr(self.business_hour, 'to_alipay_dict'):
                params['business_hour'] = self.business_hour.to_alipay_dict()
            else:
                params['business_hour'] = self.business_hour
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.commercial_circle:
            if hasattr(self.commercial_circle, 'to_alipay_dict'):
                params['commercial_circle'] = self.commercial_circle.to_alipay_dict()
            else:
                params['commercial_circle'] = self.commercial_circle
        if self.consumption:
            if hasattr(self.consumption, 'to_alipay_dict'):
                params['consumption'] = self.consumption.to_alipay_dict()
            else:
                params['consumption'] = self.consumption
        if self.country_code:
            if hasattr(self.country_code, 'to_alipay_dict'):
                params['country_code'] = self.country_code.to_alipay_dict()
            else:
                params['country_code'] = self.country_code
        if self.country_name:
            if hasattr(self.country_name, 'to_alipay_dict'):
                params['country_name'] = self.country_name.to_alipay_dict()
            else:
                params['country_name'] = self.country_name
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.extend_map:
            if hasattr(self.extend_map, 'to_alipay_dict'):
                params['extend_map'] = self.extend_map.to_alipay_dict()
            else:
                params['extend_map'] = self.extend_map
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.lat:
            if hasattr(self.lat, 'to_alipay_dict'):
                params['lat'] = self.lat.to_alipay_dict()
            else:
                params['lat'] = self.lat
        if self.lng:
            if hasattr(self.lng, 'to_alipay_dict'):
                params['lng'] = self.lng.to_alipay_dict()
            else:
                params['lng'] = self.lng
        if self.local_language:
            if hasattr(self.local_language, 'to_alipay_dict'):
                params['local_language'] = self.local_language.to_alipay_dict()
            else:
                params['local_language'] = self.local_language
        if self.local_name:
            if hasattr(self.local_name, 'to_alipay_dict'):
                params['local_name'] = self.local_name.to_alipay_dict()
            else:
                params['local_name'] = self.local_name
        if self.main_phone:
            if hasattr(self.main_phone, 'to_alipay_dict'):
                params['main_phone'] = self.main_phone.to_alipay_dict()
            else:
                params['main_phone'] = self.main_phone
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.name_alias:
            if hasattr(self.name_alias, 'to_alipay_dict'):
                params['name_alias'] = self.name_alias.to_alipay_dict()
            else:
                params['name_alias'] = self.name_alias
        if self.name_en:
            if hasattr(self.name_en, 'to_alipay_dict'):
                params['name_en'] = self.name_en.to_alipay_dict()
            else:
                params['name_en'] = self.name_en
        if self.offline_reason_detail:
            if hasattr(self.offline_reason_detail, 'to_alipay_dict'):
                params['offline_reason_detail'] = self.offline_reason_detail.to_alipay_dict()
            else:
                params['offline_reason_detail'] = self.offline_reason_detail
        if self.open_status:
            if hasattr(self.open_status, 'to_alipay_dict'):
                params['open_status'] = self.open_status.to_alipay_dict()
            else:
                params['open_status'] = self.open_status
        if self.open_time:
            if hasattr(self.open_time, 'to_alipay_dict'):
                params['open_time'] = self.open_time.to_alipay_dict()
            else:
                params['open_time'] = self.open_time
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.photo_urls:
            if isinstance(self.photo_urls, list):
                for i in range(0, len(self.photo_urls)):
                    element = self.photo_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.photo_urls[i] = element.to_alipay_dict()
            if hasattr(self.photo_urls, 'to_alipay_dict'):
                params['photo_urls'] = self.photo_urls.to_alipay_dict()
            else:
                params['photo_urls'] = self.photo_urls
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.postal_code:
            if hasattr(self.postal_code, 'to_alipay_dict'):
                params['postal_code'] = self.postal_code.to_alipay_dict()
            else:
                params['postal_code'] = self.postal_code
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.recommend_infos:
            if hasattr(self.recommend_infos, 'to_alipay_dict'):
                params['recommend_infos'] = self.recommend_infos.to_alipay_dict()
            else:
                params['recommend_infos'] = self.recommend_infos
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.service_info:
            if hasattr(self.service_info, 'to_alipay_dict'):
                params['service_info'] = self.service_info.to_alipay_dict()
            else:
                params['service_info'] = self.service_info
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        if self.source_biz_id:
            if hasattr(self.source_biz_id, 'to_alipay_dict'):
                params['source_biz_id'] = self.source_biz_id.to_alipay_dict()
            else:
                params['source_biz_id'] = self.source_biz_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.sub_seller_id:
            if hasattr(self.sub_seller_id, 'to_alipay_dict'):
                params['sub_seller_id'] = self.sub_seller_id.to_alipay_dict()
            else:
                params['sub_seller_id'] = self.sub_seller_id
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        if self.transport:
            if hasattr(self.transport, 'to_alipay_dict'):
                params['transport'] = self.transport.to_alipay_dict()
            else:
                params['transport'] = self.transport
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.video_url:
            if hasattr(self.video_url, 'to_alipay_dict'):
                params['video_url'] = self.video_url.to_alipay_dict()
            else:
                params['video_url'] = self.video_url
        if self.web_site_url:
            if hasattr(self.web_site_url, 'to_alipay_dict'):
                params['web_site_url'] = self.web_site_url.to_alipay_dict()
            else:
                params['web_site_url'] = self.web_site_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PoiQueryResult()
        if 'address' in d:
            o.address = d['address']
        if 'address_en' in d:
            o.address_en = d['address_en']
        if 'address_local' in d:
            o.address_local = d['address_local']
        if 'alternative_phone' in d:
            o.alternative_phone = d['alternative_phone']
        if 'bios' in d:
            o.bios = d['bios']
        if 'brand_info' in d:
            o.brand_info = d['brand_info']
        if 'business_hour' in d:
            o.business_hour = d['business_hour']
        if 'category' in d:
            o.category = d['category']
        if 'city' in d:
            o.city = d['city']
        if 'commercial_circle' in d:
            o.commercial_circle = d['commercial_circle']
        if 'consumption' in d:
            o.consumption = d['consumption']
        if 'country_code' in d:
            o.country_code = d['country_code']
        if 'country_name' in d:
            o.country_name = d['country_name']
        if 'description' in d:
            o.description = d['description']
        if 'extend_map' in d:
            o.extend_map = d['extend_map']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'lat' in d:
            o.lat = d['lat']
        if 'lng' in d:
            o.lng = d['lng']
        if 'local_language' in d:
            o.local_language = d['local_language']
        if 'local_name' in d:
            o.local_name = d['local_name']
        if 'main_phone' in d:
            o.main_phone = d['main_phone']
        if 'name' in d:
            o.name = d['name']
        if 'name_alias' in d:
            o.name_alias = d['name_alias']
        if 'name_en' in d:
            o.name_en = d['name_en']
        if 'offline_reason_detail' in d:
            o.offline_reason_detail = d['offline_reason_detail']
        if 'open_status' in d:
            o.open_status = d['open_status']
        if 'open_time' in d:
            o.open_time = d['open_time']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'photo_urls' in d:
            o.photo_urls = d['photo_urls']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'postal_code' in d:
            o.postal_code = d['postal_code']
        if 'province' in d:
            o.province = d['province']
        if 'recommend_infos' in d:
            o.recommend_infos = d['recommend_infos']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'service_info' in d:
            o.service_info = d['service_info']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'source_biz_id' in d:
            o.source_biz_id = d['source_biz_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'sub_seller_id' in d:
            o.sub_seller_id = d['sub_seller_id']
        if 'telephone' in d:
            o.telephone = d['telephone']
        if 'transport' in d:
            o.transport = d['transport']
        if 'type' in d:
            o.type = d['type']
        if 'video_url' in d:
            o.video_url = d['video_url']
        if 'web_site_url' in d:
            o.web_site_url = d['web_site_url']
        return o


