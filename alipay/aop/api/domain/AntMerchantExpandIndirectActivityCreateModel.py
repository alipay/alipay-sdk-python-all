#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandIndirectActivityCreateModel(object):

    def __init__(self):
        self._activity_type = None
        self._alias_name = None
        self._business_license_pic = None
        self._checkstand_pic = None
        self._indoor_pic = None
        self._name = None
        self._settled_pic = None
        self._shop_entrance_pic = None
        self._sub_merchant_id = None

    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def alias_name(self):
        return self._alias_name

    @alias_name.setter
    def alias_name(self, value):
        self._alias_name = value
    @property
    def business_license_pic(self):
        return self._business_license_pic

    @business_license_pic.setter
    def business_license_pic(self, value):
        self._business_license_pic = value
    @property
    def checkstand_pic(self):
        return self._checkstand_pic

    @checkstand_pic.setter
    def checkstand_pic(self, value):
        self._checkstand_pic = value
    @property
    def indoor_pic(self):
        return self._indoor_pic

    @indoor_pic.setter
    def indoor_pic(self, value):
        self._indoor_pic = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def settled_pic(self):
        return self._settled_pic

    @settled_pic.setter
    def settled_pic(self, value):
        self._settled_pic = value
    @property
    def shop_entrance_pic(self):
        return self._shop_entrance_pic

    @shop_entrance_pic.setter
    def shop_entrance_pic(self, value):
        self._shop_entrance_pic = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.alias_name:
            if hasattr(self.alias_name, 'to_alipay_dict'):
                params['alias_name'] = self.alias_name.to_alipay_dict()
            else:
                params['alias_name'] = self.alias_name
        if self.business_license_pic:
            if hasattr(self.business_license_pic, 'to_alipay_dict'):
                params['business_license_pic'] = self.business_license_pic.to_alipay_dict()
            else:
                params['business_license_pic'] = self.business_license_pic
        if self.checkstand_pic:
            if hasattr(self.checkstand_pic, 'to_alipay_dict'):
                params['checkstand_pic'] = self.checkstand_pic.to_alipay_dict()
            else:
                params['checkstand_pic'] = self.checkstand_pic
        if self.indoor_pic:
            if hasattr(self.indoor_pic, 'to_alipay_dict'):
                params['indoor_pic'] = self.indoor_pic.to_alipay_dict()
            else:
                params['indoor_pic'] = self.indoor_pic
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.settled_pic:
            if hasattr(self.settled_pic, 'to_alipay_dict'):
                params['settled_pic'] = self.settled_pic.to_alipay_dict()
            else:
                params['settled_pic'] = self.settled_pic
        if self.shop_entrance_pic:
            if hasattr(self.shop_entrance_pic, 'to_alipay_dict'):
                params['shop_entrance_pic'] = self.shop_entrance_pic.to_alipay_dict()
            else:
                params['shop_entrance_pic'] = self.shop_entrance_pic
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectActivityCreateModel()
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'alias_name' in d:
            o.alias_name = d['alias_name']
        if 'business_license_pic' in d:
            o.business_license_pic = d['business_license_pic']
        if 'checkstand_pic' in d:
            o.checkstand_pic = d['checkstand_pic']
        if 'indoor_pic' in d:
            o.indoor_pic = d['indoor_pic']
        if 'name' in d:
            o.name = d['name']
        if 'settled_pic' in d:
            o.settled_pic = d['settled_pic']
        if 'shop_entrance_pic' in d:
            o.shop_entrance_pic = d['shop_entrance_pic']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        return o


