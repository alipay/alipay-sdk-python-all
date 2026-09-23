#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceItemInfo(object):

    def __init__(self):
        self._package_service_item_id = None
        self._package_service_item_name = None

    @property
    def package_service_item_id(self):
        return self._package_service_item_id

    @package_service_item_id.setter
    def package_service_item_id(self, value):
        self._package_service_item_id = value
    @property
    def package_service_item_name(self):
        return self._package_service_item_name

    @package_service_item_name.setter
    def package_service_item_name(self, value):
        self._package_service_item_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.package_service_item_id:
            if hasattr(self.package_service_item_id, 'to_alipay_dict'):
                params['package_service_item_id'] = self.package_service_item_id.to_alipay_dict()
            else:
                params['package_service_item_id'] = self.package_service_item_id
        if self.package_service_item_name:
            if hasattr(self.package_service_item_name, 'to_alipay_dict'):
                params['package_service_item_name'] = self.package_service_item_name.to_alipay_dict()
            else:
                params['package_service_item_name'] = self.package_service_item_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceItemInfo()
        if 'package_service_item_id' in d:
            o.package_service_item_id = d['package_service_item_id']
        if 'package_service_item_name' in d:
            o.package_service_item_name = d['package_service_item_name']
        return o


