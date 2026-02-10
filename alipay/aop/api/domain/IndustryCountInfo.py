#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpIndicatorIndustryCountInfo import EpIndicatorIndustryCountInfo
from alipay.aop.api.domain.EpIndicatorIndustryCountInfo import EpIndicatorIndustryCountInfo
from alipay.aop.api.domain.EpIndicatorIndustryCountInfo import EpIndicatorIndustryCountInfo


class IndustryCountInfo(object):

    def __init__(self):
        self._member_industry = None
        self._nephew_industry = None
        self._unrelated_industry = None

    @property
    def member_industry(self):
        return self._member_industry

    @member_industry.setter
    def member_industry(self, value):
        if isinstance(value, list):
            self._member_industry = list()
            for i in value:
                if isinstance(i, EpIndicatorIndustryCountInfo):
                    self._member_industry.append(i)
                else:
                    self._member_industry.append(EpIndicatorIndustryCountInfo.from_alipay_dict(i))
    @property
    def nephew_industry(self):
        return self._nephew_industry

    @nephew_industry.setter
    def nephew_industry(self, value):
        if isinstance(value, list):
            self._nephew_industry = list()
            for i in value:
                if isinstance(i, EpIndicatorIndustryCountInfo):
                    self._nephew_industry.append(i)
                else:
                    self._nephew_industry.append(EpIndicatorIndustryCountInfo.from_alipay_dict(i))
    @property
    def unrelated_industry(self):
        return self._unrelated_industry

    @unrelated_industry.setter
    def unrelated_industry(self, value):
        if isinstance(value, list):
            self._unrelated_industry = list()
            for i in value:
                if isinstance(i, EpIndicatorIndustryCountInfo):
                    self._unrelated_industry.append(i)
                else:
                    self._unrelated_industry.append(EpIndicatorIndustryCountInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.member_industry:
            if isinstance(self.member_industry, list):
                for i in range(0, len(self.member_industry)):
                    element = self.member_industry[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.member_industry[i] = element.to_alipay_dict()
            if hasattr(self.member_industry, 'to_alipay_dict'):
                params['member_industry'] = self.member_industry.to_alipay_dict()
            else:
                params['member_industry'] = self.member_industry
        if self.nephew_industry:
            if isinstance(self.nephew_industry, list):
                for i in range(0, len(self.nephew_industry)):
                    element = self.nephew_industry[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.nephew_industry[i] = element.to_alipay_dict()
            if hasattr(self.nephew_industry, 'to_alipay_dict'):
                params['nephew_industry'] = self.nephew_industry.to_alipay_dict()
            else:
                params['nephew_industry'] = self.nephew_industry
        if self.unrelated_industry:
            if isinstance(self.unrelated_industry, list):
                for i in range(0, len(self.unrelated_industry)):
                    element = self.unrelated_industry[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.unrelated_industry[i] = element.to_alipay_dict()
            if hasattr(self.unrelated_industry, 'to_alipay_dict'):
                params['unrelated_industry'] = self.unrelated_industry.to_alipay_dict()
            else:
                params['unrelated_industry'] = self.unrelated_industry
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryCountInfo()
        if 'member_industry' in d:
            o.member_industry = d['member_industry']
        if 'nephew_industry' in d:
            o.nephew_industry = d['nephew_industry']
        if 'unrelated_industry' in d:
            o.unrelated_industry = d['unrelated_industry']
        return o


