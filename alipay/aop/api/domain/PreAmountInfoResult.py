#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PreAmountClauseResult import PreAmountClauseResult


class PreAmountInfoResult(object):

    def __init__(self):
        self._pre_amount_list = None
        self._total_pre_mount = None

    @property
    def pre_amount_list(self):
        return self._pre_amount_list

    @pre_amount_list.setter
    def pre_amount_list(self, value):
        if isinstance(value, list):
            self._pre_amount_list = list()
            for i in value:
                if isinstance(i, PreAmountClauseResult):
                    self._pre_amount_list.append(i)
                else:
                    self._pre_amount_list.append(PreAmountClauseResult.from_alipay_dict(i))
    @property
    def total_pre_mount(self):
        return self._total_pre_mount

    @total_pre_mount.setter
    def total_pre_mount(self, value):
        self._total_pre_mount = value


    def to_alipay_dict(self):
        params = dict()
        if self.pre_amount_list:
            if isinstance(self.pre_amount_list, list):
                for i in range(0, len(self.pre_amount_list)):
                    element = self.pre_amount_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pre_amount_list[i] = element.to_alipay_dict()
            if hasattr(self.pre_amount_list, 'to_alipay_dict'):
                params['pre_amount_list'] = self.pre_amount_list.to_alipay_dict()
            else:
                params['pre_amount_list'] = self.pre_amount_list
        if self.total_pre_mount:
            if hasattr(self.total_pre_mount, 'to_alipay_dict'):
                params['total_pre_mount'] = self.total_pre_mount.to_alipay_dict()
            else:
                params['total_pre_mount'] = self.total_pre_mount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PreAmountInfoResult()
        if 'pre_amount_list' in d:
            o.pre_amount_list = d['pre_amount_list']
        if 'total_pre_mount' in d:
            o.total_pre_mount = d['total_pre_mount']
        return o


