#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FastAuditTaskInfoVO import FastAuditTaskInfoVO


class RentInfoVO(object):

    def __init__(self):
        self._fast_audit_task_info_list = None
        self._fast_audit_url = None
        self._secure_key = None

    @property
    def fast_audit_task_info_list(self):
        return self._fast_audit_task_info_list

    @fast_audit_task_info_list.setter
    def fast_audit_task_info_list(self, value):
        if isinstance(value, list):
            self._fast_audit_task_info_list = list()
            for i in value:
                if isinstance(i, FastAuditTaskInfoVO):
                    self._fast_audit_task_info_list.append(i)
                else:
                    self._fast_audit_task_info_list.append(FastAuditTaskInfoVO.from_alipay_dict(i))
    @property
    def fast_audit_url(self):
        return self._fast_audit_url

    @fast_audit_url.setter
    def fast_audit_url(self, value):
        self._fast_audit_url = value
    @property
    def secure_key(self):
        return self._secure_key

    @secure_key.setter
    def secure_key(self, value):
        self._secure_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.fast_audit_task_info_list:
            if isinstance(self.fast_audit_task_info_list, list):
                for i in range(0, len(self.fast_audit_task_info_list)):
                    element = self.fast_audit_task_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fast_audit_task_info_list[i] = element.to_alipay_dict()
            if hasattr(self.fast_audit_task_info_list, 'to_alipay_dict'):
                params['fast_audit_task_info_list'] = self.fast_audit_task_info_list.to_alipay_dict()
            else:
                params['fast_audit_task_info_list'] = self.fast_audit_task_info_list
        if self.fast_audit_url:
            if hasattr(self.fast_audit_url, 'to_alipay_dict'):
                params['fast_audit_url'] = self.fast_audit_url.to_alipay_dict()
            else:
                params['fast_audit_url'] = self.fast_audit_url
        if self.secure_key:
            if hasattr(self.secure_key, 'to_alipay_dict'):
                params['secure_key'] = self.secure_key.to_alipay_dict()
            else:
                params['secure_key'] = self.secure_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentInfoVO()
        if 'fast_audit_task_info_list' in d:
            o.fast_audit_task_info_list = d['fast_audit_task_info_list']
        if 'fast_audit_url' in d:
            o.fast_audit_url = d['fast_audit_url']
        if 'secure_key' in d:
            o.secure_key = d['secure_key']
        return o


