#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrePayOperationInfo import PrePayOperationInfo


class InstallmentInfo(object):

    def __init__(self):
        self._install_count = None
        self._operation_list = None

    @property
    def install_count(self):
        return self._install_count

    @install_count.setter
    def install_count(self, value):
        self._install_count = value
    @property
    def operation_list(self):
        return self._operation_list

    @operation_list.setter
    def operation_list(self, value):
        if isinstance(value, PrePayOperationInfo):
            self._operation_list = value
        else:
            self._operation_list = PrePayOperationInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.install_count:
            if hasattr(self.install_count, 'to_alipay_dict'):
                params['install_count'] = self.install_count.to_alipay_dict()
            else:
                params['install_count'] = self.install_count
        if self.operation_list:
            if hasattr(self.operation_list, 'to_alipay_dict'):
                params['operation_list'] = self.operation_list.to_alipay_dict()
            else:
                params['operation_list'] = self.operation_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstallmentInfo()
        if 'install_count' in d:
            o.install_count = d['install_count']
        if 'operation_list' in d:
            o.operation_list = d['operation_list']
        return o


