#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsEndorseItem import InsEndorseItem


class AlipayInsScenePolicyEndorseApplyModel(object):

    def __init__(self):
        self._endorse_items = None
        self._out_request_no = None
        self._policy_no = None
        self._source = None

    @property
    def endorse_items(self):
        return self._endorse_items

    @endorse_items.setter
    def endorse_items(self, value):
        if isinstance(value, list):
            self._endorse_items = list()
            for i in value:
                if isinstance(i, InsEndorseItem):
                    self._endorse_items.append(i)
                else:
                    self._endorse_items.append(InsEndorseItem.from_alipay_dict(i))
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.endorse_items:
            if isinstance(self.endorse_items, list):
                for i in range(0, len(self.endorse_items)):
                    element = self.endorse_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.endorse_items[i] = element.to_alipay_dict()
            if hasattr(self.endorse_items, 'to_alipay_dict'):
                params['endorse_items'] = self.endorse_items.to_alipay_dict()
            else:
                params['endorse_items'] = self.endorse_items
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsScenePolicyEndorseApplyModel()
        if 'endorse_items' in d:
            o.endorse_items = d['endorse_items']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'source' in d:
            o.source = d['source']
        return o


