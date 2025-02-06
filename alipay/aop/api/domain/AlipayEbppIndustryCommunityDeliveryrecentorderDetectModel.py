#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryCommunityDeliveryrecentorderDetectModel(object):

    def __init__(self):
        self._city_code = None
        self._community_name = None
        self._company_code = None
        self._company_name = None
        self._delivery_open_id = None
        self._delivery_user_id = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def community_name(self):
        return self._community_name

    @community_name.setter
    def community_name(self, value):
        self._community_name = value
    @property
    def company_code(self):
        return self._company_code

    @company_code.setter
    def company_code(self, value):
        self._company_code = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def delivery_open_id(self):
        return self._delivery_open_id

    @delivery_open_id.setter
    def delivery_open_id(self, value):
        self._delivery_open_id = value
    @property
    def delivery_user_id(self):
        return self._delivery_user_id

    @delivery_user_id.setter
    def delivery_user_id(self, value):
        self._delivery_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.community_name:
            if hasattr(self.community_name, 'to_alipay_dict'):
                params['community_name'] = self.community_name.to_alipay_dict()
            else:
                params['community_name'] = self.community_name
        if self.company_code:
            if hasattr(self.company_code, 'to_alipay_dict'):
                params['company_code'] = self.company_code.to_alipay_dict()
            else:
                params['company_code'] = self.company_code
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.delivery_open_id:
            if hasattr(self.delivery_open_id, 'to_alipay_dict'):
                params['delivery_open_id'] = self.delivery_open_id.to_alipay_dict()
            else:
                params['delivery_open_id'] = self.delivery_open_id
        if self.delivery_user_id:
            if hasattr(self.delivery_user_id, 'to_alipay_dict'):
                params['delivery_user_id'] = self.delivery_user_id.to_alipay_dict()
            else:
                params['delivery_user_id'] = self.delivery_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCommunityDeliveryrecentorderDetectModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'community_name' in d:
            o.community_name = d['community_name']
        if 'company_code' in d:
            o.company_code = d['company_code']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'delivery_open_id' in d:
            o.delivery_open_id = d['delivery_open_id']
        if 'delivery_user_id' in d:
            o.delivery_user_id = d['delivery_user_id']
        return o


