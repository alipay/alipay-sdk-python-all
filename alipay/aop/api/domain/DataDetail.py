#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConversionDataDetail import ConversionDataDetail


class DataDetail(object):

    def __init__(self):
        self._biz_date = None
        self._click = None
        self._conversion_data_list = None
        self._cost = None
        self._impression = None
        self._outer_id = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def click(self):
        return self._click

    @click.setter
    def click(self, value):
        self._click = value
    @property
    def conversion_data_list(self):
        return self._conversion_data_list

    @conversion_data_list.setter
    def conversion_data_list(self, value):
        if isinstance(value, list):
            self._conversion_data_list = list()
            for i in value:
                if isinstance(i, ConversionDataDetail):
                    self._conversion_data_list.append(i)
                else:
                    self._conversion_data_list.append(ConversionDataDetail.from_alipay_dict(i))
    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value
    @property
    def impression(self):
        return self._impression

    @impression.setter
    def impression(self, value):
        self._impression = value
    @property
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, value):
        self._outer_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.click:
            if hasattr(self.click, 'to_alipay_dict'):
                params['click'] = self.click.to_alipay_dict()
            else:
                params['click'] = self.click
        if self.conversion_data_list:
            if isinstance(self.conversion_data_list, list):
                for i in range(0, len(self.conversion_data_list)):
                    element = self.conversion_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.conversion_data_list[i] = element.to_alipay_dict()
            if hasattr(self.conversion_data_list, 'to_alipay_dict'):
                params['conversion_data_list'] = self.conversion_data_list.to_alipay_dict()
            else:
                params['conversion_data_list'] = self.conversion_data_list
        if self.cost:
            if hasattr(self.cost, 'to_alipay_dict'):
                params['cost'] = self.cost.to_alipay_dict()
            else:
                params['cost'] = self.cost
        if self.impression:
            if hasattr(self.impression, 'to_alipay_dict'):
                params['impression'] = self.impression.to_alipay_dict()
            else:
                params['impression'] = self.impression
        if self.outer_id:
            if hasattr(self.outer_id, 'to_alipay_dict'):
                params['outer_id'] = self.outer_id.to_alipay_dict()
            else:
                params['outer_id'] = self.outer_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DataDetail()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'click' in d:
            o.click = d['click']
        if 'conversion_data_list' in d:
            o.conversion_data_list = d['conversion_data_list']
        if 'cost' in d:
            o.cost = d['cost']
        if 'impression' in d:
            o.impression = d['impression']
        if 'outer_id' in d:
            o.outer_id = d['outer_id']
        return o


