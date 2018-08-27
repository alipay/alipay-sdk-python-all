#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpElement import EpElement


class EpInfo(object):

    def __init__(self):
        self._ep_element_list = None

    @property
    def ep_element_list(self):
        return self._ep_element_list

    @ep_element_list.setter
    def ep_element_list(self, value):
        if isinstance(value, list):
            self._ep_element_list = list()
            for i in value:
                if isinstance(i, EpElement):
                    self._ep_element_list.append(i)
                else:
                    self._ep_element_list.append(EpElement.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ep_element_list:
            if isinstance(self.ep_element_list, list):
                for i in range(0, len(self.ep_element_list)):
                    element = self.ep_element_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ep_element_list[i] = element.to_alipay_dict()
            if hasattr(self.ep_element_list, 'to_alipay_dict'):
                params['ep_element_list'] = self.ep_element_list.to_alipay_dict()
            else:
                params['ep_element_list'] = self.ep_element_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpInfo()
        if 'ep_element_list' in d:
            o.ep_element_list = d['ep_element_list']
        return o


