#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotbpaasLavidabilldetailQueryModel(object):

    def __init__(self):
        self._gmt_recv_pay = None
        self._rp_record_id = None
        self._rp_record_type = None

    @property
    def gmt_recv_pay(self):
        return self._gmt_recv_pay

    @gmt_recv_pay.setter
    def gmt_recv_pay(self, value):
        self._gmt_recv_pay = value
    @property
    def rp_record_id(self):
        return self._rp_record_id

    @rp_record_id.setter
    def rp_record_id(self, value):
        self._rp_record_id = value
    @property
    def rp_record_type(self):
        return self._rp_record_type

    @rp_record_type.setter
    def rp_record_type(self, value):
        self._rp_record_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_recv_pay:
            if hasattr(self.gmt_recv_pay, 'to_alipay_dict'):
                params['gmt_recv_pay'] = self.gmt_recv_pay.to_alipay_dict()
            else:
                params['gmt_recv_pay'] = self.gmt_recv_pay
        if self.rp_record_id:
            if hasattr(self.rp_record_id, 'to_alipay_dict'):
                params['rp_record_id'] = self.rp_record_id.to_alipay_dict()
            else:
                params['rp_record_id'] = self.rp_record_id
        if self.rp_record_type:
            if hasattr(self.rp_record_type, 'to_alipay_dict'):
                params['rp_record_type'] = self.rp_record_type.to_alipay_dict()
            else:
                params['rp_record_type'] = self.rp_record_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotbpaasLavidabilldetailQueryModel()
        if 'gmt_recv_pay' in d:
            o.gmt_recv_pay = d['gmt_recv_pay']
        if 'rp_record_id' in d:
            o.rp_record_id = d['rp_record_id']
        if 'rp_record_type' in d:
            o.rp_record_type = d['rp_record_type']
        return o


