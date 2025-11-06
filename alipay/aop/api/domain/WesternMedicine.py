#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WesternMedicationInformation import WesternMedicationInformation


class WesternMedicine(object):

    def __init__(self):
        self._medication_information_list = None

    @property
    def medication_information_list(self):
        return self._medication_information_list

    @medication_information_list.setter
    def medication_information_list(self, value):
        if isinstance(value, list):
            self._medication_information_list = list()
            for i in value:
                if isinstance(i, WesternMedicationInformation):
                    self._medication_information_list.append(i)
                else:
                    self._medication_information_list.append(WesternMedicationInformation.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.medication_information_list:
            if isinstance(self.medication_information_list, list):
                for i in range(0, len(self.medication_information_list)):
                    element = self.medication_information_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.medication_information_list[i] = element.to_alipay_dict()
            if hasattr(self.medication_information_list, 'to_alipay_dict'):
                params['medication_information_list'] = self.medication_information_list.to_alipay_dict()
            else:
                params['medication_information_list'] = self.medication_information_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WesternMedicine()
        if 'medication_information_list' in d:
            o.medication_information_list = d['medication_information_list']
        return o


