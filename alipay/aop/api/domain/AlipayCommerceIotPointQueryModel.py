#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotPointQueryModel(object):

    def __init__(self):
        self._out_device_point_id = None
        self._page_num = None
        self._page_size = None

    @property
    def out_device_point_id(self):
        return self._out_device_point_id

    @out_device_point_id.setter
    def out_device_point_id(self, value):
        self._out_device_point_id = value
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
        if self.out_device_point_id:
            if hasattr(self.out_device_point_id, 'to_alipay_dict'):
                params['out_device_point_id'] = self.out_device_point_id.to_alipay_dict()
            else:
                params['out_device_point_id'] = self.out_device_point_id
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
        o = AlipayCommerceIotPointQueryModel()
        if 'out_device_point_id' in d:
            o.out_device_point_id = d['out_device_point_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


