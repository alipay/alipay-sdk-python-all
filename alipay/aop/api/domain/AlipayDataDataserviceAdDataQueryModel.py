#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdDataQueryModel(object):

    def __init__(self):
        self._ad_level = None
        self._biz_token = None
        self._charge_type = None
        self._end_date = None
        self._outer_id_list = None
        self._query_type = None
        self._start_date = None

    @property
    def ad_level(self):
        return self._ad_level

    @ad_level.setter
    def ad_level(self, value):
        self._ad_level = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def outer_id_list(self):
        return self._outer_id_list

    @outer_id_list.setter
    def outer_id_list(self, value):
        if isinstance(value, list):
            self._outer_id_list = list()
            for i in value:
                self._outer_id_list.append(i)
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_level:
            if hasattr(self.ad_level, 'to_alipay_dict'):
                params['ad_level'] = self.ad_level.to_alipay_dict()
            else:
                params['ad_level'] = self.ad_level
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.charge_type:
            if hasattr(self.charge_type, 'to_alipay_dict'):
                params['charge_type'] = self.charge_type.to_alipay_dict()
            else:
                params['charge_type'] = self.charge_type
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.outer_id_list:
            if isinstance(self.outer_id_list, list):
                for i in range(0, len(self.outer_id_list)):
                    element = self.outer_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.outer_id_list[i] = element.to_alipay_dict()
            if hasattr(self.outer_id_list, 'to_alipay_dict'):
                params['outer_id_list'] = self.outer_id_list.to_alipay_dict()
            else:
                params['outer_id_list'] = self.outer_id_list
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdDataQueryModel()
        if 'ad_level' in d:
            o.ad_level = d['ad_level']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'outer_id_list' in d:
            o.outer_id_list = d['outer_id_list']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


