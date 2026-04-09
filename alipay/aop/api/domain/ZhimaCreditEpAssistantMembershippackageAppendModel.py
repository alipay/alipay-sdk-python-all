#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpAssistantMembershippackageAppendModel(object):

    def __init__(self):
        self._license_num = None
        self._order_no = None
        self._out_biz_no = None
        self._package_id = None

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
        o = ZhimaCreditEpAssistantMembershippackageAppendModel()
        if 'license_num' in d:
            o.license_num = d['license_num']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'package_id' in d:
            o.package_id = d['package_id']
        return o


