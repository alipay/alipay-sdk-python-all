#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileAppPermissionUsedDTO import ApmobileAppPermissionUsedDTO
from alipay.aop.api.domain.ApmobileAppPermissionUsedOverviewDTO import ApmobileAppPermissionUsedOverviewDTO


class ApmobileAppPermissionReportSensitiveDTO(object):

    def __init__(self):
        self._permission_apply = None
        self._permission_over_apply = None
        self._permission_over_used = None
        self._permission_sum = None
        self._permission_used = None
        self._permission_used_list = None
        self._permission_used_overview_list = None

    @property
    def permission_apply(self):
        return self._permission_apply

    @permission_apply.setter
    def permission_apply(self, value):
        self._permission_apply = value
    @property
    def permission_over_apply(self):
        return self._permission_over_apply

    @permission_over_apply.setter
    def permission_over_apply(self, value):
        self._permission_over_apply = value
    @property
    def permission_over_used(self):
        return self._permission_over_used

    @permission_over_used.setter
    def permission_over_used(self, value):
        self._permission_over_used = value
    @property
    def permission_sum(self):
        return self._permission_sum

    @permission_sum.setter
    def permission_sum(self, value):
        self._permission_sum = value
    @property
    def permission_used(self):
        return self._permission_used

    @permission_used.setter
    def permission_used(self, value):
        self._permission_used = value
    @property
    def permission_used_list(self):
        return self._permission_used_list

    @permission_used_list.setter
    def permission_used_list(self, value):
        if isinstance(value, list):
            self._permission_used_list = list()
            for i in value:
                if isinstance(i, ApmobileAppPermissionUsedDTO):
                    self._permission_used_list.append(i)
                else:
                    self._permission_used_list.append(ApmobileAppPermissionUsedDTO.from_alipay_dict(i))
    @property
    def permission_used_overview_list(self):
        return self._permission_used_overview_list

    @permission_used_overview_list.setter
    def permission_used_overview_list(self, value):
        if isinstance(value, list):
            self._permission_used_overview_list = list()
            for i in value:
                if isinstance(i, ApmobileAppPermissionUsedOverviewDTO):
                    self._permission_used_overview_list.append(i)
                else:
                    self._permission_used_overview_list.append(ApmobileAppPermissionUsedOverviewDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.permission_apply:
            if hasattr(self.permission_apply, 'to_alipay_dict'):
                params['permission_apply'] = self.permission_apply.to_alipay_dict()
            else:
                params['permission_apply'] = self.permission_apply
        if self.permission_over_apply:
            if hasattr(self.permission_over_apply, 'to_alipay_dict'):
                params['permission_over_apply'] = self.permission_over_apply.to_alipay_dict()
            else:
                params['permission_over_apply'] = self.permission_over_apply
        if self.permission_over_used:
            if hasattr(self.permission_over_used, 'to_alipay_dict'):
                params['permission_over_used'] = self.permission_over_used.to_alipay_dict()
            else:
                params['permission_over_used'] = self.permission_over_used
        if self.permission_sum:
            if hasattr(self.permission_sum, 'to_alipay_dict'):
                params['permission_sum'] = self.permission_sum.to_alipay_dict()
            else:
                params['permission_sum'] = self.permission_sum
        if self.permission_used:
            if hasattr(self.permission_used, 'to_alipay_dict'):
                params['permission_used'] = self.permission_used.to_alipay_dict()
            else:
                params['permission_used'] = self.permission_used
        if self.permission_used_list:
            if isinstance(self.permission_used_list, list):
                for i in range(0, len(self.permission_used_list)):
                    element = self.permission_used_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.permission_used_list[i] = element.to_alipay_dict()
            if hasattr(self.permission_used_list, 'to_alipay_dict'):
                params['permission_used_list'] = self.permission_used_list.to_alipay_dict()
            else:
                params['permission_used_list'] = self.permission_used_list
        if self.permission_used_overview_list:
            if isinstance(self.permission_used_overview_list, list):
                for i in range(0, len(self.permission_used_overview_list)):
                    element = self.permission_used_overview_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.permission_used_overview_list[i] = element.to_alipay_dict()
            if hasattr(self.permission_used_overview_list, 'to_alipay_dict'):
                params['permission_used_overview_list'] = self.permission_used_overview_list.to_alipay_dict()
            else:
                params['permission_used_overview_list'] = self.permission_used_overview_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileAppPermissionReportSensitiveDTO()
        if 'permission_apply' in d:
            o.permission_apply = d['permission_apply']
        if 'permission_over_apply' in d:
            o.permission_over_apply = d['permission_over_apply']
        if 'permission_over_used' in d:
            o.permission_over_used = d['permission_over_used']
        if 'permission_sum' in d:
            o.permission_sum = d['permission_sum']
        if 'permission_used' in d:
            o.permission_used = d['permission_used']
        if 'permission_used_list' in d:
            o.permission_used_list = d['permission_used_list']
        if 'permission_used_overview_list' in d:
            o.permission_used_overview_list = d['permission_used_overview_list']
        return o


