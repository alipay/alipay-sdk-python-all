#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NotifyFieldExt import NotifyFieldExt
from alipay.aop.api.domain.NotifyTriggerExt import NotifyTriggerExt
from alipay.aop.api.domain.OutputExt import OutputExt


class ExterfaceExt(object):

    def __init__(self):
        self._notify_field_ext = None
        self._notify_trigger_ext = None
        self._output_ext = None

    @property
    def notify_field_ext(self):
        return self._notify_field_ext

    @notify_field_ext.setter
    def notify_field_ext(self, value):
        if isinstance(value, list):
            self._notify_field_ext = list()
            for i in value:
                if isinstance(i, NotifyFieldExt):
                    self._notify_field_ext.append(i)
                else:
                    self._notify_field_ext.append(NotifyFieldExt.from_alipay_dict(i))
    @property
    def notify_trigger_ext(self):
        return self._notify_trigger_ext

    @notify_trigger_ext.setter
    def notify_trigger_ext(self, value):
        if isinstance(value, list):
            self._notify_trigger_ext = list()
            for i in value:
                if isinstance(i, NotifyTriggerExt):
                    self._notify_trigger_ext.append(i)
                else:
                    self._notify_trigger_ext.append(NotifyTriggerExt.from_alipay_dict(i))
    @property
    def output_ext(self):
        return self._output_ext

    @output_ext.setter
    def output_ext(self, value):
        if isinstance(value, list):
            self._output_ext = list()
            for i in value:
                if isinstance(i, OutputExt):
                    self._output_ext.append(i)
                else:
                    self._output_ext.append(OutputExt.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.notify_field_ext:
            if isinstance(self.notify_field_ext, list):
                for i in range(0, len(self.notify_field_ext)):
                    element = self.notify_field_ext[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.notify_field_ext[i] = element.to_alipay_dict()
            if hasattr(self.notify_field_ext, 'to_alipay_dict'):
                params['notify_field_ext'] = self.notify_field_ext.to_alipay_dict()
            else:
                params['notify_field_ext'] = self.notify_field_ext
        if self.notify_trigger_ext:
            if isinstance(self.notify_trigger_ext, list):
                for i in range(0, len(self.notify_trigger_ext)):
                    element = self.notify_trigger_ext[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.notify_trigger_ext[i] = element.to_alipay_dict()
            if hasattr(self.notify_trigger_ext, 'to_alipay_dict'):
                params['notify_trigger_ext'] = self.notify_trigger_ext.to_alipay_dict()
            else:
                params['notify_trigger_ext'] = self.notify_trigger_ext
        if self.output_ext:
            if isinstance(self.output_ext, list):
                for i in range(0, len(self.output_ext)):
                    element = self.output_ext[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.output_ext[i] = element.to_alipay_dict()
            if hasattr(self.output_ext, 'to_alipay_dict'):
                params['output_ext'] = self.output_ext.to_alipay_dict()
            else:
                params['output_ext'] = self.output_ext
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExterfaceExt()
        if 'notify_field_ext' in d:
            o.notify_field_ext = d['notify_field_ext']
        if 'notify_trigger_ext' in d:
            o.notify_trigger_ext = d['notify_trigger_ext']
        if 'output_ext' in d:
            o.output_ext = d['output_ext']
        return o


