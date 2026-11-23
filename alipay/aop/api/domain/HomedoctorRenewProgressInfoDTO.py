#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HomedoctorServicePlanDTO import HomedoctorServicePlanDTO


class HomedoctorRenewProgressInfoDTO(object):

    def __init__(self):
        self._new_service_plan_id = None
        self._new_sign_end_date = None
        self._new_sign_start_date = None
        self._reject_reason = None
        self._service_plan_list = None

    @property
    def new_service_plan_id(self):
        return self._new_service_plan_id

    @new_service_plan_id.setter
    def new_service_plan_id(self, value):
        self._new_service_plan_id = value
    @property
    def new_sign_end_date(self):
        return self._new_sign_end_date

    @new_sign_end_date.setter
    def new_sign_end_date(self, value):
        self._new_sign_end_date = value
    @property
    def new_sign_start_date(self):
        return self._new_sign_start_date

    @new_sign_start_date.setter
    def new_sign_start_date(self, value):
        self._new_sign_start_date = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def service_plan_list(self):
        return self._service_plan_list

    @service_plan_list.setter
    def service_plan_list(self, value):
        if isinstance(value, list):
            self._service_plan_list = list()
            for i in value:
                if isinstance(i, HomedoctorServicePlanDTO):
                    self._service_plan_list.append(i)
                else:
                    self._service_plan_list.append(HomedoctorServicePlanDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.new_service_plan_id:
            if hasattr(self.new_service_plan_id, 'to_alipay_dict'):
                params['new_service_plan_id'] = self.new_service_plan_id.to_alipay_dict()
            else:
                params['new_service_plan_id'] = self.new_service_plan_id
        if self.new_sign_end_date:
            if hasattr(self.new_sign_end_date, 'to_alipay_dict'):
                params['new_sign_end_date'] = self.new_sign_end_date.to_alipay_dict()
            else:
                params['new_sign_end_date'] = self.new_sign_end_date
        if self.new_sign_start_date:
            if hasattr(self.new_sign_start_date, 'to_alipay_dict'):
                params['new_sign_start_date'] = self.new_sign_start_date.to_alipay_dict()
            else:
                params['new_sign_start_date'] = self.new_sign_start_date
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.service_plan_list:
            if isinstance(self.service_plan_list, list):
                for i in range(0, len(self.service_plan_list)):
                    element = self.service_plan_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_plan_list[i] = element.to_alipay_dict()
            if hasattr(self.service_plan_list, 'to_alipay_dict'):
                params['service_plan_list'] = self.service_plan_list.to_alipay_dict()
            else:
                params['service_plan_list'] = self.service_plan_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HomedoctorRenewProgressInfoDTO()
        if 'new_service_plan_id' in d:
            o.new_service_plan_id = d['new_service_plan_id']
        if 'new_sign_end_date' in d:
            o.new_sign_end_date = d['new_sign_end_date']
        if 'new_sign_start_date' in d:
            o.new_sign_start_date = d['new_sign_start_date']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'service_plan_list' in d:
            o.service_plan_list = d['service_plan_list']
        return o


