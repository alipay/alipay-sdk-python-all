#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CompanyOverviewLineInfo import CompanyOverviewLineInfo
from alipay.aop.api.domain.CompanyOverviewLineInfo import CompanyOverviewLineInfo
from alipay.aop.api.domain.CompanyOverviewLineInfo import CompanyOverviewLineInfo
from alipay.aop.api.domain.CompanyOverviewLineInfo import CompanyOverviewLineInfo
from alipay.aop.api.domain.CompanyOverviewLineInfo import CompanyOverviewLineInfo
from alipay.aop.api.domain.CompanyOverviewLineInfo import CompanyOverviewLineInfo


class CompanyOverviewInfo(object):

    def __init__(self):
        self._assets = None
        self._background = None
        self._evaluate = None
        self._financing = None
        self._management = None
        self._risk = None

    @property
    def assets(self):
        return self._assets

    @assets.setter
    def assets(self, value):
        if isinstance(value, list):
            self._assets = list()
            for i in value:
                if isinstance(i, CompanyOverviewLineInfo):
                    self._assets.append(i)
                else:
                    self._assets.append(CompanyOverviewLineInfo.from_alipay_dict(i))
    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        if isinstance(value, list):
            self._background = list()
            for i in value:
                if isinstance(i, CompanyOverviewLineInfo):
                    self._background.append(i)
                else:
                    self._background.append(CompanyOverviewLineInfo.from_alipay_dict(i))
    @property
    def evaluate(self):
        return self._evaluate

    @evaluate.setter
    def evaluate(self, value):
        if isinstance(value, list):
            self._evaluate = list()
            for i in value:
                if isinstance(i, CompanyOverviewLineInfo):
                    self._evaluate.append(i)
                else:
                    self._evaluate.append(CompanyOverviewLineInfo.from_alipay_dict(i))
    @property
    def financing(self):
        return self._financing

    @financing.setter
    def financing(self, value):
        if isinstance(value, list):
            self._financing = list()
            for i in value:
                if isinstance(i, CompanyOverviewLineInfo):
                    self._financing.append(i)
                else:
                    self._financing.append(CompanyOverviewLineInfo.from_alipay_dict(i))
    @property
    def management(self):
        return self._management

    @management.setter
    def management(self, value):
        if isinstance(value, list):
            self._management = list()
            for i in value:
                if isinstance(i, CompanyOverviewLineInfo):
                    self._management.append(i)
                else:
                    self._management.append(CompanyOverviewLineInfo.from_alipay_dict(i))
    @property
    def risk(self):
        return self._risk

    @risk.setter
    def risk(self, value):
        if isinstance(value, list):
            self._risk = list()
            for i in value:
                if isinstance(i, CompanyOverviewLineInfo):
                    self._risk.append(i)
                else:
                    self._risk.append(CompanyOverviewLineInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.assets:
            if isinstance(self.assets, list):
                for i in range(0, len(self.assets)):
                    element = self.assets[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.assets[i] = element.to_alipay_dict()
            if hasattr(self.assets, 'to_alipay_dict'):
                params['assets'] = self.assets.to_alipay_dict()
            else:
                params['assets'] = self.assets
        if self.background:
            if isinstance(self.background, list):
                for i in range(0, len(self.background)):
                    element = self.background[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.background[i] = element.to_alipay_dict()
            if hasattr(self.background, 'to_alipay_dict'):
                params['background'] = self.background.to_alipay_dict()
            else:
                params['background'] = self.background
        if self.evaluate:
            if isinstance(self.evaluate, list):
                for i in range(0, len(self.evaluate)):
                    element = self.evaluate[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.evaluate[i] = element.to_alipay_dict()
            if hasattr(self.evaluate, 'to_alipay_dict'):
                params['evaluate'] = self.evaluate.to_alipay_dict()
            else:
                params['evaluate'] = self.evaluate
        if self.financing:
            if isinstance(self.financing, list):
                for i in range(0, len(self.financing)):
                    element = self.financing[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.financing[i] = element.to_alipay_dict()
            if hasattr(self.financing, 'to_alipay_dict'):
                params['financing'] = self.financing.to_alipay_dict()
            else:
                params['financing'] = self.financing
        if self.management:
            if isinstance(self.management, list):
                for i in range(0, len(self.management)):
                    element = self.management[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.management[i] = element.to_alipay_dict()
            if hasattr(self.management, 'to_alipay_dict'):
                params['management'] = self.management.to_alipay_dict()
            else:
                params['management'] = self.management
        if self.risk:
            if isinstance(self.risk, list):
                for i in range(0, len(self.risk)):
                    element = self.risk[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk[i] = element.to_alipay_dict()
            if hasattr(self.risk, 'to_alipay_dict'):
                params['risk'] = self.risk.to_alipay_dict()
            else:
                params['risk'] = self.risk
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyOverviewInfo()
        if 'assets' in d:
            o.assets = d['assets']
        if 'background' in d:
            o.background = d['background']
        if 'evaluate' in d:
            o.evaluate = d['evaluate']
        if 'financing' in d:
            o.financing = d['financing']
        if 'management' in d:
            o.management = d['management']
        if 'risk' in d:
            o.risk = d['risk']
        return o


