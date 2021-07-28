#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizExtParams(object):

    def __init__(self):
        self._groupon_partners = None

    @property
    def groupon_partners(self):
        return self._groupon_partners

    @groupon_partners.setter
    def groupon_partners(self, value):
        if isinstance(value, list):
            self._groupon_partners = list()
            for i in value:
                self._groupon_partners.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.groupon_partners:
            if isinstance(self.groupon_partners, list):
                for i in range(0, len(self.groupon_partners)):
                    element = self.groupon_partners[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.groupon_partners[i] = element.to_alipay_dict()
            if hasattr(self.groupon_partners, 'to_alipay_dict'):
                params['groupon_partners'] = self.groupon_partners.to_alipay_dict()
            else:
                params['groupon_partners'] = self.groupon_partners
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizExtParams()
        if 'groupon_partners' in d:
            o.groupon_partners = d['groupon_partners']
        return o


