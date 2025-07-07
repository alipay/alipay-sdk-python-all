#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopExtInfo import ShopExtInfo


class AntMerchantExpandAeactivityPlatformSignupModel(object):

    def __init__(self):
        self._catering_url = None
        self._ele_address = None
        self._ele_brand_id = None
        self._ele_brand_name = None
        self._ele_category_1 = None
        self._ele_category_2 = None
        self._ele_latitude = None
        self._ele_longitude = None
        self._ele_outdoor_pic_url = None
        self._ele_phone = None
        self._ele_shop_name = None
        self._ele_shopid = None
        self._ext_info = None
        self._sn_code = None

    @property
    def catering_url(self):
        return self._catering_url

    @catering_url.setter
    def catering_url(self, value):
        self._catering_url = value
    @property
    def ele_address(self):
        return self._ele_address

    @ele_address.setter
    def ele_address(self, value):
        self._ele_address = value
    @property
    def ele_brand_id(self):
        return self._ele_brand_id

    @ele_brand_id.setter
    def ele_brand_id(self, value):
        self._ele_brand_id = value
    @property
    def ele_brand_name(self):
        return self._ele_brand_name

    @ele_brand_name.setter
    def ele_brand_name(self, value):
        self._ele_brand_name = value
    @property
    def ele_category_1(self):
        return self._ele_category_1

    @ele_category_1.setter
    def ele_category_1(self, value):
        self._ele_category_1 = value
    @property
    def ele_category_2(self):
        return self._ele_category_2

    @ele_category_2.setter
    def ele_category_2(self, value):
        self._ele_category_2 = value
    @property
    def ele_latitude(self):
        return self._ele_latitude

    @ele_latitude.setter
    def ele_latitude(self, value):
        self._ele_latitude = value
    @property
    def ele_longitude(self):
        return self._ele_longitude

    @ele_longitude.setter
    def ele_longitude(self, value):
        self._ele_longitude = value
    @property
    def ele_outdoor_pic_url(self):
        return self._ele_outdoor_pic_url

    @ele_outdoor_pic_url.setter
    def ele_outdoor_pic_url(self, value):
        self._ele_outdoor_pic_url = value
    @property
    def ele_phone(self):
        return self._ele_phone

    @ele_phone.setter
    def ele_phone(self, value):
        self._ele_phone = value
    @property
    def ele_shop_name(self):
        return self._ele_shop_name

    @ele_shop_name.setter
    def ele_shop_name(self, value):
        self._ele_shop_name = value
    @property
    def ele_shopid(self):
        return self._ele_shopid

    @ele_shopid.setter
    def ele_shopid(self, value):
        self._ele_shopid = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ShopExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ShopExtInfo.from_alipay_dict(i))
    @property
    def sn_code(self):
        return self._sn_code

    @sn_code.setter
    def sn_code(self, value):
        self._sn_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.catering_url:
            if hasattr(self.catering_url, 'to_alipay_dict'):
                params['catering_url'] = self.catering_url.to_alipay_dict()
            else:
                params['catering_url'] = self.catering_url
        if self.ele_address:
            if hasattr(self.ele_address, 'to_alipay_dict'):
                params['ele_address'] = self.ele_address.to_alipay_dict()
            else:
                params['ele_address'] = self.ele_address
        if self.ele_brand_id:
            if hasattr(self.ele_brand_id, 'to_alipay_dict'):
                params['ele_brand_id'] = self.ele_brand_id.to_alipay_dict()
            else:
                params['ele_brand_id'] = self.ele_brand_id
        if self.ele_brand_name:
            if hasattr(self.ele_brand_name, 'to_alipay_dict'):
                params['ele_brand_name'] = self.ele_brand_name.to_alipay_dict()
            else:
                params['ele_brand_name'] = self.ele_brand_name
        if self.ele_category_1:
            if hasattr(self.ele_category_1, 'to_alipay_dict'):
                params['ele_category_1'] = self.ele_category_1.to_alipay_dict()
            else:
                params['ele_category_1'] = self.ele_category_1
        if self.ele_category_2:
            if hasattr(self.ele_category_2, 'to_alipay_dict'):
                params['ele_category_2'] = self.ele_category_2.to_alipay_dict()
            else:
                params['ele_category_2'] = self.ele_category_2
        if self.ele_latitude:
            if hasattr(self.ele_latitude, 'to_alipay_dict'):
                params['ele_latitude'] = self.ele_latitude.to_alipay_dict()
            else:
                params['ele_latitude'] = self.ele_latitude
        if self.ele_longitude:
            if hasattr(self.ele_longitude, 'to_alipay_dict'):
                params['ele_longitude'] = self.ele_longitude.to_alipay_dict()
            else:
                params['ele_longitude'] = self.ele_longitude
        if self.ele_outdoor_pic_url:
            if hasattr(self.ele_outdoor_pic_url, 'to_alipay_dict'):
                params['ele_outdoor_pic_url'] = self.ele_outdoor_pic_url.to_alipay_dict()
            else:
                params['ele_outdoor_pic_url'] = self.ele_outdoor_pic_url
        if self.ele_phone:
            if hasattr(self.ele_phone, 'to_alipay_dict'):
                params['ele_phone'] = self.ele_phone.to_alipay_dict()
            else:
                params['ele_phone'] = self.ele_phone
        if self.ele_shop_name:
            if hasattr(self.ele_shop_name, 'to_alipay_dict'):
                params['ele_shop_name'] = self.ele_shop_name.to_alipay_dict()
            else:
                params['ele_shop_name'] = self.ele_shop_name
        if self.ele_shopid:
            if hasattr(self.ele_shopid, 'to_alipay_dict'):
                params['ele_shopid'] = self.ele_shopid.to_alipay_dict()
            else:
                params['ele_shopid'] = self.ele_shopid
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.sn_code:
            if hasattr(self.sn_code, 'to_alipay_dict'):
                params['sn_code'] = self.sn_code.to_alipay_dict()
            else:
                params['sn_code'] = self.sn_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAeactivityPlatformSignupModel()
        if 'catering_url' in d:
            o.catering_url = d['catering_url']
        if 'ele_address' in d:
            o.ele_address = d['ele_address']
        if 'ele_brand_id' in d:
            o.ele_brand_id = d['ele_brand_id']
        if 'ele_brand_name' in d:
            o.ele_brand_name = d['ele_brand_name']
        if 'ele_category_1' in d:
            o.ele_category_1 = d['ele_category_1']
        if 'ele_category_2' in d:
            o.ele_category_2 = d['ele_category_2']
        if 'ele_latitude' in d:
            o.ele_latitude = d['ele_latitude']
        if 'ele_longitude' in d:
            o.ele_longitude = d['ele_longitude']
        if 'ele_outdoor_pic_url' in d:
            o.ele_outdoor_pic_url = d['ele_outdoor_pic_url']
        if 'ele_phone' in d:
            o.ele_phone = d['ele_phone']
        if 'ele_shop_name' in d:
            o.ele_shop_name = d['ele_shop_name']
        if 'ele_shopid' in d:
            o.ele_shopid = d['ele_shopid']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'sn_code' in d:
            o.sn_code = d['sn_code']
        return o


