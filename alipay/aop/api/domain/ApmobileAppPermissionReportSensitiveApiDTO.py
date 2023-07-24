#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileUseApiDTO import ApmobileUseApiDTO
from alipay.aop.api.domain.ApmobileAppApiUsedOverviewDTO import ApmobileAppApiUsedOverviewDTO


class ApmobileAppPermissionReportSensitiveApiDTO(object):

    def __init__(self):
        self._api_used_list = None
        self._api_used_overview_list = None
        self._api_used_total = None

    @property
    def api_used_list(self):
        return self._api_used_list

    @api_used_list.setter
    def api_used_list(self, value):
        if isinstance(value, list):
            self._api_used_list = list()
            for i in value:
                if isinstance(i, ApmobileUseApiDTO):
                    self._api_used_list.append(i)
                else:
                    self._api_used_list.append(ApmobileUseApiDTO.from_alipay_dict(i))
    @property
    def api_used_overview_list(self):
        return self._api_used_overview_list

    @api_used_overview_list.setter
    def api_used_overview_list(self, value):
        if isinstance(value, list):
            self._api_used_overview_list = list()
            for i in value:
                if isinstance(i, ApmobileAppApiUsedOverviewDTO):
                    self._api_used_overview_list.append(i)
                else:
                    self._api_used_overview_list.append(ApmobileAppApiUsedOverviewDTO.from_alipay_dict(i))
    @property
    def api_used_total(self):
        return self._api_used_total

    @api_used_total.setter
    def api_used_total(self, value):
        self._api_used_total = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_used_list:
            if isinstance(self.api_used_list, list):
                for i in range(0, len(self.api_used_list)):
                    element = self.api_used_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.api_used_list[i] = element.to_alipay_dict()
            if hasattr(self.api_used_list, 'to_alipay_dict'):
                params['api_used_list'] = self.api_used_list.to_alipay_dict()
            else:
                params['api_used_list'] = self.api_used_list
        if self.api_used_overview_list:
            if isinstance(self.api_used_overview_list, list):
                for i in range(0, len(self.api_used_overview_list)):
                    element = self.api_used_overview_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.api_used_overview_list[i] = element.to_alipay_dict()
            if hasattr(self.api_used_overview_list, 'to_alipay_dict'):
                params['api_used_overview_list'] = self.api_used_overview_list.to_alipay_dict()
            else:
                params['api_used_overview_list'] = self.api_used_overview_list
        if self.api_used_total:
            if hasattr(self.api_used_total, 'to_alipay_dict'):
                params['api_used_total'] = self.api_used_total.to_alipay_dict()
            else:
                params['api_used_total'] = self.api_used_total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileAppPermissionReportSensitiveApiDTO()
        if 'api_used_list' in d:
            o.api_used_list = d['api_used_list']
        if 'api_used_overview_list' in d:
            o.api_used_overview_list = d['api_used_overview_list']
        if 'api_used_total' in d:
            o.api_used_total = d['api_used_total']
        return o


