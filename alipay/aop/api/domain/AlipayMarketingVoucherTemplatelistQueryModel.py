#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingVoucherTemplatelistQueryModel(object):

    def __init__(self):
        self._create_end_time = None
        self._create_start_time = None
        self._page_num = None
        self._page_size = None

    @property
    def create_end_time(self):
        return self._create_end_time

    @create_end_time.setter
    def create_end_time(self, value):
        self._create_end_time = value
    @property
    def create_start_time(self):
        return self._create_start_time

    @create_start_time.setter
    def create_start_time(self, value):
        self._create_start_time = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.create_end_time:
            if hasattr(self.create_end_time, 'to_alipay_dict'):
                params['create_end_time'] = self.create_end_time.to_alipay_dict()
            else:
                params['create_end_time'] = self.create_end_time
        if self.create_start_time:
            if hasattr(self.create_start_time, 'to_alipay_dict'):
                params['create_start_time'] = self.create_start_time.to_alipay_dict()
            else:
                params['create_start_time'] = self.create_start_time
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingVoucherTemplatelistQueryModel()
        if 'create_end_time' in d:
            o.create_end_time = d['create_end_time']
        if 'create_start_time' in d:
            o.create_start_time = d['create_start_time']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


