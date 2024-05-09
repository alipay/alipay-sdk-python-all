#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScoreRangeInfoDTO import ScoreRangeInfoDTO
from alipay.aop.api.domain.ShopAreaInfoDTO import ShopAreaInfoDTO


class AlipayDataAntsycmShopdataBatchqueryModel(object):

    def __init__(self):
        self._business_code = None
        self._page_num = None
        self._page_size = None
        self._partner_id = None
        self._score_range = None
        self._score_type = None
        self._shop_area = None
        self._sort_name = None
        self._task_id = None
        self._top_num = None

    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def score_range(self):
        return self._score_range

    @score_range.setter
    def score_range(self, value):
        if isinstance(value, ScoreRangeInfoDTO):
            self._score_range = value
        else:
            self._score_range = ScoreRangeInfoDTO.from_alipay_dict(value)
    @property
    def score_type(self):
        return self._score_type

    @score_type.setter
    def score_type(self, value):
        if isinstance(value, list):
            self._score_type = list()
            for i in value:
                self._score_type.append(i)
    @property
    def shop_area(self):
        return self._shop_area

    @shop_area.setter
    def shop_area(self, value):
        if isinstance(value, list):
            self._shop_area = list()
            for i in value:
                if isinstance(i, ShopAreaInfoDTO):
                    self._shop_area.append(i)
                else:
                    self._shop_area.append(ShopAreaInfoDTO.from_alipay_dict(i))
    @property
    def sort_name(self):
        return self._sort_name

    @sort_name.setter
    def sort_name(self, value):
        self._sort_name = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def top_num(self):
        return self._top_num

    @top_num.setter
    def top_num(self, value):
        self._top_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.score_range:
            if hasattr(self.score_range, 'to_alipay_dict'):
                params['score_range'] = self.score_range.to_alipay_dict()
            else:
                params['score_range'] = self.score_range
        if self.score_type:
            if isinstance(self.score_type, list):
                for i in range(0, len(self.score_type)):
                    element = self.score_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.score_type[i] = element.to_alipay_dict()
            if hasattr(self.score_type, 'to_alipay_dict'):
                params['score_type'] = self.score_type.to_alipay_dict()
            else:
                params['score_type'] = self.score_type
        if self.shop_area:
            if isinstance(self.shop_area, list):
                for i in range(0, len(self.shop_area)):
                    element = self.shop_area[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_area[i] = element.to_alipay_dict()
            if hasattr(self.shop_area, 'to_alipay_dict'):
                params['shop_area'] = self.shop_area.to_alipay_dict()
            else:
                params['shop_area'] = self.shop_area
        if self.sort_name:
            if hasattr(self.sort_name, 'to_alipay_dict'):
                params['sort_name'] = self.sort_name.to_alipay_dict()
            else:
                params['sort_name'] = self.sort_name
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.top_num:
            if hasattr(self.top_num, 'to_alipay_dict'):
                params['top_num'] = self.top_num.to_alipay_dict()
            else:
                params['top_num'] = self.top_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAntsycmShopdataBatchqueryModel()
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'score_range' in d:
            o.score_range = d['score_range']
        if 'score_type' in d:
            o.score_type = d['score_type']
        if 'shop_area' in d:
            o.shop_area = d['shop_area']
        if 'sort_name' in d:
            o.sort_name = d['sort_name']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'top_num' in d:
            o.top_num = d['top_num']
        return o


