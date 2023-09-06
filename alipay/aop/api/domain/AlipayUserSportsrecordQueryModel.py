#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserSportsrecordQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._out_biz_code = None
        self._page_index = None
        self._page_size = None
        self._record_date = None
        self._sport_types = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_code(self):
        return self._out_biz_code

    @out_biz_code.setter
    def out_biz_code(self, value):
        self._out_biz_code = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def record_date(self):
        return self._record_date

    @record_date.setter
    def record_date(self, value):
        self._record_date = value
    @property
    def sport_types(self):
        return self._sport_types

    @sport_types.setter
    def sport_types(self, value):
        if isinstance(value, list):
            self._sport_types = list()
            for i in value:
                self._sport_types.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_code:
            if hasattr(self.out_biz_code, 'to_alipay_dict'):
                params['out_biz_code'] = self.out_biz_code.to_alipay_dict()
            else:
                params['out_biz_code'] = self.out_biz_code
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.record_date:
            if hasattr(self.record_date, 'to_alipay_dict'):
                params['record_date'] = self.record_date.to_alipay_dict()
            else:
                params['record_date'] = self.record_date
        if self.sport_types:
            if isinstance(self.sport_types, list):
                for i in range(0, len(self.sport_types)):
                    element = self.sport_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sport_types[i] = element.to_alipay_dict()
            if hasattr(self.sport_types, 'to_alipay_dict'):
                params['sport_types'] = self.sport_types.to_alipay_dict()
            else:
                params['sport_types'] = self.sport_types
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
        o = AlipayUserSportsrecordQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_code' in d:
            o.out_biz_code = d['out_biz_code']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'record_date' in d:
            o.record_date = d['record_date']
        if 'sport_types' in d:
            o.sport_types = d['sport_types']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


