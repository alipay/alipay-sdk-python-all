#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsVoicePlansnfailQueryModel(object):

    def __init__(self):
        self._biz_date = None
        self._logistics_voice_plan_id = None
        self._page_size = None
        self._pre_page_max_data_id = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def logistics_voice_plan_id(self):
        return self._logistics_voice_plan_id

    @logistics_voice_plan_id.setter
    def logistics_voice_plan_id(self, value):
        self._logistics_voice_plan_id = value
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
        if self.logistics_voice_plan_id:
            if hasattr(self.logistics_voice_plan_id, 'to_alipay_dict'):
                params['logistics_voice_plan_id'] = self.logistics_voice_plan_id.to_alipay_dict()
            else:
                params['logistics_voice_plan_id'] = self.logistics_voice_plan_id
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
        o = AlipayCommerceLogisticsVoicePlansnfailQueryModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'logistics_voice_plan_id' in d:
            o.logistics_voice_plan_id = d['logistics_voice_plan_id']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'pre_page_max_data_id' in d:
            o.pre_page_max_data_id = d['pre_page_max_data_id']
        return o


