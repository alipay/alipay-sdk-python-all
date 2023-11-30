#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DelOauthDetail import DelOauthDetail


class DelOauthDetailResult(object):

    def __init__(self):
        self._details = None

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        if isinstance(value, list):
            self._details = list()
            for i in value:
                if isinstance(i, DelOauthDetail):
                    self._details.append(i)
                else:
                    self._details.append(DelOauthDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.details:
            if isinstance(self.details, list):
                for i in range(0, len(self.details)):
                    element = self.details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.details[i] = element.to_alipay_dict()
            if hasattr(self.details, 'to_alipay_dict'):
                params['details'] = self.details.to_alipay_dict()
            else:
                params['details'] = self.details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DelOauthDetailResult()
        if 'details' in d:
            o.details = d['details']
        return o


