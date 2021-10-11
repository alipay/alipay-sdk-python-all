#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GbReleaseRequest import GbReleaseRequest


class AlipayBossFncAntbudgetGroupbudgetRefundModel(object):

    def __init__(self):
        self._batch_id = None
        self._group_budget_release_request_list = None
        self._ns = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def group_budget_release_request_list(self):
        return self._group_budget_release_request_list

    @group_budget_release_request_list.setter
    def group_budget_release_request_list(self, value):
        if isinstance(value, list):
            self._group_budget_release_request_list = list()
            for i in value:
                if isinstance(i, GbReleaseRequest):
                    self._group_budget_release_request_list.append(i)
                else:
                    self._group_budget_release_request_list.append(GbReleaseRequest.from_alipay_dict(i))
    @property
    def ns(self):
        return self._ns

    @ns.setter
    def ns(self, value):
        self._ns = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.group_budget_release_request_list:
            if isinstance(self.group_budget_release_request_list, list):
                for i in range(0, len(self.group_budget_release_request_list)):
                    element = self.group_budget_release_request_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_budget_release_request_list[i] = element.to_alipay_dict()
            if hasattr(self.group_budget_release_request_list, 'to_alipay_dict'):
                params['group_budget_release_request_list'] = self.group_budget_release_request_list.to_alipay_dict()
            else:
                params['group_budget_release_request_list'] = self.group_budget_release_request_list
        if self.ns:
            if hasattr(self.ns, 'to_alipay_dict'):
                params['ns'] = self.ns.to_alipay_dict()
            else:
                params['ns'] = self.ns
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncAntbudgetGroupbudgetRefundModel()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'group_budget_release_request_list' in d:
            o.group_budget_release_request_list = d['group_budget_release_request_list']
        if 'ns' in d:
            o.ns = d['ns']
        return o


