#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoPartnerAllpoiQueryModel(object):

    def __init__(self):
        self._cur_lbs_poi = None
        self._item_id = None
        self._source = None
        self._user_id = None

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
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


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
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayCloudCloudpromoPartnerAllpoiQueryModel()
        if 'cur_lbs_poi' in d:
            o.cur_lbs_poi = d['cur_lbs_poi']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


