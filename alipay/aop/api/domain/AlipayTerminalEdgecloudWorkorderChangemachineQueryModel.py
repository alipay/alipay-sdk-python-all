#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTerminalEdgecloudWorkorderChangemachineQueryModel(object):

    def __init__(self):
        self._device_category_names = None
        self._finish_time_from_date = None
        self._finish_time_to_date = None

    @property
    def device_category_names(self):
        return self._device_category_names

    @device_category_names.setter
    def device_category_names(self, value):
        if isinstance(value, list):
            self._device_category_names = list()
            for i in value:
                self._device_category_names.append(i)
    @property
    def finish_time_from_date(self):
        return self._finish_time_from_date

    @finish_time_from_date.setter
    def finish_time_from_date(self, value):
        self._finish_time_from_date = value
    @property
    def finish_time_to_date(self):
        return self._finish_time_to_date

    @finish_time_to_date.setter
    def finish_time_to_date(self, value):
        self._finish_time_to_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_category_names:
            if isinstance(self.device_category_names, list):
                for i in range(0, len(self.device_category_names)):
                    element = self.device_category_names[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_category_names[i] = element.to_alipay_dict()
            if hasattr(self.device_category_names, 'to_alipay_dict'):
                params['device_category_names'] = self.device_category_names.to_alipay_dict()
            else:
                params['device_category_names'] = self.device_category_names
        if self.finish_time_from_date:
            if hasattr(self.finish_time_from_date, 'to_alipay_dict'):
                params['finish_time_from_date'] = self.finish_time_from_date.to_alipay_dict()
            else:
                params['finish_time_from_date'] = self.finish_time_from_date
        if self.finish_time_to_date:
            if hasattr(self.finish_time_to_date, 'to_alipay_dict'):
                params['finish_time_to_date'] = self.finish_time_to_date.to_alipay_dict()
            else:
                params['finish_time_to_date'] = self.finish_time_to_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTerminalEdgecloudWorkorderChangemachineQueryModel()
        if 'device_category_names' in d:
            o.device_category_names = d['device_category_names']
        if 'finish_time_from_date' in d:
            o.finish_time_from_date = d['finish_time_from_date']
        if 'finish_time_to_date' in d:
            o.finish_time_to_date = d['finish_time_to_date']
        return o


