#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceDeployorderDetailQueryModel(object):

    def __init__(self):
        self._biz_create_begin = None
        self._biz_ins_name = None
        self._page = None
        self._size = None

    @property
    def biz_create_begin(self):
        return self._biz_create_begin

    @biz_create_begin.setter
    def biz_create_begin(self, value):
        self._biz_create_begin = value
    @property
    def biz_ins_name(self):
        return self._biz_ins_name

    @biz_ins_name.setter
    def biz_ins_name(self, value):
        self._biz_ins_name = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_create_begin:
            if hasattr(self.biz_create_begin, 'to_alipay_dict'):
                params['biz_create_begin'] = self.biz_create_begin.to_alipay_dict()
            else:
                params['biz_create_begin'] = self.biz_create_begin
        if self.biz_ins_name:
            if hasattr(self.biz_ins_name, 'to_alipay_dict'):
                params['biz_ins_name'] = self.biz_ins_name.to_alipay_dict()
            else:
                params['biz_ins_name'] = self.biz_ins_name
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceDeployorderDetailQueryModel()
        if 'biz_create_begin' in d:
            o.biz_create_begin = d['biz_create_begin']
        if 'biz_ins_name' in d:
            o.biz_ins_name = d['biz_ins_name']
        if 'page' in d:
            o.page = d['page']
        if 'size' in d:
            o.size = d['size']
        return o


