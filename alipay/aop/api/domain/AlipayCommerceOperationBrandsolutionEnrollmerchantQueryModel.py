#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationBrandsolutionEnrollmerchantQueryModel(object):

    def __init__(self):
        self._activity_id = None
        self._pids = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def pids(self):
        return self._pids

    @pids.setter
    def pids(self, value):
        if isinstance(value, list):
            self._pids = list()
            for i in value:
                self._pids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.pids:
            if isinstance(self.pids, list):
                for i in range(0, len(self.pids)):
                    element = self.pids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pids[i] = element.to_alipay_dict()
            if hasattr(self.pids, 'to_alipay_dict'):
                params['pids'] = self.pids.to_alipay_dict()
            else:
                params['pids'] = self.pids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationBrandsolutionEnrollmerchantQueryModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'pids' in d:
            o.pids = d['pids']
        return o


