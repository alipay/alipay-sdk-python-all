#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ErrorDishEntity import ErrorDishEntity
from alipay.aop.api.domain.ErrorDishEntity import ErrorDishEntity


class ErrorDishStallEntity(object):

    def __init__(self):
        self._no_set_stall = None
        self._repeat_set_stall = None

    @property
    def no_set_stall(self):
        return self._no_set_stall

    @no_set_stall.setter
    def no_set_stall(self, value):
        if isinstance(value, list):
            self._no_set_stall = list()
            for i in value:
                if isinstance(i, ErrorDishEntity):
                    self._no_set_stall.append(i)
                else:
                    self._no_set_stall.append(ErrorDishEntity.from_alipay_dict(i))
    @property
    def repeat_set_stall(self):
        return self._repeat_set_stall

    @repeat_set_stall.setter
    def repeat_set_stall(self, value):
        if isinstance(value, list):
            self._repeat_set_stall = list()
            for i in value:
                if isinstance(i, ErrorDishEntity):
                    self._repeat_set_stall.append(i)
                else:
                    self._repeat_set_stall.append(ErrorDishEntity.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.no_set_stall:
            if isinstance(self.no_set_stall, list):
                for i in range(0, len(self.no_set_stall)):
                    element = self.no_set_stall[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.no_set_stall[i] = element.to_alipay_dict()
            if hasattr(self.no_set_stall, 'to_alipay_dict'):
                params['no_set_stall'] = self.no_set_stall.to_alipay_dict()
            else:
                params['no_set_stall'] = self.no_set_stall
        if self.repeat_set_stall:
            if isinstance(self.repeat_set_stall, list):
                for i in range(0, len(self.repeat_set_stall)):
                    element = self.repeat_set_stall[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.repeat_set_stall[i] = element.to_alipay_dict()
            if hasattr(self.repeat_set_stall, 'to_alipay_dict'):
                params['repeat_set_stall'] = self.repeat_set_stall.to_alipay_dict()
            else:
                params['repeat_set_stall'] = self.repeat_set_stall
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ErrorDishStallEntity()
        if 'no_set_stall' in d:
            o.no_set_stall = d['no_set_stall']
        if 'repeat_set_stall' in d:
            o.repeat_set_stall = d['repeat_set_stall']
        return o


