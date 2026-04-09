#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpAssistantMembershippackageOrderModel(object):

    def __init__(self):
        self._duration_quantity = None
        self._duration_unit = None
        self._exclude_license_list = None
        self._license_num = None
        self._order_no = None
        self._out_biz_no = None
        self._package_id = None

    @property
    def duration_quantity(self):
        return self._duration_quantity

    @duration_quantity.setter
    def duration_quantity(self, value):
        self._duration_quantity = value
    @property
    def duration_unit(self):
        return self._duration_unit

    @duration_unit.setter
    def duration_unit(self, value):
        self._duration_unit = value
    @property
    def exclude_license_list(self):
        return self._exclude_license_list

    @exclude_license_list.setter
    def exclude_license_list(self, value):
        if isinstance(value, list):
            self._exclude_license_list = list()
            for i in value:
                self._exclude_license_list.append(i)
    @property
    def license_num(self):
        return self._license_num

    @license_num.setter
    def license_num(self, value):
        self._license_num = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def package_id(self):
        return self._package_id

    @package_id.setter
    def package_id(self, value):
        self._package_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.duration_quantity:
            if hasattr(self.duration_quantity, 'to_alipay_dict'):
                params['duration_quantity'] = self.duration_quantity.to_alipay_dict()
            else:
                params['duration_quantity'] = self.duration_quantity
        if self.duration_unit:
            if hasattr(self.duration_unit, 'to_alipay_dict'):
                params['duration_unit'] = self.duration_unit.to_alipay_dict()
            else:
                params['duration_unit'] = self.duration_unit
        if self.exclude_license_list:
            if isinstance(self.exclude_license_list, list):
                for i in range(0, len(self.exclude_license_list)):
                    element = self.exclude_license_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exclude_license_list[i] = element.to_alipay_dict()
            if hasattr(self.exclude_license_list, 'to_alipay_dict'):
                params['exclude_license_list'] = self.exclude_license_list.to_alipay_dict()
            else:
                params['exclude_license_list'] = self.exclude_license_list
        if self.license_num:
            if hasattr(self.license_num, 'to_alipay_dict'):
                params['license_num'] = self.license_num.to_alipay_dict()
            else:
                params['license_num'] = self.license_num
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.package_id:
            if hasattr(self.package_id, 'to_alipay_dict'):
                params['package_id'] = self.package_id.to_alipay_dict()
            else:
                params['package_id'] = self.package_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAssistantMembershippackageOrderModel()
        if 'duration_quantity' in d:
            o.duration_quantity = d['duration_quantity']
        if 'duration_unit' in d:
            o.duration_unit = d['duration_unit']
        if 'exclude_license_list' in d:
            o.exclude_license_list = d['exclude_license_list']
        if 'license_num' in d:
            o.license_num = d['license_num']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'package_id' in d:
            o.package_id = d['package_id']
        return o


