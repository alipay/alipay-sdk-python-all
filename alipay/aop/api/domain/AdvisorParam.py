#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdvisorParam(object):

    def __init__(self):
        self._fulfillment_list = None

    @property
    def fulfillment_list(self):
        return self._fulfillment_list

    @fulfillment_list.setter
    def fulfillment_list(self, value):
        if isinstance(value, list):
            self._fulfillment_list = list()
            for i in value:
                self._fulfillment_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_list:
            if isinstance(self.fulfillment_list, list):
                for i in range(0, len(self.fulfillment_list)):
                    element = self.fulfillment_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fulfillment_list[i] = element.to_alipay_dict()
            if hasattr(self.fulfillment_list, 'to_alipay_dict'):
                params['fulfillment_list'] = self.fulfillment_list.to_alipay_dict()
            else:
                params['fulfillment_list'] = self.fulfillment_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdvisorParam()
        if 'fulfillment_list' in d:
            o.fulfillment_list = d['fulfillment_list']
        return o


