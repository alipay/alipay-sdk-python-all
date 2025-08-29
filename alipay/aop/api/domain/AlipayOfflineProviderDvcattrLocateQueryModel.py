#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderDvcattrLocateQueryModel(object):

    def __init__(self):
        self._bluetooth_mac = None
        self._page_index = None
        self._page_size = None

    @property
    def bluetooth_mac(self):
        return self._bluetooth_mac

    @bluetooth_mac.setter
    def bluetooth_mac(self, value):
        if isinstance(value, list):
            self._bluetooth_mac = list()
            for i in value:
                self._bluetooth_mac.append(i)
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.bluetooth_mac:
            if isinstance(self.bluetooth_mac, list):
                for i in range(0, len(self.bluetooth_mac)):
                    element = self.bluetooth_mac[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bluetooth_mac[i] = element.to_alipay_dict()
            if hasattr(self.bluetooth_mac, 'to_alipay_dict'):
                params['bluetooth_mac'] = self.bluetooth_mac.to_alipay_dict()
            else:
                params['bluetooth_mac'] = self.bluetooth_mac
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
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
        o = AlipayOfflineProviderDvcattrLocateQueryModel()
        if 'bluetooth_mac' in d:
            o.bluetooth_mac = d['bluetooth_mac']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


