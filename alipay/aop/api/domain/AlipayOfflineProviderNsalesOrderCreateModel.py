#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceRecordInfo import DeviceRecordInfo
from alipay.aop.api.domain.SalesSolutionExt import SalesSolutionExt


class AlipayOfflineProviderNsalesOrderCreateModel(object):

    def __init__(self):
        self._device_record_files = None
        self._out_biz_no = None
        self._sales_solution_ext = None
        self._scene_code = None
        self._solution_id = None
        self._timeout_express = None

    @property
    def device_record_files(self):
        return self._device_record_files

    @device_record_files.setter
    def device_record_files(self, value):
        if isinstance(value, list):
            self._device_record_files = list()
            for i in value:
                if isinstance(i, DeviceRecordInfo):
                    self._device_record_files.append(i)
                else:
                    self._device_record_files.append(DeviceRecordInfo.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sales_solution_ext(self):
        return self._sales_solution_ext

    @sales_solution_ext.setter
    def sales_solution_ext(self, value):
        if isinstance(value, SalesSolutionExt):
            self._sales_solution_ext = value
        else:
            self._sales_solution_ext = SalesSolutionExt.from_alipay_dict(value)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_record_files:
            if isinstance(self.device_record_files, list):
                for i in range(0, len(self.device_record_files)):
                    element = self.device_record_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_record_files[i] = element.to_alipay_dict()
            if hasattr(self.device_record_files, 'to_alipay_dict'):
                params['device_record_files'] = self.device_record_files.to_alipay_dict()
            else:
                params['device_record_files'] = self.device_record_files
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sales_solution_ext:
            if hasattr(self.sales_solution_ext, 'to_alipay_dict'):
                params['sales_solution_ext'] = self.sales_solution_ext.to_alipay_dict()
            else:
                params['sales_solution_ext'] = self.sales_solution_ext
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.solution_id:
            if hasattr(self.solution_id, 'to_alipay_dict'):
                params['solution_id'] = self.solution_id.to_alipay_dict()
            else:
                params['solution_id'] = self.solution_id
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNsalesOrderCreateModel()
        if 'device_record_files' in d:
            o.device_record_files = d['device_record_files']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sales_solution_ext' in d:
            o.sales_solution_ext = d['sales_solution_ext']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'solution_id' in d:
            o.solution_id = d['solution_id']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        return o


