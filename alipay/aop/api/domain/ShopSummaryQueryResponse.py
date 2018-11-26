#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopCategoryInfo import ShopCategoryInfo
from alipay.aop.api.domain.ShopCommentInfo import ShopCommentInfo


class ShopSummaryQueryResponse(object):

    def __init__(self):
        self._address = None
        self._branch_shop_name = None
        self._brand_name = None
        self._business_time = None
        self._category_infos = None
        self._city_code = None
        self._district_code = None
        self._ext_info = None
        self._gmt_create = None
        self._is_show = None
        self._latitude = None
        self._longitude = None
        self._main_image = None
        self._main_shop_name = None
        self._per_pay = None
        self._pic_coll = None
        self._province_code = None
        self._shop_comment_info = None
        self._shop_id = None
        self._shop_type = None
        self._status = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def branch_shop_name(self):
        return self._branch_shop_name

    @branch_shop_name.setter
    def branch_shop_name(self, value):
        self._branch_shop_name = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        self._business_time = value
    @property
    def category_infos(self):
        return self._category_infos

    @category_infos.setter
    def category_infos(self, value):
        if isinstance(value, list):
            self._category_infos = list()
            for i in value:
                if isinstance(i, ShopCategoryInfo):
                    self._category_infos.append(i)
                else:
                    self._category_infos.append(ShopCategoryInfo.from_alipay_dict(i))
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def is_show(self):
        return self._is_show

    @is_show.setter
    def is_show(self, value):
        self._is_show = value
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
    def main_image(self):
        return self._main_image

    @main_image.setter
    def main_image(self, value):
        self._main_image = value
    @property
    def main_shop_name(self):
        return self._main_shop_name

    @main_shop_name.setter
    def main_shop_name(self, value):
        self._main_shop_name = value
    @property
    def per_pay(self):
        return self._per_pay

    @per_pay.setter
    def per_pay(self, value):
        self._per_pay = value
    @property
    def pic_coll(self):
        return self._pic_coll

    @pic_coll.setter
    def pic_coll(self, value):
        self._pic_coll = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def shop_comment_info(self):
        return self._shop_comment_info

    @shop_comment_info.setter
    def shop_comment_info(self, value):
        if isinstance(value, ShopCommentInfo):
            self._shop_comment_info = value
        else:
            self._shop_comment_info = ShopCommentInfo.from_alipay_dict(value)
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.branch_shop_name:
            if hasattr(self.branch_shop_name, 'to_alipay_dict'):
                params['branch_shop_name'] = self.branch_shop_name.to_alipay_dict()
            else:
                params['branch_shop_name'] = self.branch_shop_name
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.business_time:
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        if self.category_infos:
            if isinstance(self.category_infos, list):
                for i in range(0, len(self.category_infos)):
                    element = self.category_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_infos[i] = element.to_alipay_dict()
            if hasattr(self.category_infos, 'to_alipay_dict'):
                params['category_infos'] = self.category_infos.to_alipay_dict()
            else:
                params['category_infos'] = self.category_infos
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.is_show:
            if hasattr(self.is_show, 'to_alipay_dict'):
                params['is_show'] = self.is_show.to_alipay_dict()
            else:
                params['is_show'] = self.is_show
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
        if self.main_image:
            if hasattr(self.main_image, 'to_alipay_dict'):
                params['main_image'] = self.main_image.to_alipay_dict()
            else:
                params['main_image'] = self.main_image
        if self.main_shop_name:
            if hasattr(self.main_shop_name, 'to_alipay_dict'):
                params['main_shop_name'] = self.main_shop_name.to_alipay_dict()
            else:
                params['main_shop_name'] = self.main_shop_name
        if self.per_pay:
            if hasattr(self.per_pay, 'to_alipay_dict'):
                params['per_pay'] = self.per_pay.to_alipay_dict()
            else:
                params['per_pay'] = self.per_pay
        if self.pic_coll:
            if hasattr(self.pic_coll, 'to_alipay_dict'):
                params['pic_coll'] = self.pic_coll.to_alipay_dict()
            else:
                params['pic_coll'] = self.pic_coll
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.shop_comment_info:
            if hasattr(self.shop_comment_info, 'to_alipay_dict'):
                params['shop_comment_info'] = self.shop_comment_info.to_alipay_dict()
            else:
                params['shop_comment_info'] = self.shop_comment_info
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopSummaryQueryResponse()
        if 'address' in d:
            o.address = d['address']
        if 'branch_shop_name' in d:
            o.branch_shop_name = d['branch_shop_name']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'category_infos' in d:
            o.category_infos = d['category_infos']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'is_show' in d:
            o.is_show = d['is_show']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'main_image' in d:
            o.main_image = d['main_image']
        if 'main_shop_name' in d:
            o.main_shop_name = d['main_shop_name']
        if 'per_pay' in d:
            o.per_pay = d['per_pay']
        if 'pic_coll' in d:
            o.pic_coll = d['pic_coll']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'shop_comment_info' in d:
            o.shop_comment_info = d['shop_comment_info']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'status' in d:
            o.status = d['status']
        return o


