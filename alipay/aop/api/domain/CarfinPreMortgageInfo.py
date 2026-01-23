#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CarfinPreMortgageFile import CarfinPreMortgageFile


class CarfinPreMortgageInfo(object):

    def __init__(self):
        self._approve_file_list = None
        self._channel = None

    @property
    def approve_file_list(self):
        return self._approve_file_list

    @approve_file_list.setter
    def approve_file_list(self, value):
        if isinstance(value, list):
            self._approve_file_list = list()
            for i in value:
                if isinstance(i, CarfinPreMortgageFile):
                    self._approve_file_list.append(i)
                else:
                    self._approve_file_list.append(CarfinPreMortgageFile.from_alipay_dict(i))
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.approve_file_list:
            if isinstance(self.approve_file_list, list):
                for i in range(0, len(self.approve_file_list)):
                    element = self.approve_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.approve_file_list[i] = element.to_alipay_dict()
            if hasattr(self.approve_file_list, 'to_alipay_dict'):
                params['approve_file_list'] = self.approve_file_list.to_alipay_dict()
            else:
                params['approve_file_list'] = self.approve_file_list
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinPreMortgageInfo()
        if 'approve_file_list' in d:
            o.approve_file_list = d['approve_file_list']
        if 'channel' in d:
            o.channel = d['channel']
        return o


