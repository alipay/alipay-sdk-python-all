#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCharityCommonwealCreateModel(object):

    def __init__(self):
        self._biz_time = None
        self._ext_info = None
        self._numerical = None
        self._original_data = None
        self._partner_id = None
        self._unique_id = None
        self._user_id = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def numerical(self):
        return self._numerical

    @numerical.setter
    def numerical(self, value):
        self._numerical = value
    @property
    def original_data(self):
        return self._original_data

    @original_data.setter
    def original_data(self, value):
        self._original_data = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.numerical:
            if hasattr(self.numerical, 'to_alipay_dict'):
                params['numerical'] = self.numerical.to_alipay_dict()
            else:
                params['numerical'] = self.numerical
        if self.original_data:
            if hasattr(self.original_data, 'to_alipay_dict'):
                params['original_data'] = self.original_data.to_alipay_dict()
            else:
                params['original_data'] = self.original_data
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
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
        o = AlipayUserCharityCommonwealCreateModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'numerical' in d:
            o.numerical = d['numerical']
        if 'original_data' in d:
            o.original_data = d['original_data']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


