#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StuffInfo(object):

    def __init__(self):
        self._description = None
        self._ext_info = None
        self._item_name = None
        self._sku_no = None
        self._standard_description = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def sku_no(self):
        return self._sku_no

    @sku_no.setter
    def sku_no(self, value):
        self._sku_no = value
    @property
    def standard_description(self):
        return self._standard_description

    @standard_description.setter
    def standard_description(self, value):
        self._standard_description = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.sku_no:
            if hasattr(self.sku_no, 'to_alipay_dict'):
                params['sku_no'] = self.sku_no.to_alipay_dict()
            else:
                params['sku_no'] = self.sku_no
        if self.standard_description:
            if hasattr(self.standard_description, 'to_alipay_dict'):
                params['standard_description'] = self.standard_description.to_alipay_dict()
            else:
                params['standard_description'] = self.standard_description
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StuffInfo()
        if 'description' in d:
            o.description = d['description']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'sku_no' in d:
            o.sku_no = d['sku_no']
        if 'standard_description' in d:
            o.standard_description = d['standard_description']
        return o


