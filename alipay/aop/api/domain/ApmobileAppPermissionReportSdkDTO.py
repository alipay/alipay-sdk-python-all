#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileSdkDTO import ApmobileSdkDTO


class ApmobileAppPermissionReportSdkDTO(object):

    def __init__(self):
        self._sdk_list = None
        self._sdk_sum = None
        self._sdk_used = None

    @property
    def sdk_list(self):
        return self._sdk_list

    @sdk_list.setter
    def sdk_list(self, value):
        if isinstance(value, list):
            self._sdk_list = list()
            for i in value:
                if isinstance(i, ApmobileSdkDTO):
                    self._sdk_list.append(i)
                else:
                    self._sdk_list.append(ApmobileSdkDTO.from_alipay_dict(i))
    @property
    def sdk_sum(self):
        return self._sdk_sum

    @sdk_sum.setter
    def sdk_sum(self, value):
        self._sdk_sum = value
    @property
    def sdk_used(self):
        return self._sdk_used

    @sdk_used.setter
    def sdk_used(self, value):
        self._sdk_used = value


    def to_alipay_dict(self):
        params = dict()
        if self.sdk_list:
            if isinstance(self.sdk_list, list):
                for i in range(0, len(self.sdk_list)):
                    element = self.sdk_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sdk_list[i] = element.to_alipay_dict()
            if hasattr(self.sdk_list, 'to_alipay_dict'):
                params['sdk_list'] = self.sdk_list.to_alipay_dict()
            else:
                params['sdk_list'] = self.sdk_list
        if self.sdk_sum:
            if hasattr(self.sdk_sum, 'to_alipay_dict'):
                params['sdk_sum'] = self.sdk_sum.to_alipay_dict()
            else:
                params['sdk_sum'] = self.sdk_sum
        if self.sdk_used:
            if hasattr(self.sdk_used, 'to_alipay_dict'):
                params['sdk_used'] = self.sdk_used.to_alipay_dict()
            else:
                params['sdk_used'] = self.sdk_used
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileAppPermissionReportSdkDTO()
        if 'sdk_list' in d:
            o.sdk_list = d['sdk_list']
        if 'sdk_sum' in d:
            o.sdk_sum = d['sdk_sum']
        if 'sdk_used' in d:
            o.sdk_used = d['sdk_used']
        return o


