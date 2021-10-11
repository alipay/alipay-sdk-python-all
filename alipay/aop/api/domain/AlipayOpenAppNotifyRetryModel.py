#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppNotifyRetryModel(object):

    def __init__(self):
        self._notify_id_list = None

    @property
    def notify_id_list(self):
        return self._notify_id_list

    @notify_id_list.setter
    def notify_id_list(self, value):
        if isinstance(value, list):
            self._notify_id_list = list()
            for i in value:
                self._notify_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.notify_id_list:
            if isinstance(self.notify_id_list, list):
                for i in range(0, len(self.notify_id_list)):
                    element = self.notify_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.notify_id_list[i] = element.to_alipay_dict()
            if hasattr(self.notify_id_list, 'to_alipay_dict'):
                params['notify_id_list'] = self.notify_id_list.to_alipay_dict()
            else:
                params['notify_id_list'] = self.notify_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppNotifyRetryModel()
        if 'notify_id_list' in d:
            o.notify_id_list = d['notify_id_list']
        return o


