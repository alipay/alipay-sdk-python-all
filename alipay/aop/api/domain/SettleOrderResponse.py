#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettleDetailResponse import SettleDetailResponse


class SettleOrderResponse(object):

    def __init__(self):
        self._deduction_order_id = None
        self._settle_detail_response_list = None
        self._settle_fail_reason = None
        self._settle_fail_times = None
        self._settle_order_id = None
        self._settle_status = None

    @property
    def deduction_order_id(self):
        return self._deduction_order_id

    @deduction_order_id.setter
    def deduction_order_id(self, value):
        self._deduction_order_id = value
    @property
    def settle_detail_response_list(self):
        return self._settle_detail_response_list

    @settle_detail_response_list.setter
    def settle_detail_response_list(self, value):
        if isinstance(value, list):
            self._settle_detail_response_list = list()
            for i in value:
                if isinstance(i, SettleDetailResponse):
                    self._settle_detail_response_list.append(i)
                else:
                    self._settle_detail_response_list.append(SettleDetailResponse.from_alipay_dict(i))
    @property
    def settle_fail_reason(self):
        return self._settle_fail_reason

    @settle_fail_reason.setter
    def settle_fail_reason(self, value):
        self._settle_fail_reason = value
    @property
    def settle_fail_times(self):
        return self._settle_fail_times

    @settle_fail_times.setter
    def settle_fail_times(self, value):
        self._settle_fail_times = value
    @property
    def settle_order_id(self):
        return self._settle_order_id

    @settle_order_id.setter
    def settle_order_id(self, value):
        self._settle_order_id = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduction_order_id:
            if hasattr(self.deduction_order_id, 'to_alipay_dict'):
                params['deduction_order_id'] = self.deduction_order_id.to_alipay_dict()
            else:
                params['deduction_order_id'] = self.deduction_order_id
        if self.settle_detail_response_list:
            if isinstance(self.settle_detail_response_list, list):
                for i in range(0, len(self.settle_detail_response_list)):
                    element = self.settle_detail_response_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settle_detail_response_list[i] = element.to_alipay_dict()
            if hasattr(self.settle_detail_response_list, 'to_alipay_dict'):
                params['settle_detail_response_list'] = self.settle_detail_response_list.to_alipay_dict()
            else:
                params['settle_detail_response_list'] = self.settle_detail_response_list
        if self.settle_fail_reason:
            if hasattr(self.settle_fail_reason, 'to_alipay_dict'):
                params['settle_fail_reason'] = self.settle_fail_reason.to_alipay_dict()
            else:
                params['settle_fail_reason'] = self.settle_fail_reason
        if self.settle_fail_times:
            if hasattr(self.settle_fail_times, 'to_alipay_dict'):
                params['settle_fail_times'] = self.settle_fail_times.to_alipay_dict()
            else:
                params['settle_fail_times'] = self.settle_fail_times
        if self.settle_order_id:
            if hasattr(self.settle_order_id, 'to_alipay_dict'):
                params['settle_order_id'] = self.settle_order_id.to_alipay_dict()
            else:
                params['settle_order_id'] = self.settle_order_id
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettleOrderResponse()
        if 'deduction_order_id' in d:
            o.deduction_order_id = d['deduction_order_id']
        if 'settle_detail_response_list' in d:
            o.settle_detail_response_list = d['settle_detail_response_list']
        if 'settle_fail_reason' in d:
            o.settle_fail_reason = d['settle_fail_reason']
        if 'settle_fail_times' in d:
            o.settle_fail_times = d['settle_fail_times']
        if 'settle_order_id' in d:
            o.settle_order_id = d['settle_order_id']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        return o


