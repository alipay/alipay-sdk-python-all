#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmCarOwnerOrderInfo(object):

    def __init__(self):
        self._biz_order_no = None
        self._order_status = None
        self._service_order_cnt = None

    @property
    def biz_order_no(self):
        return self._biz_order_no

    @biz_order_no.setter
    def biz_order_no(self, value):
        self._biz_order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def service_order_cnt(self):
        return self._service_order_cnt

    @service_order_cnt.setter
    def service_order_cnt(self, value):
        self._service_order_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_no:
            if hasattr(self.biz_order_no, 'to_alipay_dict'):
                params['biz_order_no'] = self.biz_order_no.to_alipay_dict()
            else:
                params['biz_order_no'] = self.biz_order_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.service_order_cnt:
            if hasattr(self.service_order_cnt, 'to_alipay_dict'):
                params['service_order_cnt'] = self.service_order_cnt.to_alipay_dict()
            else:
                params['service_order_cnt'] = self.service_order_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmCarOwnerOrderInfo()
        if 'biz_order_no' in d:
            o.biz_order_no = d['biz_order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'service_order_cnt' in d:
            o.service_order_cnt = d['service_order_cnt']
        return o


