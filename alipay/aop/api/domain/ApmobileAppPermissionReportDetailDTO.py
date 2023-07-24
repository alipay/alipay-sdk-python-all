#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileDetectDetailDTO import ApmobileDetectDetailDTO


class ApmobileAppPermissionReportDetailDTO(object):

    def __init__(self):
        self._detect_detail_list = None

    @property
    def detect_detail_list(self):
        return self._detect_detail_list

    @detect_detail_list.setter
    def detect_detail_list(self, value):
        if isinstance(value, list):
            self._detect_detail_list = list()
            for i in value:
                if isinstance(i, ApmobileDetectDetailDTO):
                    self._detect_detail_list.append(i)
                else:
                    self._detect_detail_list.append(ApmobileDetectDetailDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.detect_detail_list:
            if isinstance(self.detect_detail_list, list):
                for i in range(0, len(self.detect_detail_list)):
                    element = self.detect_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detect_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.detect_detail_list, 'to_alipay_dict'):
                params['detect_detail_list'] = self.detect_detail_list.to_alipay_dict()
            else:
                params['detect_detail_list'] = self.detect_detail_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileAppPermissionReportDetailDTO()
        if 'detect_detail_list' in d:
            o.detect_detail_list = d['detect_detail_list']
        return o


