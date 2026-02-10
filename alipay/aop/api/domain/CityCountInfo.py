#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpIndicatorCityCountInfo import EpIndicatorCityCountInfo
from alipay.aop.api.domain.EpIndicatorCityCountInfo import EpIndicatorCityCountInfo
from alipay.aop.api.domain.EpIndicatorCityCountInfo import EpIndicatorCityCountInfo


class CityCountInfo(object):

    def __init__(self):
        self._member_province = None
        self._nephew_province = None
        self._unrelated_province = None

    @property
    def member_province(self):
        return self._member_province

    @member_province.setter
    def member_province(self, value):
        if isinstance(value, list):
            self._member_province = list()
            for i in value:
                if isinstance(i, EpIndicatorCityCountInfo):
                    self._member_province.append(i)
                else:
                    self._member_province.append(EpIndicatorCityCountInfo.from_alipay_dict(i))
    @property
    def nephew_province(self):
        return self._nephew_province

    @nephew_province.setter
    def nephew_province(self, value):
        if isinstance(value, list):
            self._nephew_province = list()
            for i in value:
                if isinstance(i, EpIndicatorCityCountInfo):
                    self._nephew_province.append(i)
                else:
                    self._nephew_province.append(EpIndicatorCityCountInfo.from_alipay_dict(i))
    @property
    def unrelated_province(self):
        return self._unrelated_province

    @unrelated_province.setter
    def unrelated_province(self, value):
        if isinstance(value, list):
            self._unrelated_province = list()
            for i in value:
                if isinstance(i, EpIndicatorCityCountInfo):
                    self._unrelated_province.append(i)
                else:
                    self._unrelated_province.append(EpIndicatorCityCountInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.member_province:
            if isinstance(self.member_province, list):
                for i in range(0, len(self.member_province)):
                    element = self.member_province[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.member_province[i] = element.to_alipay_dict()
            if hasattr(self.member_province, 'to_alipay_dict'):
                params['member_province'] = self.member_province.to_alipay_dict()
            else:
                params['member_province'] = self.member_province
        if self.nephew_province:
            if isinstance(self.nephew_province, list):
                for i in range(0, len(self.nephew_province)):
                    element = self.nephew_province[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.nephew_province[i] = element.to_alipay_dict()
            if hasattr(self.nephew_province, 'to_alipay_dict'):
                params['nephew_province'] = self.nephew_province.to_alipay_dict()
            else:
                params['nephew_province'] = self.nephew_province
        if self.unrelated_province:
            if isinstance(self.unrelated_province, list):
                for i in range(0, len(self.unrelated_province)):
                    element = self.unrelated_province[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.unrelated_province[i] = element.to_alipay_dict()
            if hasattr(self.unrelated_province, 'to_alipay_dict'):
                params['unrelated_province'] = self.unrelated_province.to_alipay_dict()
            else:
                params['unrelated_province'] = self.unrelated_province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CityCountInfo()
        if 'member_province' in d:
            o.member_province = d['member_province']
        if 'nephew_province' in d:
            o.nephew_province = d['nephew_province']
        if 'unrelated_province' in d:
            o.unrelated_province = d['unrelated_province']
        return o


