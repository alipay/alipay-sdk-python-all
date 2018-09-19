#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductProvider(object):

    def __init__(self):
        self._agency = None
        self._agency_name = None
        self._biz_type = None
        self._id = None
        self._sub_biz_type = None
        self._sub_operator = None
        self._sub_operator_name = None

    @property
    def agency(self):
        return self._agency

    @agency.setter
    def agency(self, value):
        self._agency = value
    @property
    def agency_name(self):
        return self._agency_name

    @agency_name.setter
    def agency_name(self, value):
        self._agency_name = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def sub_operator(self):
        return self._sub_operator

    @sub_operator.setter
    def sub_operator(self, value):
        self._sub_operator = value
    @property
    def sub_operator_name(self):
        return self._sub_operator_name

    @sub_operator_name.setter
    def sub_operator_name(self, value):
        self._sub_operator_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.agency:
            if hasattr(self.agency, 'to_alipay_dict'):
                params['agency'] = self.agency.to_alipay_dict()
            else:
                params['agency'] = self.agency
        if self.agency_name:
            if hasattr(self.agency_name, 'to_alipay_dict'):
                params['agency_name'] = self.agency_name.to_alipay_dict()
            else:
                params['agency_name'] = self.agency_name
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        if self.sub_operator:
            if hasattr(self.sub_operator, 'to_alipay_dict'):
                params['sub_operator'] = self.sub_operator.to_alipay_dict()
            else:
                params['sub_operator'] = self.sub_operator
        if self.sub_operator_name:
            if hasattr(self.sub_operator_name, 'to_alipay_dict'):
                params['sub_operator_name'] = self.sub_operator_name.to_alipay_dict()
            else:
                params['sub_operator_name'] = self.sub_operator_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductProvider()
        if 'agency' in d:
            o.agency = d['agency']
        if 'agency_name' in d:
            o.agency_name = d['agency_name']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'id' in d:
            o.id = d['id']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'sub_operator' in d:
            o.sub_operator = d['sub_operator']
        if 'sub_operator_name' in d:
            o.sub_operator_name = d['sub_operator_name']
        return o


