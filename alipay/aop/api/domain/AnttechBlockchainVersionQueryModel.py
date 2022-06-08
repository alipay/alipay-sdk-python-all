#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainVersionQueryModel(object):

    def __init__(self):
        self._business_id = None
        self._end_time = None
        self._is_troop = None
        self._page_num = None
        self._page_size = None
        self._product_id = None
        self._product_line_id = None
        self._project_name = None
        self._start_time = None
        self._version_num = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def is_troop(self):
        return self._is_troop

    @is_troop.setter
    def is_troop(self, value):
        self._is_troop = value
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
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_line_id(self):
        return self._product_line_id

    @product_line_id.setter
    def product_line_id(self, value):
        self._product_line_id = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def version_num(self):
        return self._version_num

    @version_num.setter
    def version_num(self, value):
        self._version_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.is_troop:
            if hasattr(self.is_troop, 'to_alipay_dict'):
                params['is_troop'] = self.is_troop.to_alipay_dict()
            else:
                params['is_troop'] = self.is_troop
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
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_line_id:
            if hasattr(self.product_line_id, 'to_alipay_dict'):
                params['product_line_id'] = self.product_line_id.to_alipay_dict()
            else:
                params['product_line_id'] = self.product_line_id
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.version_num:
            if hasattr(self.version_num, 'to_alipay_dict'):
                params['version_num'] = self.version_num.to_alipay_dict()
            else:
                params['version_num'] = self.version_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainVersionQueryModel()
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'is_troop' in d:
            o.is_troop = d['is_troop']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_line_id' in d:
            o.product_line_id = d['product_line_id']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'version_num' in d:
            o.version_num = d['version_num']
        return o


