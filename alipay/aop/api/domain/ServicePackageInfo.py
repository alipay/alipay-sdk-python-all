#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServicePackageInfo(object):

    def __init__(self):
        self._service_package_end_time = None
        self._service_package_id = None
        self._service_package_item_id = None
        self._service_package_item_name = None
        self._service_package_name = None
        self._service_package_order_id = None
        self._sub_package_item_id = None

    @property
    def service_package_end_time(self):
        return self._service_package_end_time

    @service_package_end_time.setter
    def service_package_end_time(self, value):
        self._service_package_end_time = value
    @property
    def service_package_id(self):
        return self._service_package_id

    @service_package_id.setter
    def service_package_id(self, value):
        self._service_package_id = value
    @property
    def service_package_item_id(self):
        return self._service_package_item_id

    @service_package_item_id.setter
    def service_package_item_id(self, value):
        self._service_package_item_id = value
    @property
    def service_package_item_name(self):
        return self._service_package_item_name

    @service_package_item_name.setter
    def service_package_item_name(self, value):
        self._service_package_item_name = value
    @property
    def service_package_name(self):
        return self._service_package_name

    @service_package_name.setter
    def service_package_name(self, value):
        self._service_package_name = value
    @property
    def service_package_order_id(self):
        return self._service_package_order_id

    @service_package_order_id.setter
    def service_package_order_id(self, value):
        self._service_package_order_id = value
    @property
    def sub_package_item_id(self):
        return self._sub_package_item_id

    @sub_package_item_id.setter
    def sub_package_item_id(self, value):
        self._sub_package_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_package_end_time:
            if hasattr(self.service_package_end_time, 'to_alipay_dict'):
                params['service_package_end_time'] = self.service_package_end_time.to_alipay_dict()
            else:
                params['service_package_end_time'] = self.service_package_end_time
        if self.service_package_id:
            if hasattr(self.service_package_id, 'to_alipay_dict'):
                params['service_package_id'] = self.service_package_id.to_alipay_dict()
            else:
                params['service_package_id'] = self.service_package_id
        if self.service_package_item_id:
            if hasattr(self.service_package_item_id, 'to_alipay_dict'):
                params['service_package_item_id'] = self.service_package_item_id.to_alipay_dict()
            else:
                params['service_package_item_id'] = self.service_package_item_id
        if self.service_package_item_name:
            if hasattr(self.service_package_item_name, 'to_alipay_dict'):
                params['service_package_item_name'] = self.service_package_item_name.to_alipay_dict()
            else:
                params['service_package_item_name'] = self.service_package_item_name
        if self.service_package_name:
            if hasattr(self.service_package_name, 'to_alipay_dict'):
                params['service_package_name'] = self.service_package_name.to_alipay_dict()
            else:
                params['service_package_name'] = self.service_package_name
        if self.service_package_order_id:
            if hasattr(self.service_package_order_id, 'to_alipay_dict'):
                params['service_package_order_id'] = self.service_package_order_id.to_alipay_dict()
            else:
                params['service_package_order_id'] = self.service_package_order_id
        if self.sub_package_item_id:
            if hasattr(self.sub_package_item_id, 'to_alipay_dict'):
                params['sub_package_item_id'] = self.sub_package_item_id.to_alipay_dict()
            else:
                params['sub_package_item_id'] = self.sub_package_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServicePackageInfo()
        if 'service_package_end_time' in d:
            o.service_package_end_time = d['service_package_end_time']
        if 'service_package_id' in d:
            o.service_package_id = d['service_package_id']
        if 'service_package_item_id' in d:
            o.service_package_item_id = d['service_package_item_id']
        if 'service_package_item_name' in d:
            o.service_package_item_name = d['service_package_item_name']
        if 'service_package_name' in d:
            o.service_package_name = d['service_package_name']
        if 'service_package_order_id' in d:
            o.service_package_order_id = d['service_package_order_id']
        if 'sub_package_item_id' in d:
            o.sub_package_item_id = d['sub_package_item_id']
        return o


