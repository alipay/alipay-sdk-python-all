#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalDoctorAgentBatchqueryModel(object):

    def __init__(self):
        self._doctor_id_list = None

    @property
    def doctor_id_list(self):
        return self._doctor_id_list

    @doctor_id_list.setter
    def doctor_id_list(self, value):
        if isinstance(value, list):
            self._doctor_id_list = list()
            for i in value:
                self._doctor_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_id_list:
            if isinstance(self.doctor_id_list, list):
                for i in range(0, len(self.doctor_id_list)):
                    element = self.doctor_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.doctor_id_list[i] = element.to_alipay_dict()
            if hasattr(self.doctor_id_list, 'to_alipay_dict'):
                params['doctor_id_list'] = self.doctor_id_list.to_alipay_dict()
            else:
                params['doctor_id_list'] = self.doctor_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalDoctorAgentBatchqueryModel()
        if 'doctor_id_list' in d:
            o.doctor_id_list = d['doctor_id_list']
        return o


