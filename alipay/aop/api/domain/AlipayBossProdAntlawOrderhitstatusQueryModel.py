#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntlawOrderhitstatusQueryModel(object):

    def __init__(self):
        self._request_app_name = None
        self._request_biz_num = None
        self._request_hash_value = None
        self._request_time_stamp = None

    @property
    def request_app_name(self):
        return self._request_app_name

    @request_app_name.setter
    def request_app_name(self, value):
        self._request_app_name = value
    @property
    def request_biz_num(self):
        return self._request_biz_num

    @request_biz_num.setter
    def request_biz_num(self, value):
        self._request_biz_num = value
    @property
    def request_hash_value(self):
        return self._request_hash_value

    @request_hash_value.setter
    def request_hash_value(self, value):
        self._request_hash_value = value
    @property
    def request_time_stamp(self):
        return self._request_time_stamp

    @request_time_stamp.setter
    def request_time_stamp(self, value):
        self._request_time_stamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.request_app_name:
            if hasattr(self.request_app_name, 'to_alipay_dict'):
                params['request_app_name'] = self.request_app_name.to_alipay_dict()
            else:
                params['request_app_name'] = self.request_app_name
        if self.request_biz_num:
            if hasattr(self.request_biz_num, 'to_alipay_dict'):
                params['request_biz_num'] = self.request_biz_num.to_alipay_dict()
            else:
                params['request_biz_num'] = self.request_biz_num
        if self.request_hash_value:
            if hasattr(self.request_hash_value, 'to_alipay_dict'):
                params['request_hash_value'] = self.request_hash_value.to_alipay_dict()
            else:
                params['request_hash_value'] = self.request_hash_value
        if self.request_time_stamp:
            if hasattr(self.request_time_stamp, 'to_alipay_dict'):
                params['request_time_stamp'] = self.request_time_stamp.to_alipay_dict()
            else:
                params['request_time_stamp'] = self.request_time_stamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlawOrderhitstatusQueryModel()
        if 'request_app_name' in d:
            o.request_app_name = d['request_app_name']
        if 'request_biz_num' in d:
            o.request_biz_num = d['request_biz_num']
        if 'request_hash_value' in d:
            o.request_hash_value = d['request_hash_value']
        if 'request_time_stamp' in d:
            o.request_time_stamp = d['request_time_stamp']
        return o


