#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftCtocAssetQueryModel(object):

    def __init__(self):
        self._access_token = None
        self._id_no = None
        self._id_type = None
        self._last_index = None
        self._sku_id_list = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def id_no(self):
        return self._id_no

    @id_no.setter
    def id_no(self, value):
        self._id_no = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def last_index(self):
        return self._last_index

    @last_index.setter
    def last_index(self, value):
        self._last_index = value
    @property
    def sku_id_list(self):
        return self._sku_id_list

    @sku_id_list.setter
    def sku_id_list(self, value):
        if isinstance(value, list):
            self._sku_id_list = list()
            for i in value:
                self._sku_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        if self.id_no:
            if hasattr(self.id_no, 'to_alipay_dict'):
                params['id_no'] = self.id_no.to_alipay_dict()
            else:
                params['id_no'] = self.id_no
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.last_index:
            if hasattr(self.last_index, 'to_alipay_dict'):
                params['last_index'] = self.last_index.to_alipay_dict()
            else:
                params['last_index'] = self.last_index
        if self.sku_id_list:
            if isinstance(self.sku_id_list, list):
                for i in range(0, len(self.sku_id_list)):
                    element = self.sku_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_id_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_id_list, 'to_alipay_dict'):
                params['sku_id_list'] = self.sku_id_list.to_alipay_dict()
            else:
                params['sku_id_list'] = self.sku_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftCtocAssetQueryModel()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'id_no' in d:
            o.id_no = d['id_no']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'last_index' in d:
            o.last_index = d['last_index']
        if 'sku_id_list' in d:
            o.sku_id_list = d['sku_id_list']
        return o


