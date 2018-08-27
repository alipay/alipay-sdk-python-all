#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertPreserveCommissionClause(object):

    def __init__(self):
        self._claimer_id_type = None
        self._claimers = None

    @property
    def claimer_id_type(self):
        return self._claimer_id_type

    @claimer_id_type.setter
    def claimer_id_type(self, value):
        self._claimer_id_type = value
    @property
    def claimers(self):
        return self._claimers

    @claimers.setter
    def claimers(self, value):
        if isinstance(value, list):
            self._claimers = list()
            for i in value:
                self._claimers.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.claimer_id_type:
            if hasattr(self.claimer_id_type, 'to_alipay_dict'):
                params['claimer_id_type'] = self.claimer_id_type.to_alipay_dict()
            else:
                params['claimer_id_type'] = self.claimer_id_type
        if self.claimers:
            if isinstance(self.claimers, list):
                for i in range(0, len(self.claimers)):
                    element = self.claimers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.claimers[i] = element.to_alipay_dict()
            if hasattr(self.claimers, 'to_alipay_dict'):
                params['claimers'] = self.claimers.to_alipay_dict()
            else:
                params['claimers'] = self.claimers
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertPreserveCommissionClause()
        if 'claimer_id_type' in d:
            o.claimer_id_type = d['claimer_id_type']
        if 'claimers' in d:
            o.claimers = d['claimers']
        return o


