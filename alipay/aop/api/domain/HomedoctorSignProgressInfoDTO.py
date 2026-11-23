#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HomedoctorServicePlanDTO import HomedoctorServicePlanDTO


class HomedoctorSignProgressInfoDTO(object):

    def __init__(self):
        self._doctor_id = None
        self._doctor_name = None
        self._fee = None
        self._latitude = None
        self._longitude = None
        self._org_address = None
        self._org_code = None
        self._org_name = None
        self._pay_amount = None
        self._pay_time = None
        self._period = None
        self._reject_reason = None
        self._service_plan_id = None
        self._service_plan_list = None
        self._service_plan_name = None
        self._sign_end_date = None
        self._sign_start_date = None
        self._team_id = None
        self._team_name = None

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def org_address(self):
        return self._org_address

    @org_address.setter
    def org_address(self, value):
        self._org_address = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def service_plan_id(self):
        return self._service_plan_id

    @service_plan_id.setter
    def service_plan_id(self, value):
        self._service_plan_id = value
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
    @property
    def service_plan_name(self):
        return self._service_plan_name

    @service_plan_name.setter
    def service_plan_name(self, value):
        self._service_plan_name = value
    @property
    def sign_end_date(self):
        return self._sign_end_date

    @sign_end_date.setter
    def sign_end_date(self, value):
        self._sign_end_date = value
    @property
    def sign_start_date(self):
        return self._sign_start_date

    @sign_start_date.setter
    def sign_start_date(self, value):
        self._sign_start_date = value
    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, value):
        self._team_id = value
    @property
    def team_name(self):
        return self._team_name

    @team_name.setter
    def team_name(self, value):
        self._team_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.fee:
            if hasattr(self.fee, 'to_alipay_dict'):
                params['fee'] = self.fee.to_alipay_dict()
            else:
                params['fee'] = self.fee
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.org_address:
            if hasattr(self.org_address, 'to_alipay_dict'):
                params['org_address'] = self.org_address.to_alipay_dict()
            else:
                params['org_address'] = self.org_address
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.service_plan_id:
            if hasattr(self.service_plan_id, 'to_alipay_dict'):
                params['service_plan_id'] = self.service_plan_id.to_alipay_dict()
            else:
                params['service_plan_id'] = self.service_plan_id
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
        if self.service_plan_name:
            if hasattr(self.service_plan_name, 'to_alipay_dict'):
                params['service_plan_name'] = self.service_plan_name.to_alipay_dict()
            else:
                params['service_plan_name'] = self.service_plan_name
        if self.sign_end_date:
            if hasattr(self.sign_end_date, 'to_alipay_dict'):
                params['sign_end_date'] = self.sign_end_date.to_alipay_dict()
            else:
                params['sign_end_date'] = self.sign_end_date
        if self.sign_start_date:
            if hasattr(self.sign_start_date, 'to_alipay_dict'):
                params['sign_start_date'] = self.sign_start_date.to_alipay_dict()
            else:
                params['sign_start_date'] = self.sign_start_date
        if self.team_id:
            if hasattr(self.team_id, 'to_alipay_dict'):
                params['team_id'] = self.team_id.to_alipay_dict()
            else:
                params['team_id'] = self.team_id
        if self.team_name:
            if hasattr(self.team_name, 'to_alipay_dict'):
                params['team_name'] = self.team_name.to_alipay_dict()
            else:
                params['team_name'] = self.team_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HomedoctorSignProgressInfoDTO()
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'fee' in d:
            o.fee = d['fee']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'org_address' in d:
            o.org_address = d['org_address']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'period' in d:
            o.period = d['period']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'service_plan_id' in d:
            o.service_plan_id = d['service_plan_id']
        if 'service_plan_list' in d:
            o.service_plan_list = d['service_plan_list']
        if 'service_plan_name' in d:
            o.service_plan_name = d['service_plan_name']
        if 'sign_end_date' in d:
            o.sign_end_date = d['sign_end_date']
        if 'sign_start_date' in d:
            o.sign_start_date = d['sign_start_date']
        if 'team_id' in d:
            o.team_id = d['team_id']
        if 'team_name' in d:
            o.team_name = d['team_name']
        return o


