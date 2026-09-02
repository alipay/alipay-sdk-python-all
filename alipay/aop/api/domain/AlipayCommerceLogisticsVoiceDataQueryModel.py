#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsVoiceDataQueryModel(object):

    def __init__(self):
        self._biz_date = None
        self._dim_key = None
        self._dim_type = None
        self._page_size = None
        self._pre_page_max_data_id = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def dim_key(self):
        return self._dim_key

    @dim_key.setter
    def dim_key(self, value):
        self._dim_key = value
    @property
    def dim_type(self):
        return self._dim_type

    @dim_type.setter
    def dim_type(self, value):
        self._dim_type = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def pre_page_max_data_id(self):
        return self._pre_page_max_data_id

    @pre_page_max_data_id.setter
    def pre_page_max_data_id(self, value):
        self._pre_page_max_data_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.dim_key:
            if hasattr(self.dim_key, 'to_alipay_dict'):
                params['dim_key'] = self.dim_key.to_alipay_dict()
            else:
                params['dim_key'] = self.dim_key
        if self.dim_type:
            if hasattr(self.dim_type, 'to_alipay_dict'):
                params['dim_type'] = self.dim_type.to_alipay_dict()
            else:
                params['dim_type'] = self.dim_type
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.pre_page_max_data_id:
            if hasattr(self.pre_page_max_data_id, 'to_alipay_dict'):
                params['pre_page_max_data_id'] = self.pre_page_max_data_id.to_alipay_dict()
            else:
                params['pre_page_max_data_id'] = self.pre_page_max_data_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsVoiceDataQueryModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'dim_key' in d:
            o.dim_key = d['dim_key']
        if 'dim_type' in d:
            o.dim_type = d['dim_type']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'pre_page_max_data_id' in d:
            o.pre_page_max_data_id = d['pre_page_max_data_id']
        return o


