#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtUserInfo import ExtUserInfo
from alipay.aop.api.domain.OrderDetail import OrderDetail


class AlipayTradeMergePrecreateModel(object):

    def __init__(self):
        self._ext_user_info = None
        self._order_details = None
        self._out_merge_no = None
        self._time_expire = None
        self._timeout_express = None

    @property
    def ext_user_info(self):
        return self._ext_user_info

    @ext_user_info.setter
    def ext_user_info(self, value):
        if isinstance(value, ExtUserInfo):
            self._ext_user_info = value
        else:
            self._ext_user_info = ExtUserInfo.from_alipay_dict(value)
    @property
    def order_details(self):
        return self._order_details

    @order_details.setter
    def order_details(self, value):
        if isinstance(value, list):
            self._order_details = list()
            for i in value:
                if isinstance(i, OrderDetail):
                    self._order_details.append(i)
                else:
                    self._order_details.append(OrderDetail.from_alipay_dict(i))
    @property
    def out_merge_no(self):
        return self._out_merge_no

    @out_merge_no.setter
    def out_merge_no(self, value):
        self._out_merge_no = value
    @property
    def time_expire(self):
        return self._time_expire

    @time_expire.setter
    def time_expire(self, value):
        self._time_expire = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_user_info:
            if hasattr(self.ext_user_info, 'to_alipay_dict'):
                params['ext_user_info'] = self.ext_user_info.to_alipay_dict()
            else:
                params['ext_user_info'] = self.ext_user_info
        if self.order_details:
            if isinstance(self.order_details, list):
                for i in range(0, len(self.order_details)):
                    element = self.order_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_details[i] = element.to_alipay_dict()
            if hasattr(self.order_details, 'to_alipay_dict'):
                params['order_details'] = self.order_details.to_alipay_dict()
            else:
                params['order_details'] = self.order_details
        if self.out_merge_no:
            if hasattr(self.out_merge_no, 'to_alipay_dict'):
                params['out_merge_no'] = self.out_merge_no.to_alipay_dict()
            else:
                params['out_merge_no'] = self.out_merge_no
        if self.time_expire:
            if hasattr(self.time_expire, 'to_alipay_dict'):
                params['time_expire'] = self.time_expire.to_alipay_dict()
            else:
                params['time_expire'] = self.time_expire
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeMergePrecreateModel()
        if 'ext_user_info' in d:
            o.ext_user_info = d['ext_user_info']
        if 'order_details' in d:
            o.order_details = d['order_details']
        if 'out_merge_no' in d:
            o.out_merge_no = d['out_merge_no']
        if 'time_expire' in d:
            o.time_expire = d['time_expire']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        return o


