#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IsvSpiDefinition(object):

    def __init__(self):
        self._biz_code = None
        self._description = None
        self._icon = None
        self._spi_endpoint = None
        self._spi_ext_property = None
        self._spi_key = None
        self._spi_name = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def spi_endpoint(self):
        return self._spi_endpoint

    @spi_endpoint.setter
    def spi_endpoint(self, value):
        self._spi_endpoint = value
    @property
    def spi_ext_property(self):
        return self._spi_ext_property

    @spi_ext_property.setter
    def spi_ext_property(self, value):
        self._spi_ext_property = value
    @property
    def spi_key(self):
        return self._spi_key

    @spi_key.setter
    def spi_key(self, value):
        self._spi_key = value
    @property
    def spi_name(self):
        return self._spi_name

    @spi_name.setter
    def spi_name(self, value):
        self._spi_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.spi_endpoint:
            if hasattr(self.spi_endpoint, 'to_alipay_dict'):
                params['spi_endpoint'] = self.spi_endpoint.to_alipay_dict()
            else:
                params['spi_endpoint'] = self.spi_endpoint
        if self.spi_ext_property:
            if hasattr(self.spi_ext_property, 'to_alipay_dict'):
                params['spi_ext_property'] = self.spi_ext_property.to_alipay_dict()
            else:
                params['spi_ext_property'] = self.spi_ext_property
        if self.spi_key:
            if hasattr(self.spi_key, 'to_alipay_dict'):
                params['spi_key'] = self.spi_key.to_alipay_dict()
            else:
                params['spi_key'] = self.spi_key
        if self.spi_name:
            if hasattr(self.spi_name, 'to_alipay_dict'):
                params['spi_name'] = self.spi_name.to_alipay_dict()
            else:
                params['spi_name'] = self.spi_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IsvSpiDefinition()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'description' in d:
            o.description = d['description']
        if 'icon' in d:
            o.icon = d['icon']
        if 'spi_endpoint' in d:
            o.spi_endpoint = d['spi_endpoint']
        if 'spi_ext_property' in d:
            o.spi_ext_property = d['spi_ext_property']
        if 'spi_key' in d:
            o.spi_key = d['spi_key']
        if 'spi_name' in d:
            o.spi_name = d['spi_name']
        return o


