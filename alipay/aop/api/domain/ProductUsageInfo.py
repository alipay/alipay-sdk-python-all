#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FeeItemInfo import FeeItemInfo


class ProductUsageInfo(object):

    def __init__(self):
        self._display_name = None
        self._fee_item_infos = None
        self._icon = None
        self._name = None

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def fee_item_infos(self):
        return self._fee_item_infos

    @fee_item_infos.setter
    def fee_item_infos(self, value):
        if isinstance(value, list):
            self._fee_item_infos = list()
            for i in value:
                if isinstance(i, FeeItemInfo):
                    self._fee_item_infos.append(i)
                else:
                    self._fee_item_infos.append(FeeItemInfo.from_alipay_dict(i))
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.fee_item_infos:
            if isinstance(self.fee_item_infos, list):
                for i in range(0, len(self.fee_item_infos)):
                    element = self.fee_item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fee_item_infos[i] = element.to_alipay_dict()
            if hasattr(self.fee_item_infos, 'to_alipay_dict'):
                params['fee_item_infos'] = self.fee_item_infos.to_alipay_dict()
            else:
                params['fee_item_infos'] = self.fee_item_infos
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductUsageInfo()
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'fee_item_infos' in d:
            o.fee_item_infos = d['fee_item_infos']
        if 'icon' in d:
            o.icon = d['icon']
        if 'name' in d:
            o.name = d['name']
        return o


