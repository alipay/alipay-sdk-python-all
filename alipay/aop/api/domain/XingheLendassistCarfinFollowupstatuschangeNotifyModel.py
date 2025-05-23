#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomerServiceInfo import CustomerServiceInfo


class XingheLendassistCarfinFollowupstatuschangeNotifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._blocking_status = None
        self._customer_service_info = None
        self._followup_res_list = None
        self._followup_status = None
        self._out_apply_no = None
        self._status = None
        self._vehicle_mortgage_expiry_date = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def blocking_status(self):
        return self._blocking_status

    @blocking_status.setter
    def blocking_status(self, value):
        self._blocking_status = value
    @property
    def customer_service_info(self):
        return self._customer_service_info

    @customer_service_info.setter
    def customer_service_info(self, value):
        if isinstance(value, CustomerServiceInfo):
            self._customer_service_info = value
        else:
            self._customer_service_info = CustomerServiceInfo.from_alipay_dict(value)
    @property
    def followup_res_list(self):
        return self._followup_res_list

    @followup_res_list.setter
    def followup_res_list(self, value):
        if isinstance(value, list):
            self._followup_res_list = list()
            for i in value:
                self._followup_res_list.append(i)
    @property
    def followup_status(self):
        return self._followup_status

    @followup_status.setter
    def followup_status(self, value):
        self._followup_status = value
    @property
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def vehicle_mortgage_expiry_date(self):
        return self._vehicle_mortgage_expiry_date

    @vehicle_mortgage_expiry_date.setter
    def vehicle_mortgage_expiry_date(self, value):
        self._vehicle_mortgage_expiry_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.blocking_status:
            if hasattr(self.blocking_status, 'to_alipay_dict'):
                params['blocking_status'] = self.blocking_status.to_alipay_dict()
            else:
                params['blocking_status'] = self.blocking_status
        if self.customer_service_info:
            if hasattr(self.customer_service_info, 'to_alipay_dict'):
                params['customer_service_info'] = self.customer_service_info.to_alipay_dict()
            else:
                params['customer_service_info'] = self.customer_service_info
        if self.followup_res_list:
            if isinstance(self.followup_res_list, list):
                for i in range(0, len(self.followup_res_list)):
                    element = self.followup_res_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.followup_res_list[i] = element.to_alipay_dict()
            if hasattr(self.followup_res_list, 'to_alipay_dict'):
                params['followup_res_list'] = self.followup_res_list.to_alipay_dict()
            else:
                params['followup_res_list'] = self.followup_res_list
        if self.followup_status:
            if hasattr(self.followup_status, 'to_alipay_dict'):
                params['followup_status'] = self.followup_status.to_alipay_dict()
            else:
                params['followup_status'] = self.followup_status
        if self.out_apply_no:
            if hasattr(self.out_apply_no, 'to_alipay_dict'):
                params['out_apply_no'] = self.out_apply_no.to_alipay_dict()
            else:
                params['out_apply_no'] = self.out_apply_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.vehicle_mortgage_expiry_date:
            if hasattr(self.vehicle_mortgage_expiry_date, 'to_alipay_dict'):
                params['vehicle_mortgage_expiry_date'] = self.vehicle_mortgage_expiry_date.to_alipay_dict()
            else:
                params['vehicle_mortgage_expiry_date'] = self.vehicle_mortgage_expiry_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinFollowupstatuschangeNotifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'blocking_status' in d:
            o.blocking_status = d['blocking_status']
        if 'customer_service_info' in d:
            o.customer_service_info = d['customer_service_info']
        if 'followup_res_list' in d:
            o.followup_res_list = d['followup_res_list']
        if 'followup_status' in d:
            o.followup_status = d['followup_status']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        if 'status' in d:
            o.status = d['status']
        if 'vehicle_mortgage_expiry_date' in d:
            o.vehicle_mortgage_expiry_date = d['vehicle_mortgage_expiry_date']
        return o


