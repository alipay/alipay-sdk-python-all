#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringOrderPushSignModel(object):

    def __init__(self):
        self._batch_no = None
        self._ext_infos = None
        self._order_id = None
        self._out_biz_no = None
        self._receipt_code = None
        self._receipt_time = None
        self._reject_reason_code = None
        self._reject_reason_desc = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def receipt_code(self):
        return self._receipt_code

    @receipt_code.setter
    def receipt_code(self, value):
        self._receipt_code = value
    @property
    def receipt_time(self):
        return self._receipt_time

    @receipt_time.setter
    def receipt_time(self, value):
        self._receipt_time = value
    @property
    def reject_reason_code(self):
        return self._reject_reason_code

    @reject_reason_code.setter
    def reject_reason_code(self, value):
        self._reject_reason_code = value
    @property
    def reject_reason_desc(self):
        return self._reject_reason_desc

    @reject_reason_desc.setter
    def reject_reason_desc(self, value):
        self._reject_reason_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.receipt_code:
            if hasattr(self.receipt_code, 'to_alipay_dict'):
                params['receipt_code'] = self.receipt_code.to_alipay_dict()
            else:
                params['receipt_code'] = self.receipt_code
        if self.receipt_time:
            if hasattr(self.receipt_time, 'to_alipay_dict'):
                params['receipt_time'] = self.receipt_time.to_alipay_dict()
            else:
                params['receipt_time'] = self.receipt_time
        if self.reject_reason_code:
            if hasattr(self.reject_reason_code, 'to_alipay_dict'):
                params['reject_reason_code'] = self.reject_reason_code.to_alipay_dict()
            else:
                params['reject_reason_code'] = self.reject_reason_code
        if self.reject_reason_desc:
            if hasattr(self.reject_reason_desc, 'to_alipay_dict'):
                params['reject_reason_desc'] = self.reject_reason_desc.to_alipay_dict()
            else:
                params['reject_reason_desc'] = self.reject_reason_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringOrderPushSignModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'receipt_code' in d:
            o.receipt_code = d['receipt_code']
        if 'receipt_time' in d:
            o.receipt_time = d['receipt_time']
        if 'reject_reason_code' in d:
            o.reject_reason_code = d['reject_reason_code']
        if 'reject_reason_desc' in d:
            o.reject_reason_desc = d['reject_reason_desc']
        return o


