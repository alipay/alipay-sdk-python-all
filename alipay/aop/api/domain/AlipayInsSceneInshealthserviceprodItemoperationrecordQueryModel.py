#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInshealthserviceprodItemoperationrecordQueryModel(object):

    def __init__(self):
        self._ant_ser_prod_no = None
        self._init_time_end = None
        self._init_time_start = None
        self._merchant_item_code = None
        self._page_no = None
        self._page_size = None
        self._refresh_type_list = None
        self._status_list = None

    @property
    def ant_ser_prod_no(self):
        return self._ant_ser_prod_no

    @ant_ser_prod_no.setter
    def ant_ser_prod_no(self, value):
        self._ant_ser_prod_no = value
    @property
    def init_time_end(self):
        return self._init_time_end

    @init_time_end.setter
    def init_time_end(self, value):
        self._init_time_end = value
    @property
    def init_time_start(self):
        return self._init_time_start

    @init_time_start.setter
    def init_time_start(self, value):
        self._init_time_start = value
    @property
    def merchant_item_code(self):
        return self._merchant_item_code

    @merchant_item_code.setter
    def merchant_item_code(self, value):
        self._merchant_item_code = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def refresh_type_list(self):
        return self._refresh_type_list

    @refresh_type_list.setter
    def refresh_type_list(self, value):
        if isinstance(value, list):
            self._refresh_type_list = list()
            for i in value:
                self._refresh_type_list.append(i)
    @property
    def status_list(self):
        return self._status_list

    @status_list.setter
    def status_list(self, value):
        if isinstance(value, list):
            self._status_list = list()
            for i in value:
                self._status_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.ant_ser_prod_no:
            if hasattr(self.ant_ser_prod_no, 'to_alipay_dict'):
                params['ant_ser_prod_no'] = self.ant_ser_prod_no.to_alipay_dict()
            else:
                params['ant_ser_prod_no'] = self.ant_ser_prod_no
        if self.init_time_end:
            if hasattr(self.init_time_end, 'to_alipay_dict'):
                params['init_time_end'] = self.init_time_end.to_alipay_dict()
            else:
                params['init_time_end'] = self.init_time_end
        if self.init_time_start:
            if hasattr(self.init_time_start, 'to_alipay_dict'):
                params['init_time_start'] = self.init_time_start.to_alipay_dict()
            else:
                params['init_time_start'] = self.init_time_start
        if self.merchant_item_code:
            if hasattr(self.merchant_item_code, 'to_alipay_dict'):
                params['merchant_item_code'] = self.merchant_item_code.to_alipay_dict()
            else:
                params['merchant_item_code'] = self.merchant_item_code
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.refresh_type_list:
            if isinstance(self.refresh_type_list, list):
                for i in range(0, len(self.refresh_type_list)):
                    element = self.refresh_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refresh_type_list[i] = element.to_alipay_dict()
            if hasattr(self.refresh_type_list, 'to_alipay_dict'):
                params['refresh_type_list'] = self.refresh_type_list.to_alipay_dict()
            else:
                params['refresh_type_list'] = self.refresh_type_list
        if self.status_list:
            if isinstance(self.status_list, list):
                for i in range(0, len(self.status_list)):
                    element = self.status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status_list[i] = element.to_alipay_dict()
            if hasattr(self.status_list, 'to_alipay_dict'):
                params['status_list'] = self.status_list.to_alipay_dict()
            else:
                params['status_list'] = self.status_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInshealthserviceprodItemoperationrecordQueryModel()
        if 'ant_ser_prod_no' in d:
            o.ant_ser_prod_no = d['ant_ser_prod_no']
        if 'init_time_end' in d:
            o.init_time_end = d['init_time_end']
        if 'init_time_start' in d:
            o.init_time_start = d['init_time_start']
        if 'merchant_item_code' in d:
            o.merchant_item_code = d['merchant_item_code']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'refresh_type_list' in d:
            o.refresh_type_list = d['refresh_type_list']
        if 'status_list' in d:
            o.status_list = d['status_list']
        return o


