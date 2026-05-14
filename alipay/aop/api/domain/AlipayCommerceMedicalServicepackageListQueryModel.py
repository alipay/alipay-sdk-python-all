#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalServicepackageListQueryModel(object):

    def __init__(self):
        self._is_purchased = None
        self._lead_doctor_id = None
        self._package_id_list = None

    @property
    def is_purchased(self):
        return self._is_purchased

    @is_purchased.setter
    def is_purchased(self, value):
        self._is_purchased = value
    @property
    def lead_doctor_id(self):
        return self._lead_doctor_id

    @lead_doctor_id.setter
    def lead_doctor_id(self, value):
        self._lead_doctor_id = value
    @property
    def package_id_list(self):
        return self._package_id_list

    @package_id_list.setter
    def package_id_list(self, value):
        if isinstance(value, list):
            self._package_id_list = list()
            for i in value:
                self._package_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.is_purchased:
            if hasattr(self.is_purchased, 'to_alipay_dict'):
                params['is_purchased'] = self.is_purchased.to_alipay_dict()
            else:
                params['is_purchased'] = self.is_purchased
        if self.lead_doctor_id:
            if hasattr(self.lead_doctor_id, 'to_alipay_dict'):
                params['lead_doctor_id'] = self.lead_doctor_id.to_alipay_dict()
            else:
                params['lead_doctor_id'] = self.lead_doctor_id
        if self.package_id_list:
            if isinstance(self.package_id_list, list):
                for i in range(0, len(self.package_id_list)):
                    element = self.package_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.package_id_list[i] = element.to_alipay_dict()
            if hasattr(self.package_id_list, 'to_alipay_dict'):
                params['package_id_list'] = self.package_id_list.to_alipay_dict()
            else:
                params['package_id_list'] = self.package_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalServicepackageListQueryModel()
        if 'is_purchased' in d:
            o.is_purchased = d['is_purchased']
        if 'lead_doctor_id' in d:
            o.lead_doctor_id = d['lead_doctor_id']
        if 'package_id_list' in d:
            o.package_id_list = d['package_id_list']
        return o


