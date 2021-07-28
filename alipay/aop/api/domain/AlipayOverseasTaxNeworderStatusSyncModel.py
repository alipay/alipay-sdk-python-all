#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTaxNeworderStatusSyncModel(object):

    def __init__(self):
        self._doc_id = None
        self._extend_param = None
        self._status = None
        self._status_change_time = None
        self._status_msg = None
        self._tax_order_no = None
        self._tax_payment_no = None

    @property
    def doc_id(self):
        return self._doc_id

    @doc_id.setter
    def doc_id(self, value):
        self._doc_id = value
    @property
    def extend_param(self):
        return self._extend_param

    @extend_param.setter
    def extend_param(self, value):
        self._extend_param = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_change_time(self):
        return self._status_change_time

    @status_change_time.setter
    def status_change_time(self, value):
        self._status_change_time = value
    @property
    def status_msg(self):
        return self._status_msg

    @status_msg.setter
    def status_msg(self, value):
        self._status_msg = value
    @property
    def tax_order_no(self):
        return self._tax_order_no

    @tax_order_no.setter
    def tax_order_no(self, value):
        self._tax_order_no = value
    @property
    def tax_payment_no(self):
        return self._tax_payment_no

    @tax_payment_no.setter
    def tax_payment_no(self, value):
        self._tax_payment_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.doc_id:
            if hasattr(self.doc_id, 'to_alipay_dict'):
                params['doc_id'] = self.doc_id.to_alipay_dict()
            else:
                params['doc_id'] = self.doc_id
        if self.extend_param:
            if hasattr(self.extend_param, 'to_alipay_dict'):
                params['extend_param'] = self.extend_param.to_alipay_dict()
            else:
                params['extend_param'] = self.extend_param
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_change_time:
            if hasattr(self.status_change_time, 'to_alipay_dict'):
                params['status_change_time'] = self.status_change_time.to_alipay_dict()
            else:
                params['status_change_time'] = self.status_change_time
        if self.status_msg:
            if hasattr(self.status_msg, 'to_alipay_dict'):
                params['status_msg'] = self.status_msg.to_alipay_dict()
            else:
                params['status_msg'] = self.status_msg
        if self.tax_order_no:
            if hasattr(self.tax_order_no, 'to_alipay_dict'):
                params['tax_order_no'] = self.tax_order_no.to_alipay_dict()
            else:
                params['tax_order_no'] = self.tax_order_no
        if self.tax_payment_no:
            if hasattr(self.tax_payment_no, 'to_alipay_dict'):
                params['tax_payment_no'] = self.tax_payment_no.to_alipay_dict()
            else:
                params['tax_payment_no'] = self.tax_payment_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTaxNeworderStatusSyncModel()
        if 'doc_id' in d:
            o.doc_id = d['doc_id']
        if 'extend_param' in d:
            o.extend_param = d['extend_param']
        if 'status' in d:
            o.status = d['status']
        if 'status_change_time' in d:
            o.status_change_time = d['status_change_time']
        if 'status_msg' in d:
            o.status_msg = d['status_msg']
        if 'tax_order_no' in d:
            o.tax_order_no = d['tax_order_no']
        if 'tax_payment_no' in d:
            o.tax_payment_no = d['tax_payment_no']
        return o


