#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityDeliveryExtInfo(object):

    def __init__(self):
        self._auto_delivery = None
        self._channel_list = None

    @property
    def auto_delivery(self):
        return self._auto_delivery

    @auto_delivery.setter
    def auto_delivery(self, value):
        self._auto_delivery = value
    @property
    def channel_list(self):
        return self._channel_list

    @channel_list.setter
    def channel_list(self, value):
        if isinstance(value, list):
            self._channel_list = list()
            for i in value:
                self._channel_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.auto_delivery:
            if hasattr(self.auto_delivery, 'to_alipay_dict'):
                params['auto_delivery'] = self.auto_delivery.to_alipay_dict()
            else:
                params['auto_delivery'] = self.auto_delivery
        if self.channel_list:
            if isinstance(self.channel_list, list):
                for i in range(0, len(self.channel_list)):
                    element = self.channel_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channel_list[i] = element.to_alipay_dict()
            if hasattr(self.channel_list, 'to_alipay_dict'):
                params['channel_list'] = self.channel_list.to_alipay_dict()
            else:
                params['channel_list'] = self.channel_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityDeliveryExtInfo()
        if 'auto_delivery' in d:
            o.auto_delivery = d['auto_delivery']
        if 'channel_list' in d:
            o.channel_list = d['channel_list']
        return o


