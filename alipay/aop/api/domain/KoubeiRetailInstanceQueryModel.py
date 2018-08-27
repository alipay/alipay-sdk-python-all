#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailInstanceQueryModel(object):

    def __init__(self):
        self._instance_type = None
        self._page_num = None
        self._page_size = None

    @property
    def instance_type(self):
        return self._instance_type

    @instance_type.setter
    def instance_type(self, value):
        self._instance_type = value
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
        if self.instance_type:
            if hasattr(self.instance_type, 'to_alipay_dict'):
                params['instance_type'] = self.instance_type.to_alipay_dict()
            else:
                params['instance_type'] = self.instance_type
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
        o = KoubeiRetailInstanceQueryModel()
        if 'instance_type' in d:
            o.instance_type = d['instance_type']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


