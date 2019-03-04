#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LogisticsExternalInfo import LogisticsExternalInfo


class KoubeiTradeKbdeliveryDeliveryApplyModel(object):

    def __init__(self):
        self._attach = None
        self._logistics_external_info = None
        self._logistics_type = None
        self._order_no = None
        self._remark = None
        self._request_id = None

    @property
    def attach(self):
        return self._attach

    @attach.setter
    def attach(self, value):
        self._attach = value
    @property
    def logistics_external_info(self):
        return self._logistics_external_info

    @logistics_external_info.setter
    def logistics_external_info(self, value):
        if isinstance(value, LogisticsExternalInfo):
            self._logistics_external_info = value
        else:
            self._logistics_external_info = LogisticsExternalInfo.from_alipay_dict(value)
    @property
    def logistics_type(self):
        return self._logistics_type

    @logistics_type.setter
    def logistics_type(self, value):
        self._logistics_type = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attach:
            if hasattr(self.attach, 'to_alipay_dict'):
                params['attach'] = self.attach.to_alipay_dict()
            else:
                params['attach'] = self.attach
        if self.logistics_external_info:
            if hasattr(self.logistics_external_info, 'to_alipay_dict'):
                params['logistics_external_info'] = self.logistics_external_info.to_alipay_dict()
            else:
                params['logistics_external_info'] = self.logistics_external_info
        if self.logistics_type:
            if hasattr(self.logistics_type, 'to_alipay_dict'):
                params['logistics_type'] = self.logistics_type.to_alipay_dict()
            else:
                params['logistics_type'] = self.logistics_type
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeKbdeliveryDeliveryApplyModel()
        if 'attach' in d:
            o.attach = d['attach']
        if 'logistics_external_info' in d:
            o.logistics_external_info = d['logistics_external_info']
        if 'logistics_type' in d:
            o.logistics_type = d['logistics_type']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'remark' in d:
            o.remark = d['remark']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


