#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoRoutePolylineQueryModel(object):

    def __init__(self):
        self._cur_lbs_poi = None
        self._dest = None
        self._dest_lbs_poi = None
        self._item_id = None
        self._source = None
        self._type = None

    @property
    def cur_lbs_poi(self):
        return self._cur_lbs_poi

    @cur_lbs_poi.setter
    def cur_lbs_poi(self, value):
        self._cur_lbs_poi = value
    @property
    def dest(self):
        return self._dest

    @dest.setter
    def dest(self, value):
        self._dest = value
    @property
    def dest_lbs_poi(self):
        return self._dest_lbs_poi

    @dest_lbs_poi.setter
    def dest_lbs_poi(self, value):
        self._dest_lbs_poi = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cur_lbs_poi:
            if hasattr(self.cur_lbs_poi, 'to_alipay_dict'):
                params['cur_lbs_poi'] = self.cur_lbs_poi.to_alipay_dict()
            else:
                params['cur_lbs_poi'] = self.cur_lbs_poi
        if self.dest:
            if hasattr(self.dest, 'to_alipay_dict'):
                params['dest'] = self.dest.to_alipay_dict()
            else:
                params['dest'] = self.dest
        if self.dest_lbs_poi:
            if hasattr(self.dest_lbs_poi, 'to_alipay_dict'):
                params['dest_lbs_poi'] = self.dest_lbs_poi.to_alipay_dict()
            else:
                params['dest_lbs_poi'] = self.dest_lbs_poi
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoRoutePolylineQueryModel()
        if 'cur_lbs_poi' in d:
            o.cur_lbs_poi = d['cur_lbs_poi']
        if 'dest' in d:
            o.dest = d['dest']
        if 'dest_lbs_poi' in d:
            o.dest_lbs_poi = d['dest_lbs_poi']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'source' in d:
            o.source = d['source']
        if 'type' in d:
            o.type = d['type']
        return o


