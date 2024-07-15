#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HouseMode import HouseMode


class AlipayEbppCommunityAffordrentalhouseUploadModel(object):

    def __init__(self):
        self._address = None
        self._city_code = None
        self._detail_url = None
        self._house_mode_list = None
        self._house_mode_num = None
        self._house_num = None
        self._lat = None
        self._lng = None
        self._source = None
        self._source_id = None
        self._source_name = None
        self._status = None
        self._tel = None
        self._title = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def house_mode_list(self):
        return self._house_mode_list

    @house_mode_list.setter
    def house_mode_list(self, value):
        if isinstance(value, list):
            self._house_mode_list = list()
            for i in value:
                if isinstance(i, HouseMode):
                    self._house_mode_list.append(i)
                else:
                    self._house_mode_list.append(HouseMode.from_alipay_dict(i))
    @property
    def house_mode_num(self):
        return self._house_mode_num

    @house_mode_num.setter
    def house_mode_num(self, value):
        self._house_mode_num = value
    @property
    def house_num(self):
        return self._house_num

    @house_num.setter
    def house_num(self, value):
        self._house_num = value
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
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def source_name(self):
        return self._source_name

    @source_name.setter
    def source_name(self, value):
        self._source_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, value):
        self._tel = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.house_mode_list:
            if isinstance(self.house_mode_list, list):
                for i in range(0, len(self.house_mode_list)):
                    element = self.house_mode_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.house_mode_list[i] = element.to_alipay_dict()
            if hasattr(self.house_mode_list, 'to_alipay_dict'):
                params['house_mode_list'] = self.house_mode_list.to_alipay_dict()
            else:
                params['house_mode_list'] = self.house_mode_list
        if self.house_mode_num:
            if hasattr(self.house_mode_num, 'to_alipay_dict'):
                params['house_mode_num'] = self.house_mode_num.to_alipay_dict()
            else:
                params['house_mode_num'] = self.house_mode_num
        if self.house_num:
            if hasattr(self.house_num, 'to_alipay_dict'):
                params['house_num'] = self.house_num.to_alipay_dict()
            else:
                params['house_num'] = self.house_num
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
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.source_name:
            if hasattr(self.source_name, 'to_alipay_dict'):
                params['source_name'] = self.source_name.to_alipay_dict()
            else:
                params['source_name'] = self.source_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tel:
            if hasattr(self.tel, 'to_alipay_dict'):
                params['tel'] = self.tel.to_alipay_dict()
            else:
                params['tel'] = self.tel
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
        o = AlipayEbppCommunityAffordrentalhouseUploadModel()
        if 'address' in d:
            o.address = d['address']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'house_mode_list' in d:
            o.house_mode_list = d['house_mode_list']
        if 'house_mode_num' in d:
            o.house_mode_num = d['house_mode_num']
        if 'house_num' in d:
            o.house_num = d['house_num']
        if 'lat' in d:
            o.lat = d['lat']
        if 'lng' in d:
            o.lng = d['lng']
        if 'source' in d:
            o.source = d['source']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'source_name' in d:
            o.source_name = d['source_name']
        if 'status' in d:
            o.status = d['status']
        if 'tel' in d:
            o.tel = d['tel']
        if 'title' in d:
            o.title = d['title']
        return o


