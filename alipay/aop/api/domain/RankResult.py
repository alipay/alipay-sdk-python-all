#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RankCar import RankCar
from alipay.aop.api.domain.DetailInfo import DetailInfo


class RankResult(object):

    def __init__(self):
        self._brand_id = None
        self._brand_name = None
        self._car_list = None
        self._count = None
        self._descender_price = None
        self._detail_info = None
        self._image = None
        self._last_rank = None
        self._last_rank_value = None
        self._max_price = None
        self._min_price = None
        self._rank = None
        self._rank_data_type = None
        self._series_id = None
        self._series_name = None
        self._series_new_energy_type = None
        self._text = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def car_list(self):
        return self._car_list

    @car_list.setter
    def car_list(self, value):
        if isinstance(value, list):
            self._car_list = list()
            for i in value:
                if isinstance(i, RankCar):
                    self._car_list.append(i)
                else:
                    self._car_list.append(RankCar.from_alipay_dict(i))
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def descender_price(self):
        return self._descender_price

    @descender_price.setter
    def descender_price(self, value):
        self._descender_price = value
    @property
    def detail_info(self):
        return self._detail_info

    @detail_info.setter
    def detail_info(self, value):
        if isinstance(value, DetailInfo):
            self._detail_info = value
        else:
            self._detail_info = DetailInfo.from_alipay_dict(value)
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def last_rank(self):
        return self._last_rank

    @last_rank.setter
    def last_rank(self, value):
        self._last_rank = value
    @property
    def last_rank_value(self):
        return self._last_rank_value

    @last_rank_value.setter
    def last_rank_value(self, value):
        self._last_rank_value = value
    @property
    def max_price(self):
        return self._max_price

    @max_price.setter
    def max_price(self, value):
        self._max_price = value
    @property
    def min_price(self):
        return self._min_price

    @min_price.setter
    def min_price(self, value):
        self._min_price = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def rank_data_type(self):
        return self._rank_data_type

    @rank_data_type.setter
    def rank_data_type(self, value):
        self._rank_data_type = value
    @property
    def series_id(self):
        return self._series_id

    @series_id.setter
    def series_id(self, value):
        self._series_id = value
    @property
    def series_name(self):
        return self._series_name

    @series_name.setter
    def series_name(self, value):
        self._series_name = value
    @property
    def series_new_energy_type(self):
        return self._series_new_energy_type

    @series_new_energy_type.setter
    def series_new_energy_type(self, value):
        self._series_new_energy_type = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.car_list:
            if isinstance(self.car_list, list):
                for i in range(0, len(self.car_list)):
                    element = self.car_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.car_list[i] = element.to_alipay_dict()
            if hasattr(self.car_list, 'to_alipay_dict'):
                params['car_list'] = self.car_list.to_alipay_dict()
            else:
                params['car_list'] = self.car_list
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.descender_price:
            if hasattr(self.descender_price, 'to_alipay_dict'):
                params['descender_price'] = self.descender_price.to_alipay_dict()
            else:
                params['descender_price'] = self.descender_price
        if self.detail_info:
            if hasattr(self.detail_info, 'to_alipay_dict'):
                params['detail_info'] = self.detail_info.to_alipay_dict()
            else:
                params['detail_info'] = self.detail_info
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.last_rank:
            if hasattr(self.last_rank, 'to_alipay_dict'):
                params['last_rank'] = self.last_rank.to_alipay_dict()
            else:
                params['last_rank'] = self.last_rank
        if self.last_rank_value:
            if hasattr(self.last_rank_value, 'to_alipay_dict'):
                params['last_rank_value'] = self.last_rank_value.to_alipay_dict()
            else:
                params['last_rank_value'] = self.last_rank_value
        if self.max_price:
            if hasattr(self.max_price, 'to_alipay_dict'):
                params['max_price'] = self.max_price.to_alipay_dict()
            else:
                params['max_price'] = self.max_price
        if self.min_price:
            if hasattr(self.min_price, 'to_alipay_dict'):
                params['min_price'] = self.min_price.to_alipay_dict()
            else:
                params['min_price'] = self.min_price
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.rank_data_type:
            if hasattr(self.rank_data_type, 'to_alipay_dict'):
                params['rank_data_type'] = self.rank_data_type.to_alipay_dict()
            else:
                params['rank_data_type'] = self.rank_data_type
        if self.series_id:
            if hasattr(self.series_id, 'to_alipay_dict'):
                params['series_id'] = self.series_id.to_alipay_dict()
            else:
                params['series_id'] = self.series_id
        if self.series_name:
            if hasattr(self.series_name, 'to_alipay_dict'):
                params['series_name'] = self.series_name.to_alipay_dict()
            else:
                params['series_name'] = self.series_name
        if self.series_new_energy_type:
            if hasattr(self.series_new_energy_type, 'to_alipay_dict'):
                params['series_new_energy_type'] = self.series_new_energy_type.to_alipay_dict()
            else:
                params['series_new_energy_type'] = self.series_new_energy_type
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RankResult()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'car_list' in d:
            o.car_list = d['car_list']
        if 'count' in d:
            o.count = d['count']
        if 'descender_price' in d:
            o.descender_price = d['descender_price']
        if 'detail_info' in d:
            o.detail_info = d['detail_info']
        if 'image' in d:
            o.image = d['image']
        if 'last_rank' in d:
            o.last_rank = d['last_rank']
        if 'last_rank_value' in d:
            o.last_rank_value = d['last_rank_value']
        if 'max_price' in d:
            o.max_price = d['max_price']
        if 'min_price' in d:
            o.min_price = d['min_price']
        if 'rank' in d:
            o.rank = d['rank']
        if 'rank_data_type' in d:
            o.rank_data_type = d['rank_data_type']
        if 'series_id' in d:
            o.series_id = d['series_id']
        if 'series_name' in d:
            o.series_name = d['series_name']
        if 'series_new_energy_type' in d:
            o.series_new_energy_type = d['series_new_energy_type']
        if 'text' in d:
            o.text = d['text']
        return o


