#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpUboInfo import EpUboInfo


class EpUboResult(object):

    def __init__(self):
        self._crn = None
        self._is_exempt = None
        self._is_normal_status = None
        self._is_transp_high = None
        self._org_name = None
        self._org_type_oversee = None
        self._standard_reg_type = None
        self._ubo_list = None

    @property
    def crn(self):
        return self._crn

    @crn.setter
    def crn(self, value):
        self._crn = value
    @property
    def is_exempt(self):
        return self._is_exempt

    @is_exempt.setter
    def is_exempt(self, value):
        self._is_exempt = value
    @property
    def is_normal_status(self):
        return self._is_normal_status

    @is_normal_status.setter
    def is_normal_status(self, value):
        self._is_normal_status = value
    @property
    def is_transp_high(self):
        return self._is_transp_high

    @is_transp_high.setter
    def is_transp_high(self, value):
        self._is_transp_high = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def org_type_oversee(self):
        return self._org_type_oversee

    @org_type_oversee.setter
    def org_type_oversee(self, value):
        self._org_type_oversee = value
    @property
    def standard_reg_type(self):
        return self._standard_reg_type

    @standard_reg_type.setter
    def standard_reg_type(self, value):
        self._standard_reg_type = value
    @property
    def ubo_list(self):
        return self._ubo_list

    @ubo_list.setter
    def ubo_list(self, value):
        if isinstance(value, list):
            self._ubo_list = list()
            for i in value:
                if isinstance(i, EpUboInfo):
                    self._ubo_list.append(i)
                else:
                    self._ubo_list.append(EpUboInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.crn:
            if hasattr(self.crn, 'to_alipay_dict'):
                params['crn'] = self.crn.to_alipay_dict()
            else:
                params['crn'] = self.crn
        if self.is_exempt:
            if hasattr(self.is_exempt, 'to_alipay_dict'):
                params['is_exempt'] = self.is_exempt.to_alipay_dict()
            else:
                params['is_exempt'] = self.is_exempt
        if self.is_normal_status:
            if hasattr(self.is_normal_status, 'to_alipay_dict'):
                params['is_normal_status'] = self.is_normal_status.to_alipay_dict()
            else:
                params['is_normal_status'] = self.is_normal_status
        if self.is_transp_high:
            if hasattr(self.is_transp_high, 'to_alipay_dict'):
                params['is_transp_high'] = self.is_transp_high.to_alipay_dict()
            else:
                params['is_transp_high'] = self.is_transp_high
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.org_type_oversee:
            if hasattr(self.org_type_oversee, 'to_alipay_dict'):
                params['org_type_oversee'] = self.org_type_oversee.to_alipay_dict()
            else:
                params['org_type_oversee'] = self.org_type_oversee
        if self.standard_reg_type:
            if hasattr(self.standard_reg_type, 'to_alipay_dict'):
                params['standard_reg_type'] = self.standard_reg_type.to_alipay_dict()
            else:
                params['standard_reg_type'] = self.standard_reg_type
        if self.ubo_list:
            if isinstance(self.ubo_list, list):
                for i in range(0, len(self.ubo_list)):
                    element = self.ubo_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ubo_list[i] = element.to_alipay_dict()
            if hasattr(self.ubo_list, 'to_alipay_dict'):
                params['ubo_list'] = self.ubo_list.to_alipay_dict()
            else:
                params['ubo_list'] = self.ubo_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpUboResult()
        if 'crn' in d:
            o.crn = d['crn']
        if 'is_exempt' in d:
            o.is_exempt = d['is_exempt']
        if 'is_normal_status' in d:
            o.is_normal_status = d['is_normal_status']
        if 'is_transp_high' in d:
            o.is_transp_high = d['is_transp_high']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'org_type_oversee' in d:
            o.org_type_oversee = d['org_type_oversee']
        if 'standard_reg_type' in d:
            o.standard_reg_type = d['standard_reg_type']
        if 'ubo_list' in d:
            o.ubo_list = d['ubo_list']
        return o


