#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerbaseinfoListQueryModel(object):

    def __init__(self):
        self._app_sub_type = None
        self._developer_id = None
        self._inst_code = None
        self._page_num = None
        self._page_size = None

    @property
    def app_sub_type(self):
        return self._app_sub_type

    @app_sub_type.setter
    def app_sub_type(self, value):
        self._app_sub_type = value
    @property
    def developer_id(self):
        return self._developer_id

    @developer_id.setter
    def developer_id(self, value):
        self._developer_id = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
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
        if self.app_sub_type:
            if hasattr(self.app_sub_type, 'to_alipay_dict'):
                params['app_sub_type'] = self.app_sub_type.to_alipay_dict()
            else:
                params['app_sub_type'] = self.app_sub_type
        if self.developer_id:
            if hasattr(self.developer_id, 'to_alipay_dict'):
                params['developer_id'] = self.developer_id.to_alipay_dict()
            else:
                params['developer_id'] = self.developer_id
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
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
        o = AlipayOpenMiniInnerbaseinfoListQueryModel()
        if 'app_sub_type' in d:
            o.app_sub_type = d['app_sub_type']
        if 'developer_id' in d:
            o.developer_id = d['developer_id']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


