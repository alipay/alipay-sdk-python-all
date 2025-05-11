#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailActivitypointsQueryModel(object):

    def __init__(self):
        self._activity_id_list = None
        self._page_num = None
        self._page_size = None

    @property
    def activity_id_list(self):
        return self._activity_id_list

    @activity_id_list.setter
    def activity_id_list(self, value):
        if isinstance(value, list):
            self._activity_id_list = list()
            for i in value:
                self._activity_id_list.append(i)
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
        if self.activity_id_list:
            if isinstance(self.activity_id_list, list):
                for i in range(0, len(self.activity_id_list)):
                    element = self.activity_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_id_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_id_list, 'to_alipay_dict'):
                params['activity_id_list'] = self.activity_id_list.to_alipay_dict()
            else:
                params['activity_id_list'] = self.activity_id_list
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
        o = AlipayCommerceRetailActivitypointsQueryModel()
        if 'activity_id_list' in d:
            o.activity_id_list = d['activity_id_list']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


