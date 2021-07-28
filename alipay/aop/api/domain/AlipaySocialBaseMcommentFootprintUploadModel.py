#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseMcommentFootprintUploadModel(object):

    def __init__(self):
        self._biz_type = None
        self._ext_data = None
        self._footprint_model_code = None
        self._footprint_model_data = None
        self._footprint_time = None
        self._item_id = None
        self._source = None
        self._user_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def footprint_model_code(self):
        return self._footprint_model_code

    @footprint_model_code.setter
    def footprint_model_code(self, value):
        self._footprint_model_code = value
    @property
    def footprint_model_data(self):
        return self._footprint_model_data

    @footprint_model_data.setter
    def footprint_model_data(self, value):
        self._footprint_model_data = value
    @property
    def footprint_time(self):
        return self._footprint_time

    @footprint_time.setter
    def footprint_time(self, value):
        self._footprint_time = value
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
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
        if self.footprint_model_code:
            if hasattr(self.footprint_model_code, 'to_alipay_dict'):
                params['footprint_model_code'] = self.footprint_model_code.to_alipay_dict()
            else:
                params['footprint_model_code'] = self.footprint_model_code
        if self.footprint_model_data:
            if hasattr(self.footprint_model_data, 'to_alipay_dict'):
                params['footprint_model_data'] = self.footprint_model_data.to_alipay_dict()
            else:
                params['footprint_model_data'] = self.footprint_model_data
        if self.footprint_time:
            if hasattr(self.footprint_time, 'to_alipay_dict'):
                params['footprint_time'] = self.footprint_time.to_alipay_dict()
            else:
                params['footprint_time'] = self.footprint_time
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
        o = AlipaySocialBaseMcommentFootprintUploadModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'footprint_model_code' in d:
            o.footprint_model_code = d['footprint_model_code']
        if 'footprint_model_data' in d:
            o.footprint_model_data = d['footprint_model_data']
        if 'footprint_time' in d:
            o.footprint_time = d['footprint_time']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


