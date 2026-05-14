#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CareInfo import CareInfo
from alipay.aop.api.domain.InpatientNursingPatientInfo import InpatientNursingPatientInfo
from alipay.aop.api.domain.InpatientNursingServiceResult import InpatientNursingServiceResult
from alipay.aop.api.domain.InpatientNursingStaffInfo import InpatientNursingStaffInfo


class InpatientNursingFulfillmentDetailData(object):

    def __init__(self):
        self._arrival_time = None
        self._cancel_reason = None
        self._cancel_remark = None
        self._cancel_time = None
        self._care_info = None
        self._completion_time = None
        self._create_time = None
        self._departure_time = None
        self._finish_time = None
        self._patient_info = None
        self._service_result = None
        self._staff_info = None
        self._update_time = None

    @property
    def arrival_time(self):
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, value):
        self._arrival_time = value
    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def cancel_remark(self):
        return self._cancel_remark

    @cancel_remark.setter
    def cancel_remark(self, value):
        self._cancel_remark = value
    @property
    def cancel_time(self):
        return self._cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self._cancel_time = value
    @property
    def care_info(self):
        return self._care_info

    @care_info.setter
    def care_info(self, value):
        if isinstance(value, CareInfo):
            self._care_info = value
        else:
            self._care_info = CareInfo.from_alipay_dict(value)
    @property
    def completion_time(self):
        return self._completion_time

    @completion_time.setter
    def completion_time(self, value):
        self._completion_time = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def departure_time(self):
        return self._departure_time

    @departure_time.setter
    def departure_time(self, value):
        self._departure_time = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def patient_info(self):
        return self._patient_info

    @patient_info.setter
    def patient_info(self, value):
        if isinstance(value, InpatientNursingPatientInfo):
            self._patient_info = value
        else:
            self._patient_info = InpatientNursingPatientInfo.from_alipay_dict(value)
    @property
    def service_result(self):
        return self._service_result

    @service_result.setter
    def service_result(self, value):
        if isinstance(value, InpatientNursingServiceResult):
            self._service_result = value
        else:
            self._service_result = InpatientNursingServiceResult.from_alipay_dict(value)
    @property
    def staff_info(self):
        return self._staff_info

    @staff_info.setter
    def staff_info(self, value):
        if isinstance(value, InpatientNursingStaffInfo):
            self._staff_info = value
        else:
            self._staff_info = InpatientNursingStaffInfo.from_alipay_dict(value)
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.arrival_time:
            if hasattr(self.arrival_time, 'to_alipay_dict'):
                params['arrival_time'] = self.arrival_time.to_alipay_dict()
            else:
                params['arrival_time'] = self.arrival_time
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.cancel_remark:
            if hasattr(self.cancel_remark, 'to_alipay_dict'):
                params['cancel_remark'] = self.cancel_remark.to_alipay_dict()
            else:
                params['cancel_remark'] = self.cancel_remark
        if self.cancel_time:
            if hasattr(self.cancel_time, 'to_alipay_dict'):
                params['cancel_time'] = self.cancel_time.to_alipay_dict()
            else:
                params['cancel_time'] = self.cancel_time
        if self.care_info:
            if hasattr(self.care_info, 'to_alipay_dict'):
                params['care_info'] = self.care_info.to_alipay_dict()
            else:
                params['care_info'] = self.care_info
        if self.completion_time:
            if hasattr(self.completion_time, 'to_alipay_dict'):
                params['completion_time'] = self.completion_time.to_alipay_dict()
            else:
                params['completion_time'] = self.completion_time
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.departure_time:
            if hasattr(self.departure_time, 'to_alipay_dict'):
                params['departure_time'] = self.departure_time.to_alipay_dict()
            else:
                params['departure_time'] = self.departure_time
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
        if self.patient_info:
            if hasattr(self.patient_info, 'to_alipay_dict'):
                params['patient_info'] = self.patient_info.to_alipay_dict()
            else:
                params['patient_info'] = self.patient_info
        if self.service_result:
            if hasattr(self.service_result, 'to_alipay_dict'):
                params['service_result'] = self.service_result.to_alipay_dict()
            else:
                params['service_result'] = self.service_result
        if self.staff_info:
            if hasattr(self.staff_info, 'to_alipay_dict'):
                params['staff_info'] = self.staff_info.to_alipay_dict()
            else:
                params['staff_info'] = self.staff_info
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InpatientNursingFulfillmentDetailData()
        if 'arrival_time' in d:
            o.arrival_time = d['arrival_time']
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'cancel_remark' in d:
            o.cancel_remark = d['cancel_remark']
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'care_info' in d:
            o.care_info = d['care_info']
        if 'completion_time' in d:
            o.completion_time = d['completion_time']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'departure_time' in d:
            o.departure_time = d['departure_time']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'patient_info' in d:
            o.patient_info = d['patient_info']
        if 'service_result' in d:
            o.service_result = d['service_result']
        if 'staff_info' in d:
            o.staff_info = d['staff_info']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


