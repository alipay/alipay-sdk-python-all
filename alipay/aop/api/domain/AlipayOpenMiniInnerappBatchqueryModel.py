#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerappBatchqueryModel(object):

    def __init__(self):
        self._app_type_list = None
        self._dev_id = None
        self._page_num = None
        self._page_size = None

    @property
    def app_type_list(self):
        return self._app_type_list

    @app_type_list.setter
    def app_type_list(self, value):
        if isinstance(value, list):
            self._app_type_list = list()
            for i in value:
                self._app_type_list.append(i)
    @property
    def dev_id(self):
        return self._dev_id

    @dev_id.setter
    def dev_id(self, value):
        self._dev_id = value
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
        if self.app_type_list:
            if isinstance(self.app_type_list, list):
                for i in range(0, len(self.app_type_list)):
                    element = self.app_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_type_list[i] = element.to_alipay_dict()
            if hasattr(self.app_type_list, 'to_alipay_dict'):
                params['app_type_list'] = self.app_type_list.to_alipay_dict()
            else:
                params['app_type_list'] = self.app_type_list
        if self.dev_id:
            if hasattr(self.dev_id, 'to_alipay_dict'):
                params['dev_id'] = self.dev_id.to_alipay_dict()
            else:
                params['dev_id'] = self.dev_id
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
        o = AlipayOpenMiniInnerappBatchqueryModel()
        if 'app_type_list' in d:
            o.app_type_list = d['app_type_list']
        if 'dev_id' in d:
            o.dev_id = d['dev_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


