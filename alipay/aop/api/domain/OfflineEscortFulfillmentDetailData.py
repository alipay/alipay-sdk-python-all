#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ClinicInfo import ClinicInfo
from alipay.aop.api.domain.FulfillmentPatientInfo import FulfillmentPatientInfo
from alipay.aop.api.domain.ServiceResult import ServiceResult
from alipay.aop.api.domain.FulfillmentStaffInfo import FulfillmentStaffInfo


class OfflineEscortFulfillmentDetailData(object):

    def __init__(self):
        self._cancel_reason = None
        self._cancel_remark = None
        self._cancel_time = None
        self._clinic_info = None
        self._close_reason = None
        self._close_remark = None
        self._close_time = None
        self._create_time = None
        self._finish_time = None
        self._patient_info = None
        self._scheduled_time = None
        self._service_end_time = None
        self._service_result = None
        self._service_start_time = None
        self._staff_info = None
        self._update_time = None

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
    def clinic_info(self):
        return self._clinic_info

    @clinic_info.setter
    def clinic_info(self, value):
        if isinstance(value, ClinicInfo):
            self._clinic_info = value
        else:
            self._clinic_info = ClinicInfo.from_alipay_dict(value)
    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
    @property
    def close_remark(self):
        return self._close_remark

    @close_remark.setter
    def close_remark(self, value):
        self._close_remark = value
    @property
    def close_time(self):
        return self._close_time

    @close_time.setter
    def close_time(self, value):
        self._close_time = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
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
        if isinstance(value, FulfillmentPatientInfo):
            self._patient_info = value
        else:
            self._patient_info = FulfillmentPatientInfo.from_alipay_dict(value)
    @property
    def scheduled_time(self):
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, value):
        self._scheduled_time = value
    @property
    def service_end_time(self):
        return self._service_end_time

    @service_end_time.setter
    def service_end_time(self, value):
        self._service_end_time = value
    @property
    def service_result(self):
        return self._service_result

    @service_result.setter
    def service_result(self, value):
        if isinstance(value, ServiceResult):
            self._service_result = value
        else:
            self._service_result = ServiceResult.from_alipay_dict(value)
    @property
    def service_start_time(self):
        return self._service_start_time

    @service_start_time.setter
    def service_start_time(self, value):
        self._service_start_time = value
    @property
    def staff_info(self):
        return self._staff_info

    @staff_info.setter
    def staff_info(self, value):
        if isinstance(value, FulfillmentStaffInfo):
            self._staff_info = value
        else:
            self._staff_info = FulfillmentStaffInfo.from_alipay_dict(value)
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.clinic_info:
            if hasattr(self.clinic_info, 'to_alipay_dict'):
                params['clinic_info'] = self.clinic_info.to_alipay_dict()
            else:
                params['clinic_info'] = self.clinic_info
        if self.close_reason:
            if hasattr(self.close_reason, 'to_alipay_dict'):
                params['close_reason'] = self.close_reason.to_alipay_dict()
            else:
                params['close_reason'] = self.close_reason
        if self.close_remark:
            if hasattr(self.close_remark, 'to_alipay_dict'):
                params['close_remark'] = self.close_remark.to_alipay_dict()
            else:
                params['close_remark'] = self.close_remark
        if self.close_time:
            if hasattr(self.close_time, 'to_alipay_dict'):
                params['close_time'] = self.close_time.to_alipay_dict()
            else:
                params['close_time'] = self.close_time
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
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
        if self.scheduled_time:
            if hasattr(self.scheduled_time, 'to_alipay_dict'):
                params['scheduled_time'] = self.scheduled_time.to_alipay_dict()
            else:
                params['scheduled_time'] = self.scheduled_time
        if self.service_end_time:
            if hasattr(self.service_end_time, 'to_alipay_dict'):
                params['service_end_time'] = self.service_end_time.to_alipay_dict()
            else:
                params['service_end_time'] = self.service_end_time
        if self.service_result:
            if hasattr(self.service_result, 'to_alipay_dict'):
                params['service_result'] = self.service_result.to_alipay_dict()
            else:
                params['service_result'] = self.service_result
        if self.service_start_time:
            if hasattr(self.service_start_time, 'to_alipay_dict'):
                params['service_start_time'] = self.service_start_time.to_alipay_dict()
            else:
                params['service_start_time'] = self.service_start_time
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
        o = OfflineEscortFulfillmentDetailData()
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'cancel_remark' in d:
            o.cancel_remark = d['cancel_remark']
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'clinic_info' in d:
            o.clinic_info = d['clinic_info']
        if 'close_reason' in d:
            o.close_reason = d['close_reason']
        if 'close_remark' in d:
            o.close_remark = d['close_remark']
        if 'close_time' in d:
            o.close_time = d['close_time']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'patient_info' in d:
            o.patient_info = d['patient_info']
        if 'scheduled_time' in d:
            o.scheduled_time = d['scheduled_time']
        if 'service_end_time' in d:
            o.service_end_time = d['service_end_time']
        if 'service_result' in d:
            o.service_result = d['service_result']
        if 'service_start_time' in d:
            o.service_start_time = d['service_start_time']
        if 'staff_info' in d:
            o.staff_info = d['staff_info']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


