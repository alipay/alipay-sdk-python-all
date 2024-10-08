#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantGroupActivityBatchqueryModel(object):

    def __init__(self):
        self._biz_type_list = None
        self._page_num = None
        self._page_size = None
        self._status = None

    @property
    def biz_type_list(self):
        return self._biz_type_list

    @biz_type_list.setter
    def biz_type_list(self, value):
        if isinstance(value, list):
            self._biz_type_list = list()
            for i in value:
                self._biz_type_list.append(i)
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type_list:
            if isinstance(self.biz_type_list, list):
                for i in range(0, len(self.biz_type_list)):
                    element = self.biz_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_type_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_type_list, 'to_alipay_dict'):
                params['biz_type_list'] = self.biz_type_list.to_alipay_dict()
            else:
                params['biz_type_list'] = self.biz_type_list
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupActivityBatchqueryModel()
        if 'biz_type_list' in d:
            o.biz_type_list = d['biz_type_list']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'status' in d:
            o.status = d['status']
        return o


