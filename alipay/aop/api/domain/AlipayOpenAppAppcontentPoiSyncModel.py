#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Attribute import Attribute


class AlipayOpenAppAppcontentPoiSyncModel(object):

    def __init__(self):
        self._address = None
        self._alipay_url = None
        self._amap_poi_id = None
        self._attributes = None
        self._biz_source = None
        self._biz_unique_id = None
        self._contact_name = None
        self._contact_tele = None
        self._latitude = None
        self._logo = None
        self._longitude = None
        self._name = None
        self._photos = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def alipay_url(self):
        return self._alipay_url

    @alipay_url.setter
    def alipay_url(self, value):
        self._alipay_url = value
    @property
    def amap_poi_id(self):
        return self._amap_poi_id

    @amap_poi_id.setter
    def amap_poi_id(self, value):
        self._amap_poi_id = value
    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        if isinstance(value, list):
            self._attributes = list()
            for i in value:
                if isinstance(i, Attribute):
                    self._attributes.append(i)
                else:
                    self._attributes.append(Attribute.from_alipay_dict(i))
    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def biz_unique_id(self):
        return self._biz_unique_id

    @biz_unique_id.setter
    def biz_unique_id(self, value):
        self._biz_unique_id = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_tele(self):
        return self._contact_tele

    @contact_tele.setter
    def contact_tele(self, value):
        self._contact_tele = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def photos(self):
        return self._photos

    @photos.setter
    def photos(self, value):
        if isinstance(value, list):
            self._photos = list()
            for i in value:
                self._photos.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.alipay_url:
            if hasattr(self.alipay_url, 'to_alipay_dict'):
                params['alipay_url'] = self.alipay_url.to_alipay_dict()
            else:
                params['alipay_url'] = self.alipay_url
        if self.amap_poi_id:
            if hasattr(self.amap_poi_id, 'to_alipay_dict'):
                params['amap_poi_id'] = self.amap_poi_id.to_alipay_dict()
            else:
                params['amap_poi_id'] = self.amap_poi_id
        if self.attributes:
            if isinstance(self.attributes, list):
                for i in range(0, len(self.attributes)):
                    element = self.attributes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attributes[i] = element.to_alipay_dict()
            if hasattr(self.attributes, 'to_alipay_dict'):
                params['attributes'] = self.attributes.to_alipay_dict()
            else:
                params['attributes'] = self.attributes
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.biz_unique_id:
            if hasattr(self.biz_unique_id, 'to_alipay_dict'):
                params['biz_unique_id'] = self.biz_unique_id.to_alipay_dict()
            else:
                params['biz_unique_id'] = self.biz_unique_id
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_tele:
            if hasattr(self.contact_tele, 'to_alipay_dict'):
                params['contact_tele'] = self.contact_tele.to_alipay_dict()
            else:
                params['contact_tele'] = self.contact_tele
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.photos:
            if isinstance(self.photos, list):
                for i in range(0, len(self.photos)):
                    element = self.photos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.photos[i] = element.to_alipay_dict()
            if hasattr(self.photos, 'to_alipay_dict'):
                params['photos'] = self.photos.to_alipay_dict()
            else:
                params['photos'] = self.photos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppAppcontentPoiSyncModel()
        if 'address' in d:
            o.address = d['address']
        if 'alipay_url' in d:
            o.alipay_url = d['alipay_url']
        if 'amap_poi_id' in d:
            o.amap_poi_id = d['amap_poi_id']
        if 'attributes' in d:
            o.attributes = d['attributes']
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'biz_unique_id' in d:
            o.biz_unique_id = d['biz_unique_id']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_tele' in d:
            o.contact_tele = d['contact_tele']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'logo' in d:
            o.logo = d['logo']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'name' in d:
            o.name = d['name']
        if 'photos' in d:
            o.photos = d['photos']
        return o


