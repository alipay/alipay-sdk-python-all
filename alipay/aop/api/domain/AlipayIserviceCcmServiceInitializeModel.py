#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IsvSpiDefinition import IsvSpiDefinition


class AlipayIserviceCcmServiceInitializeModel(object):

    def __init__(self):
        self._description = None
        self._icon = None
        self._service_code = None
        self._service_name = None
        self._service_order_url = None
        self._spis = None

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
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_order_url(self):
        return self._service_order_url

    @service_order_url.setter
    def service_order_url(self, value):
        self._service_order_url = value
    @property
    def spis(self):
        return self._spis

    @spis.setter
    def spis(self, value):
        if isinstance(value, list):
            self._spis = list()
            for i in value:
                if isinstance(i, IsvSpiDefinition):
                    self._spis.append(i)
                else:
                    self._spis.append(IsvSpiDefinition.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
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
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_order_url:
            if hasattr(self.service_order_url, 'to_alipay_dict'):
                params['service_order_url'] = self.service_order_url.to_alipay_dict()
            else:
                params['service_order_url'] = self.service_order_url
        if self.spis:
            if isinstance(self.spis, list):
                for i in range(0, len(self.spis)):
                    element = self.spis[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.spis[i] = element.to_alipay_dict()
            if hasattr(self.spis, 'to_alipay_dict'):
                params['spis'] = self.spis.to_alipay_dict()
            else:
                params['spis'] = self.spis
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmServiceInitializeModel()
        if 'description' in d:
            o.description = d['description']
        if 'icon' in d:
            o.icon = d['icon']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_order_url' in d:
            o.service_order_url = d['service_order_url']
        if 'spis' in d:
            o.spis = d['spis']
        return o


