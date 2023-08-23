#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseResourceusageMonthlyQueryModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._end_month = None
        self._fee_item_code = None
        self._start_month = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def end_month(self):
        return self._end_month

    @end_month.setter
    def end_month(self, value):
        self._end_month = value
    @property
    def fee_item_code(self):
        return self._fee_item_code

    @fee_item_code.setter
    def fee_item_code(self, value):
        self._fee_item_code = value
    @property
    def start_month(self):
        return self._start_month

    @start_month.setter
    def start_month(self, value):
        self._start_month = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.end_month:
            if hasattr(self.end_month, 'to_alipay_dict'):
                params['end_month'] = self.end_month.to_alipay_dict()
            else:
                params['end_month'] = self.end_month
        if self.fee_item_code:
            if hasattr(self.fee_item_code, 'to_alipay_dict'):
                params['fee_item_code'] = self.fee_item_code.to_alipay_dict()
            else:
                params['fee_item_code'] = self.fee_item_code
        if self.start_month:
            if hasattr(self.start_month, 'to_alipay_dict'):
                params['start_month'] = self.start_month.to_alipay_dict()
            else:
                params['start_month'] = self.start_month
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseResourceusageMonthlyQueryModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'end_month' in d:
            o.end_month = d['end_month']
        if 'fee_item_code' in d:
            o.fee_item_code = d['fee_item_code']
        if 'start_month' in d:
            o.start_month = d['start_month']
        return o


