#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SalesSolutionExt import SalesSolutionExt


class DeviceExtAttribute(object):

    def __init__(self):
        self._external_id = None
        self._external_shop_id = None
        self._sales_entry_order_id = None
        self._sales_solution_ext = None
        self._shop_name = None
        self._shop_nick_name = None
        self._solution_id = None
        self._source = None
        self._spi_app_id = None
        self._terminal_bind_info = None

    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def external_shop_id(self):
        return self._external_shop_id

    @external_shop_id.setter
    def external_shop_id(self, value):
        self._external_shop_id = value
    @property
    def sales_entry_order_id(self):
        return self._sales_entry_order_id

    @sales_entry_order_id.setter
    def sales_entry_order_id(self, value):
        self._sales_entry_order_id = value
    @property
    def sales_solution_ext(self):
        return self._sales_solution_ext

    @sales_solution_ext.setter
    def sales_solution_ext(self, value):
        if isinstance(value, SalesSolutionExt):
            self._sales_solution_ext = value
        else:
            self._sales_solution_ext = SalesSolutionExt.from_alipay_dict(value)
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_nick_name(self):
        return self._shop_nick_name

    @shop_nick_name.setter
    def shop_nick_name(self, value):
        self._shop_nick_name = value
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def spi_app_id(self):
        return self._spi_app_id

    @spi_app_id.setter
    def spi_app_id(self, value):
        self._spi_app_id = value
    @property
    def terminal_bind_info(self):
        return self._terminal_bind_info

    @terminal_bind_info.setter
    def terminal_bind_info(self, value):
        self._terminal_bind_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.external_shop_id:
            if hasattr(self.external_shop_id, 'to_alipay_dict'):
                params['external_shop_id'] = self.external_shop_id.to_alipay_dict()
            else:
                params['external_shop_id'] = self.external_shop_id
        if self.sales_entry_order_id:
            if hasattr(self.sales_entry_order_id, 'to_alipay_dict'):
                params['sales_entry_order_id'] = self.sales_entry_order_id.to_alipay_dict()
            else:
                params['sales_entry_order_id'] = self.sales_entry_order_id
        if self.sales_solution_ext:
            if hasattr(self.sales_solution_ext, 'to_alipay_dict'):
                params['sales_solution_ext'] = self.sales_solution_ext.to_alipay_dict()
            else:
                params['sales_solution_ext'] = self.sales_solution_ext
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_nick_name:
            if hasattr(self.shop_nick_name, 'to_alipay_dict'):
                params['shop_nick_name'] = self.shop_nick_name.to_alipay_dict()
            else:
                params['shop_nick_name'] = self.shop_nick_name
        if self.solution_id:
            if hasattr(self.solution_id, 'to_alipay_dict'):
                params['solution_id'] = self.solution_id.to_alipay_dict()
            else:
                params['solution_id'] = self.solution_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.spi_app_id:
            if hasattr(self.spi_app_id, 'to_alipay_dict'):
                params['spi_app_id'] = self.spi_app_id.to_alipay_dict()
            else:
                params['spi_app_id'] = self.spi_app_id
        if self.terminal_bind_info:
            if hasattr(self.terminal_bind_info, 'to_alipay_dict'):
                params['terminal_bind_info'] = self.terminal_bind_info.to_alipay_dict()
            else:
                params['terminal_bind_info'] = self.terminal_bind_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceExtAttribute()
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'external_shop_id' in d:
            o.external_shop_id = d['external_shop_id']
        if 'sales_entry_order_id' in d:
            o.sales_entry_order_id = d['sales_entry_order_id']
        if 'sales_solution_ext' in d:
            o.sales_solution_ext = d['sales_solution_ext']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_nick_name' in d:
            o.shop_nick_name = d['shop_nick_name']
        if 'solution_id' in d:
            o.solution_id = d['solution_id']
        if 'source' in d:
            o.source = d['source']
        if 'spi_app_id' in d:
            o.spi_app_id = d['spi_app_id']
        if 'terminal_bind_info' in d:
            o.terminal_bind_info = d['terminal_bind_info']
        return o


