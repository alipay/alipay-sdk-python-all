#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoCustomrouteCreateormodifyModel(object):

    def __init__(self):
        self._cur_lbs_poi = None
        self._item_id = None
        self._poi_info_id_list = None
        self._request_id = None
        self._route_id = None

    @property
    def cur_lbs_poi(self):
        return self._cur_lbs_poi

    @cur_lbs_poi.setter
    def cur_lbs_poi(self, value):
        self._cur_lbs_poi = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def poi_info_id_list(self):
        return self._poi_info_id_list

    @poi_info_id_list.setter
    def poi_info_id_list(self, value):
        if isinstance(value, list):
            self._poi_info_id_list = list()
            for i in value:
                self._poi_info_id_list.append(i)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def route_id(self):
        return self._route_id

    @route_id.setter
    def route_id(self, value):
        self._route_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cur_lbs_poi:
            if hasattr(self.cur_lbs_poi, 'to_alipay_dict'):
                params['cur_lbs_poi'] = self.cur_lbs_poi.to_alipay_dict()
            else:
                params['cur_lbs_poi'] = self.cur_lbs_poi
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.poi_info_id_list:
            if isinstance(self.poi_info_id_list, list):
                for i in range(0, len(self.poi_info_id_list)):
                    element = self.poi_info_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.poi_info_id_list[i] = element.to_alipay_dict()
            if hasattr(self.poi_info_id_list, 'to_alipay_dict'):
                params['poi_info_id_list'] = self.poi_info_id_list.to_alipay_dict()
            else:
                params['poi_info_id_list'] = self.poi_info_id_list
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.route_id:
            if hasattr(self.route_id, 'to_alipay_dict'):
                params['route_id'] = self.route_id.to_alipay_dict()
            else:
                params['route_id'] = self.route_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoCustomrouteCreateormodifyModel()
        if 'cur_lbs_poi' in d:
            o.cur_lbs_poi = d['cur_lbs_poi']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'poi_info_id_list' in d:
            o.poi_info_id_list = d['poi_info_id_list']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'route_id' in d:
            o.route_id = d['route_id']
        return o


