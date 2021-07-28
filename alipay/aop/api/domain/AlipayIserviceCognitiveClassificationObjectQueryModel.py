#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCognitiveClassificationObjectQueryModel(object):

    def __init__(self):
        self._biz_code = None
        self._city_code = None
        self._cognition_content = None
        self._cognition_type = None
        self._group_id = None
        self._latitude = None
        self._longitude = None
        self._service_code = None
        self._test_query = None
        self._user_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def cognition_content(self):
        return self._cognition_content

    @cognition_content.setter
    def cognition_content(self, value):
        self._cognition_content = value
    @property
    def cognition_type(self):
        return self._cognition_type

    @cognition_type.setter
    def cognition_type(self, value):
        self._cognition_type = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
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
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def test_query(self):
        return self._test_query

    @test_query.setter
    def test_query(self, value):
        self._test_query = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.cognition_content:
            if hasattr(self.cognition_content, 'to_alipay_dict'):
                params['cognition_content'] = self.cognition_content.to_alipay_dict()
            else:
                params['cognition_content'] = self.cognition_content
        if self.cognition_type:
            if hasattr(self.cognition_type, 'to_alipay_dict'):
                params['cognition_type'] = self.cognition_type.to_alipay_dict()
            else:
                params['cognition_type'] = self.cognition_type
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
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
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.test_query:
            if hasattr(self.test_query, 'to_alipay_dict'):
                params['test_query'] = self.test_query.to_alipay_dict()
            else:
                params['test_query'] = self.test_query
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCognitiveClassificationObjectQueryModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'cognition_content' in d:
            o.cognition_content = d['cognition_content']
        if 'cognition_type' in d:
            o.cognition_type = d['cognition_type']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'test_query' in d:
            o.test_query = d['test_query']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


