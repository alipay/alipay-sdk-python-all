#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CarfinMortgageReceivedFile import CarfinMortgageReceivedFile


class XingheLendassistCarfinCarproxymaterialNotifyModel(object):

    def __init__(self):
        self._file_list = None
        self._mortgage_no = None
        self._notify_scene = None
        self._out_proxy_no = None

    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                if isinstance(i, CarfinMortgageReceivedFile):
                    self._file_list.append(i)
                else:
                    self._file_list.append(CarfinMortgageReceivedFile.from_alipay_dict(i))
    @property
    def mortgage_no(self):
        return self._mortgage_no

    @mortgage_no.setter
    def mortgage_no(self, value):
        self._mortgage_no = value
    @property
    def notify_scene(self):
        return self._notify_scene

    @notify_scene.setter
    def notify_scene(self, value):
        self._notify_scene = value
    @property
    def out_proxy_no(self):
        return self._out_proxy_no

    @out_proxy_no.setter
    def out_proxy_no(self, value):
        self._out_proxy_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_list:
            if isinstance(self.file_list, list):
                for i in range(0, len(self.file_list)):
                    element = self.file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_list[i] = element.to_alipay_dict()
            if hasattr(self.file_list, 'to_alipay_dict'):
                params['file_list'] = self.file_list.to_alipay_dict()
            else:
                params['file_list'] = self.file_list
        if self.mortgage_no:
            if hasattr(self.mortgage_no, 'to_alipay_dict'):
                params['mortgage_no'] = self.mortgage_no.to_alipay_dict()
            else:
                params['mortgage_no'] = self.mortgage_no
        if self.notify_scene:
            if hasattr(self.notify_scene, 'to_alipay_dict'):
                params['notify_scene'] = self.notify_scene.to_alipay_dict()
            else:
                params['notify_scene'] = self.notify_scene
        if self.out_proxy_no:
            if hasattr(self.out_proxy_no, 'to_alipay_dict'):
                params['out_proxy_no'] = self.out_proxy_no.to_alipay_dict()
            else:
                params['out_proxy_no'] = self.out_proxy_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinCarproxymaterialNotifyModel()
        if 'file_list' in d:
            o.file_list = d['file_list']
        if 'mortgage_no' in d:
            o.mortgage_no = d['mortgage_no']
        if 'notify_scene' in d:
            o.notify_scene = d['notify_scene']
        if 'out_proxy_no' in d:
            o.out_proxy_no = d['out_proxy_no']
        return o


