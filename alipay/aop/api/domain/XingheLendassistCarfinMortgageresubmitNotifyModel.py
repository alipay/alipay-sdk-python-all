#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgreementFile import AgreementFile
from alipay.aop.api.domain.CarfinMortgageReceivedFile import CarfinMortgageReceivedFile
from alipay.aop.api.domain.CarfinMortgageVehicleInfo import CarfinMortgageVehicleInfo


class XingheLendassistCarfinMortgageresubmitNotifyModel(object):

    def __init__(self):
        self._agreement_file_list = None
        self._apply_no = None
        self._approve_file_list = None
        self._lend_apply_no = None
        self._mortgage_no = None
        self._out_apply_no = None
        self._out_lend_apply_no = None
        self._vehicle_info = None

    @property
    def agreement_file_list(self):
        return self._agreement_file_list

    @agreement_file_list.setter
    def agreement_file_list(self, value):
        if isinstance(value, list):
            self._agreement_file_list = list()
            for i in value:
                if isinstance(i, AgreementFile):
                    self._agreement_file_list.append(i)
                else:
                    self._agreement_file_list.append(AgreementFile.from_alipay_dict(i))
    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def approve_file_list(self):
        return self._approve_file_list

    @approve_file_list.setter
    def approve_file_list(self, value):
        if isinstance(value, list):
            self._approve_file_list = list()
            for i in value:
                if isinstance(i, CarfinMortgageReceivedFile):
                    self._approve_file_list.append(i)
                else:
                    self._approve_file_list.append(CarfinMortgageReceivedFile.from_alipay_dict(i))
    @property
    def lend_apply_no(self):
        return self._lend_apply_no

    @lend_apply_no.setter
    def lend_apply_no(self, value):
        self._lend_apply_no = value
    @property
    def mortgage_no(self):
        return self._mortgage_no

    @mortgage_no.setter
    def mortgage_no(self, value):
        self._mortgage_no = value
    @property
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value
    @property
    def out_lend_apply_no(self):
        return self._out_lend_apply_no

    @out_lend_apply_no.setter
    def out_lend_apply_no(self, value):
        self._out_lend_apply_no = value
    @property
    def vehicle_info(self):
        return self._vehicle_info

    @vehicle_info.setter
    def vehicle_info(self, value):
        if isinstance(value, CarfinMortgageVehicleInfo):
            self._vehicle_info = value
        else:
            self._vehicle_info = CarfinMortgageVehicleInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_file_list:
            if isinstance(self.agreement_file_list, list):
                for i in range(0, len(self.agreement_file_list)):
                    element = self.agreement_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.agreement_file_list[i] = element.to_alipay_dict()
            if hasattr(self.agreement_file_list, 'to_alipay_dict'):
                params['agreement_file_list'] = self.agreement_file_list.to_alipay_dict()
            else:
                params['agreement_file_list'] = self.agreement_file_list
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.approve_file_list:
            if isinstance(self.approve_file_list, list):
                for i in range(0, len(self.approve_file_list)):
                    element = self.approve_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.approve_file_list[i] = element.to_alipay_dict()
            if hasattr(self.approve_file_list, 'to_alipay_dict'):
                params['approve_file_list'] = self.approve_file_list.to_alipay_dict()
            else:
                params['approve_file_list'] = self.approve_file_list
        if self.lend_apply_no:
            if hasattr(self.lend_apply_no, 'to_alipay_dict'):
                params['lend_apply_no'] = self.lend_apply_no.to_alipay_dict()
            else:
                params['lend_apply_no'] = self.lend_apply_no
        if self.mortgage_no:
            if hasattr(self.mortgage_no, 'to_alipay_dict'):
                params['mortgage_no'] = self.mortgage_no.to_alipay_dict()
            else:
                params['mortgage_no'] = self.mortgage_no
        if self.out_apply_no:
            if hasattr(self.out_apply_no, 'to_alipay_dict'):
                params['out_apply_no'] = self.out_apply_no.to_alipay_dict()
            else:
                params['out_apply_no'] = self.out_apply_no
        if self.out_lend_apply_no:
            if hasattr(self.out_lend_apply_no, 'to_alipay_dict'):
                params['out_lend_apply_no'] = self.out_lend_apply_no.to_alipay_dict()
            else:
                params['out_lend_apply_no'] = self.out_lend_apply_no
        if self.vehicle_info:
            if hasattr(self.vehicle_info, 'to_alipay_dict'):
                params['vehicle_info'] = self.vehicle_info.to_alipay_dict()
            else:
                params['vehicle_info'] = self.vehicle_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinMortgageresubmitNotifyModel()
        if 'agreement_file_list' in d:
            o.agreement_file_list = d['agreement_file_list']
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'approve_file_list' in d:
            o.approve_file_list = d['approve_file_list']
        if 'lend_apply_no' in d:
            o.lend_apply_no = d['lend_apply_no']
        if 'mortgage_no' in d:
            o.mortgage_no = d['mortgage_no']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        if 'out_lend_apply_no' in d:
            o.out_lend_apply_no = d['out_lend_apply_no']
        if 'vehicle_info' in d:
            o.vehicle_info = d['vehicle_info']
        return o


