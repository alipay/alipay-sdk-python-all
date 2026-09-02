#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActualVisitInfo import ActualVisitInfo
from alipay.aop.api.domain.ClinicInfo import ClinicInfo
from alipay.aop.api.domain.FulfillmentMaterialInfo import FulfillmentMaterialInfo
from alipay.aop.api.domain.FulfillmentPatientInfo import FulfillmentPatientInfo


class RegistrationGreenChannelFulfillmentDetailData(object):

    def __init__(self):
        self._actual_visit_info = None
        self._cancel_reason = None
        self._cancel_remark = None
        self._cancel_time = None
        self._clinic_info = None
        self._confirmed_time = None
        self._create_time = None
        self._finish_time = None
        self._material_info = None
        self._patient_info = None
        self._processed_time = None
        self._reserved_time = None
        self._update_time = None

    @property
    def actual_visit_info(self):
        return self._actual_visit_info

    @actual_visit_info.setter
    def actual_visit_info(self, value):
        if isinstance(value, ActualVisitInfo):
            self._actual_visit_info = value
        else:
            self._actual_visit_info = ActualVisitInfo.from_alipay_dict(value)
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
    def confirmed_time(self):
        return self._confirmed_time

    @confirmed_time.setter
    def confirmed_time(self, value):
        self._confirmed_time = value
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
    def material_info(self):
        return self._material_info

    @material_info.setter
    def material_info(self, value):
        if isinstance(value, FulfillmentMaterialInfo):
            self._material_info = value
        else:
            self._material_info = FulfillmentMaterialInfo.from_alipay_dict(value)
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
    def processed_time(self):
        return self._processed_time

    @processed_time.setter
    def processed_time(self, value):
        self._processed_time = value
    @property
    def reserved_time(self):
        return self._reserved_time

    @reserved_time.setter
    def reserved_time(self, value):
        self._reserved_time = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_visit_info:
            if hasattr(self.actual_visit_info, 'to_alipay_dict'):
                params['actual_visit_info'] = self.actual_visit_info.to_alipay_dict()
            else:
                params['actual_visit_info'] = self.actual_visit_info
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
        if self.confirmed_time:
            if hasattr(self.confirmed_time, 'to_alipay_dict'):
                params['confirmed_time'] = self.confirmed_time.to_alipay_dict()
            else:
                params['confirmed_time'] = self.confirmed_time
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
        if self.material_info:
            if hasattr(self.material_info, 'to_alipay_dict'):
                params['material_info'] = self.material_info.to_alipay_dict()
            else:
                params['material_info'] = self.material_info
        if self.patient_info:
            if hasattr(self.patient_info, 'to_alipay_dict'):
                params['patient_info'] = self.patient_info.to_alipay_dict()
            else:
                params['patient_info'] = self.patient_info
        if self.processed_time:
            if hasattr(self.processed_time, 'to_alipay_dict'):
                params['processed_time'] = self.processed_time.to_alipay_dict()
            else:
                params['processed_time'] = self.processed_time
        if self.reserved_time:
            if hasattr(self.reserved_time, 'to_alipay_dict'):
                params['reserved_time'] = self.reserved_time.to_alipay_dict()
            else:
                params['reserved_time'] = self.reserved_time
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
        o = RegistrationGreenChannelFulfillmentDetailData()
        if 'actual_visit_info' in d:
            o.actual_visit_info = d['actual_visit_info']
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'cancel_remark' in d:
            o.cancel_remark = d['cancel_remark']
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'clinic_info' in d:
            o.clinic_info = d['clinic_info']
        if 'confirmed_time' in d:
            o.confirmed_time = d['confirmed_time']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'material_info' in d:
            o.material_info = d['material_info']
        if 'patient_info' in d:
            o.patient_info = d['patient_info']
        if 'processed_time' in d:
            o.processed_time = d['processed_time']
        if 'reserved_time' in d:
            o.reserved_time = d['reserved_time']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


