#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceTagParam import ServiceTagParam


class AlipayCommerceMedicalHealthmanagemServicetagSyncModel(object):

    def __init__(self):
        self._service_tag_list = None

    @property
    def service_tag_list(self):
        return self._service_tag_list

    @service_tag_list.setter
    def service_tag_list(self, value):
        if isinstance(value, list):
            self._service_tag_list = list()
            for i in value:
                if isinstance(i, ServiceTagParam):
                    self._service_tag_list.append(i)
                else:
                    self._service_tag_list.append(ServiceTagParam.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.service_tag_list:
            if isinstance(self.service_tag_list, list):
                for i in range(0, len(self.service_tag_list)):
                    element = self.service_tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_tag_list[i] = element.to_alipay_dict()
            if hasattr(self.service_tag_list, 'to_alipay_dict'):
                params['service_tag_list'] = self.service_tag_list.to_alipay_dict()
            else:
                params['service_tag_list'] = self.service_tag_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHealthmanagemServicetagSyncModel()
        if 'service_tag_list' in d:
            o.service_tag_list = d['service_tag_list']
        return o


