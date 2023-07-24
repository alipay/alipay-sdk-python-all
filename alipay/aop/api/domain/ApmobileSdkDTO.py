#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileApiDetailDiffByApiNameDTO import ApmobileApiDetailDiffByApiNameDTO
from alipay.aop.api.domain.ApmobileSdkUsedDTO import ApmobileSdkUsedDTO


class ApmobileSdkDTO(object):

    def __init__(self):
        self._api_used_num = None
        self._sdk_api_used_diff_by_api_list = None
        self._sdk_name = None
        self._sdk_summary = None
        self._sdk_used_list = None

    @property
    def api_used_num(self):
        return self._api_used_num

    @api_used_num.setter
    def api_used_num(self, value):
        self._api_used_num = value
    @property
    def sdk_api_used_diff_by_api_list(self):
        return self._sdk_api_used_diff_by_api_list

    @sdk_api_used_diff_by_api_list.setter
    def sdk_api_used_diff_by_api_list(self, value):
        if isinstance(value, ApmobileApiDetailDiffByApiNameDTO):
            self._sdk_api_used_diff_by_api_list = value
        else:
            self._sdk_api_used_diff_by_api_list = ApmobileApiDetailDiffByApiNameDTO.from_alipay_dict(value)
    @property
    def sdk_name(self):
        return self._sdk_name

    @sdk_name.setter
    def sdk_name(self, value):
        self._sdk_name = value
    @property
    def sdk_summary(self):
        return self._sdk_summary

    @sdk_summary.setter
    def sdk_summary(self, value):
        self._sdk_summary = value
    @property
    def sdk_used_list(self):
        return self._sdk_used_list

    @sdk_used_list.setter
    def sdk_used_list(self, value):
        if isinstance(value, list):
            self._sdk_used_list = list()
            for i in value:
                if isinstance(i, ApmobileSdkUsedDTO):
                    self._sdk_used_list.append(i)
                else:
                    self._sdk_used_list.append(ApmobileSdkUsedDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.api_used_num:
            if hasattr(self.api_used_num, 'to_alipay_dict'):
                params['api_used_num'] = self.api_used_num.to_alipay_dict()
            else:
                params['api_used_num'] = self.api_used_num
        if self.sdk_api_used_diff_by_api_list:
            if hasattr(self.sdk_api_used_diff_by_api_list, 'to_alipay_dict'):
                params['sdk_api_used_diff_by_api_list'] = self.sdk_api_used_diff_by_api_list.to_alipay_dict()
            else:
                params['sdk_api_used_diff_by_api_list'] = self.sdk_api_used_diff_by_api_list
        if self.sdk_name:
            if hasattr(self.sdk_name, 'to_alipay_dict'):
                params['sdk_name'] = self.sdk_name.to_alipay_dict()
            else:
                params['sdk_name'] = self.sdk_name
        if self.sdk_summary:
            if hasattr(self.sdk_summary, 'to_alipay_dict'):
                params['sdk_summary'] = self.sdk_summary.to_alipay_dict()
            else:
                params['sdk_summary'] = self.sdk_summary
        if self.sdk_used_list:
            if isinstance(self.sdk_used_list, list):
                for i in range(0, len(self.sdk_used_list)):
                    element = self.sdk_used_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sdk_used_list[i] = element.to_alipay_dict()
            if hasattr(self.sdk_used_list, 'to_alipay_dict'):
                params['sdk_used_list'] = self.sdk_used_list.to_alipay_dict()
            else:
                params['sdk_used_list'] = self.sdk_used_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileSdkDTO()
        if 'api_used_num' in d:
            o.api_used_num = d['api_used_num']
        if 'sdk_api_used_diff_by_api_list' in d:
            o.sdk_api_used_diff_by_api_list = d['sdk_api_used_diff_by_api_list']
        if 'sdk_name' in d:
            o.sdk_name = d['sdk_name']
        if 'sdk_summary' in d:
            o.sdk_summary = d['sdk_summary']
        if 'sdk_used_list' in d:
            o.sdk_used_list = d['sdk_used_list']
        return o


