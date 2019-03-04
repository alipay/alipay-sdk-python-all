#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenServicemarketOrderSyncModel(object):

    def __init__(self):
        self._consumer_uid = None
        self._fin_tech_order_no = None
        self._fin_tech_product_code = None
        self._gmt_modified = None
        self._order_status = None
        self._order_time = None
        self._order_type = None
        self._out_biz_no = None

    @property
    def consumer_uid(self):
        return self._consumer_uid

    @consumer_uid.setter
    def consumer_uid(self, value):
        self._consumer_uid = value
    @property
    def fin_tech_order_no(self):
        return self._fin_tech_order_no

    @fin_tech_order_no.setter
    def fin_tech_order_no(self, value):
        self._fin_tech_order_no = value
    @property
    def fin_tech_product_code(self):
        return self._fin_tech_product_code

    @fin_tech_product_code.setter
    def fin_tech_product_code(self, value):
        self._fin_tech_product_code = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.consumer_uid:
            if hasattr(self.consumer_uid, 'to_alipay_dict'):
                params['consumer_uid'] = self.consumer_uid.to_alipay_dict()
            else:
                params['consumer_uid'] = self.consumer_uid
        if self.fin_tech_order_no:
            if hasattr(self.fin_tech_order_no, 'to_alipay_dict'):
                params['fin_tech_order_no'] = self.fin_tech_order_no.to_alipay_dict()
            else:
                params['fin_tech_order_no'] = self.fin_tech_order_no
        if self.fin_tech_product_code:
            if hasattr(self.fin_tech_product_code, 'to_alipay_dict'):
                params['fin_tech_product_code'] = self.fin_tech_product_code.to_alipay_dict()
            else:
                params['fin_tech_product_code'] = self.fin_tech_product_code
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenServicemarketOrderSyncModel()
        if 'consumer_uid' in d:
            o.consumer_uid = d['consumer_uid']
        if 'fin_tech_order_no' in d:
            o.fin_tech_order_no = d['fin_tech_order_no']
        if 'fin_tech_product_code' in d:
            o.fin_tech_product_code = d['fin_tech_product_code']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


