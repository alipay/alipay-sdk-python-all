#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftSkuCampaignCreateModel(object):

    def __init__(self):
        self._camp_biz_type = None
        self._camp_name = None
        self._end_time = None
        self._group_id = None
        self._sku_id = None
        self._start_time = None

    @property
    def camp_biz_type(self):
        return self._camp_biz_type

    @camp_biz_type.setter
    def camp_biz_type(self, value):
        self._camp_biz_type = value
    @property
    def camp_name(self):
        return self._camp_name

    @camp_name.setter
    def camp_name(self, value):
        self._camp_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_biz_type:
            if hasattr(self.camp_biz_type, 'to_alipay_dict'):
                params['camp_biz_type'] = self.camp_biz_type.to_alipay_dict()
            else:
                params['camp_biz_type'] = self.camp_biz_type
        if self.camp_name:
            if hasattr(self.camp_name, 'to_alipay_dict'):
                params['camp_name'] = self.camp_name.to_alipay_dict()
            else:
                params['camp_name'] = self.camp_name
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftSkuCampaignCreateModel()
        if 'camp_biz_type' in d:
            o.camp_biz_type = d['camp_biz_type']
        if 'camp_name' in d:
            o.camp_name = d['camp_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


