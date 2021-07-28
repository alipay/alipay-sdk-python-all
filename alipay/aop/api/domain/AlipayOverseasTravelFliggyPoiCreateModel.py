#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FliggyPoiInfo import FliggyPoiInfo


class AlipayOverseasTravelFliggyPoiCreateModel(object):

    def __init__(self):
        self._data_version = None
        self._ext_info = None
        self._global_shop_id = None
        self._poi_data = None
        self._request_id = None
        self._task_subtype = None

    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def global_shop_id(self):
        return self._global_shop_id

    @global_shop_id.setter
    def global_shop_id(self, value):
        self._global_shop_id = value
    @property
    def poi_data(self):
        return self._poi_data

    @poi_data.setter
    def poi_data(self, value):
        if isinstance(value, FliggyPoiInfo):
            self._poi_data = value
        else:
            self._poi_data = FliggyPoiInfo.from_alipay_dict(value)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def task_subtype(self):
        return self._task_subtype

    @task_subtype.setter
    def task_subtype(self, value):
        self._task_subtype = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.global_shop_id:
            if hasattr(self.global_shop_id, 'to_alipay_dict'):
                params['global_shop_id'] = self.global_shop_id.to_alipay_dict()
            else:
                params['global_shop_id'] = self.global_shop_id
        if self.poi_data:
            if hasattr(self.poi_data, 'to_alipay_dict'):
                params['poi_data'] = self.poi_data.to_alipay_dict()
            else:
                params['poi_data'] = self.poi_data
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.task_subtype:
            if hasattr(self.task_subtype, 'to_alipay_dict'):
                params['task_subtype'] = self.task_subtype.to_alipay_dict()
            else:
                params['task_subtype'] = self.task_subtype
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelFliggyPoiCreateModel()
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'global_shop_id' in d:
            o.global_shop_id = d['global_shop_id']
        if 'poi_data' in d:
            o.poi_data = d['poi_data']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'task_subtype' in d:
            o.task_subtype = d['task_subtype']
        return o


