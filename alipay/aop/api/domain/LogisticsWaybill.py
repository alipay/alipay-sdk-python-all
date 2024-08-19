#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderMediaInfo import OrderMediaInfo
from alipay.aop.api.domain.WaybillStep import WaybillStep


class LogisticsWaybill(object):

    def __init__(self):
        self._additional_reason = None
        self._logistics_code = None
        self._logistics_media_list = None
        self._return_delivery_type = None
        self._status = None
        self._steps = None
        self._waybill_no = None

    @property
    def additional_reason(self):
        return self._additional_reason

    @additional_reason.setter
    def additional_reason(self, value):
        self._additional_reason = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def logistics_media_list(self):
        return self._logistics_media_list

    @logistics_media_list.setter
    def logistics_media_list(self, value):
        if isinstance(value, list):
            self._logistics_media_list = list()
            for i in value:
                if isinstance(i, OrderMediaInfo):
                    self._logistics_media_list.append(i)
                else:
                    self._logistics_media_list.append(OrderMediaInfo.from_alipay_dict(i))
    @property
    def return_delivery_type(self):
        return self._return_delivery_type

    @return_delivery_type.setter
    def return_delivery_type(self, value):
        self._return_delivery_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, value):
        if isinstance(value, list):
            self._steps = list()
            for i in value:
                if isinstance(i, WaybillStep):
                    self._steps.append(i)
                else:
                    self._steps.append(WaybillStep.from_alipay_dict(i))
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_reason:
            if hasattr(self.additional_reason, 'to_alipay_dict'):
                params['additional_reason'] = self.additional_reason.to_alipay_dict()
            else:
                params['additional_reason'] = self.additional_reason
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.logistics_media_list:
            if isinstance(self.logistics_media_list, list):
                for i in range(0, len(self.logistics_media_list)):
                    element = self.logistics_media_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logistics_media_list[i] = element.to_alipay_dict()
            if hasattr(self.logistics_media_list, 'to_alipay_dict'):
                params['logistics_media_list'] = self.logistics_media_list.to_alipay_dict()
            else:
                params['logistics_media_list'] = self.logistics_media_list
        if self.return_delivery_type:
            if hasattr(self.return_delivery_type, 'to_alipay_dict'):
                params['return_delivery_type'] = self.return_delivery_type.to_alipay_dict()
            else:
                params['return_delivery_type'] = self.return_delivery_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.steps:
            if isinstance(self.steps, list):
                for i in range(0, len(self.steps)):
                    element = self.steps[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.steps[i] = element.to_alipay_dict()
            if hasattr(self.steps, 'to_alipay_dict'):
                params['steps'] = self.steps.to_alipay_dict()
            else:
                params['steps'] = self.steps
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsWaybill()
        if 'additional_reason' in d:
            o.additional_reason = d['additional_reason']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'logistics_media_list' in d:
            o.logistics_media_list = d['logistics_media_list']
        if 'return_delivery_type' in d:
            o.return_delivery_type = d['return_delivery_type']
        if 'status' in d:
            o.status = d['status']
        if 'steps' in d:
            o.steps = d['steps']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o


