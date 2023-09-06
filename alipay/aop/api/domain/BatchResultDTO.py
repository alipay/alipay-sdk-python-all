#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SingleResultDTO import SingleResultDTO


class BatchResultDTO(object):

    def __init__(self):
        self._all_succeeded = None
        self._result_list = None

    @property
    def all_succeeded(self):
        return self._all_succeeded

    @all_succeeded.setter
    def all_succeeded(self, value):
        self._all_succeeded = value
    @property
    def result_list(self):
        return self._result_list

    @result_list.setter
    def result_list(self, value):
        if isinstance(value, list):
            self._result_list = list()
            for i in value:
                if isinstance(i, SingleResultDTO):
                    self._result_list.append(i)
                else:
                    self._result_list.append(SingleResultDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.all_succeeded:
            if hasattr(self.all_succeeded, 'to_alipay_dict'):
                params['all_succeeded'] = self.all_succeeded.to_alipay_dict()
            else:
                params['all_succeeded'] = self.all_succeeded
        if self.result_list:
            if isinstance(self.result_list, list):
                for i in range(0, len(self.result_list)):
                    element = self.result_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.result_list[i] = element.to_alipay_dict()
            if hasattr(self.result_list, 'to_alipay_dict'):
                params['result_list'] = self.result_list.to_alipay_dict()
            else:
                params['result_list'] = self.result_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BatchResultDTO()
        if 'all_succeeded' in d:
            o.all_succeeded = d['all_succeeded']
        if 'result_list' in d:
            o.result_list = d['result_list']
        return o


