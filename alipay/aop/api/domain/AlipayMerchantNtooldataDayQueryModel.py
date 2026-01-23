#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantNtooldataDayQueryModel(object):

    def __init__(self):
        self._device_id_list = None
        self._device_type = None
        self._metrics_date = None
        self._page_num = None
        self._page_size = None
        self._smid_list = None

    @property
    def device_id_list(self):
        return self._device_id_list

    @device_id_list.setter
    def device_id_list(self, value):
        if isinstance(value, list):
            self._device_id_list = list()
            for i in value:
                self._device_id_list.append(i)
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def metrics_date(self):
        return self._metrics_date

    @metrics_date.setter
    def metrics_date(self, value):
        self._metrics_date = value
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
    def smid_list(self):
        return self._smid_list

    @smid_list.setter
    def smid_list(self, value):
        if isinstance(value, list):
            self._smid_list = list()
            for i in value:
                self._smid_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.device_id_list:
            if isinstance(self.device_id_list, list):
                for i in range(0, len(self.device_id_list)):
                    element = self.device_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_id_list[i] = element.to_alipay_dict()
            if hasattr(self.device_id_list, 'to_alipay_dict'):
                params['device_id_list'] = self.device_id_list.to_alipay_dict()
            else:
                params['device_id_list'] = self.device_id_list
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.metrics_date:
            if hasattr(self.metrics_date, 'to_alipay_dict'):
                params['metrics_date'] = self.metrics_date.to_alipay_dict()
            else:
                params['metrics_date'] = self.metrics_date
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
        if self.smid_list:
            if isinstance(self.smid_list, list):
                for i in range(0, len(self.smid_list)):
                    element = self.smid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.smid_list[i] = element.to_alipay_dict()
            if hasattr(self.smid_list, 'to_alipay_dict'):
                params['smid_list'] = self.smid_list.to_alipay_dict()
            else:
                params['smid_list'] = self.smid_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantNtooldataDayQueryModel()
        if 'device_id_list' in d:
            o.device_id_list = d['device_id_list']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'metrics_date' in d:
            o.metrics_date = d['metrics_date']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'smid_list' in d:
            o.smid_list = d['smid_list']
        return o


