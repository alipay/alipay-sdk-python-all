#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpInfo import EpInfo
from alipay.aop.api.domain.EpInfo import EpInfo
from alipay.aop.api.domain.EpInfo import EpInfo
from alipay.aop.api.domain.EpInfo import EpInfo
from alipay.aop.api.domain.EpInfo import EpInfo
from alipay.aop.api.domain.EpInfo import EpInfo
from alipay.aop.api.domain.EpInfo import EpInfo


class LawsuitRecord(object):

    def __init__(self):
        self._ajlc_list = None
        self._bgt_list = None
        self._cpws_list = None
        self._fygg_list = None
        self._ktgg_list = None
        self._sxgg_list = None
        self._zxgg_list = None

    @property
    def ajlc_list(self):
        return self._ajlc_list

    @ajlc_list.setter
    def ajlc_list(self, value):
        if isinstance(value, list):
            self._ajlc_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._ajlc_list.append(i)
                else:
                    self._ajlc_list.append(EpInfo.from_alipay_dict(i))
    @property
    def bgt_list(self):
        return self._bgt_list

    @bgt_list.setter
    def bgt_list(self, value):
        if isinstance(value, list):
            self._bgt_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._bgt_list.append(i)
                else:
                    self._bgt_list.append(EpInfo.from_alipay_dict(i))
    @property
    def cpws_list(self):
        return self._cpws_list

    @cpws_list.setter
    def cpws_list(self, value):
        if isinstance(value, list):
            self._cpws_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._cpws_list.append(i)
                else:
                    self._cpws_list.append(EpInfo.from_alipay_dict(i))
    @property
    def fygg_list(self):
        return self._fygg_list

    @fygg_list.setter
    def fygg_list(self, value):
        if isinstance(value, list):
            self._fygg_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._fygg_list.append(i)
                else:
                    self._fygg_list.append(EpInfo.from_alipay_dict(i))
    @property
    def ktgg_list(self):
        return self._ktgg_list

    @ktgg_list.setter
    def ktgg_list(self, value):
        if isinstance(value, list):
            self._ktgg_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._ktgg_list.append(i)
                else:
                    self._ktgg_list.append(EpInfo.from_alipay_dict(i))
    @property
    def sxgg_list(self):
        return self._sxgg_list

    @sxgg_list.setter
    def sxgg_list(self, value):
        if isinstance(value, list):
            self._sxgg_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._sxgg_list.append(i)
                else:
                    self._sxgg_list.append(EpInfo.from_alipay_dict(i))
    @property
    def zxgg_list(self):
        return self._zxgg_list

    @zxgg_list.setter
    def zxgg_list(self, value):
        if isinstance(value, list):
            self._zxgg_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._zxgg_list.append(i)
                else:
                    self._zxgg_list.append(EpInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ajlc_list:
            if isinstance(self.ajlc_list, list):
                for i in range(0, len(self.ajlc_list)):
                    element = self.ajlc_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ajlc_list[i] = element.to_alipay_dict()
            if hasattr(self.ajlc_list, 'to_alipay_dict'):
                params['ajlc_list'] = self.ajlc_list.to_alipay_dict()
            else:
                params['ajlc_list'] = self.ajlc_list
        if self.bgt_list:
            if isinstance(self.bgt_list, list):
                for i in range(0, len(self.bgt_list)):
                    element = self.bgt_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bgt_list[i] = element.to_alipay_dict()
            if hasattr(self.bgt_list, 'to_alipay_dict'):
                params['bgt_list'] = self.bgt_list.to_alipay_dict()
            else:
                params['bgt_list'] = self.bgt_list
        if self.cpws_list:
            if isinstance(self.cpws_list, list):
                for i in range(0, len(self.cpws_list)):
                    element = self.cpws_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cpws_list[i] = element.to_alipay_dict()
            if hasattr(self.cpws_list, 'to_alipay_dict'):
                params['cpws_list'] = self.cpws_list.to_alipay_dict()
            else:
                params['cpws_list'] = self.cpws_list
        if self.fygg_list:
            if isinstance(self.fygg_list, list):
                for i in range(0, len(self.fygg_list)):
                    element = self.fygg_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fygg_list[i] = element.to_alipay_dict()
            if hasattr(self.fygg_list, 'to_alipay_dict'):
                params['fygg_list'] = self.fygg_list.to_alipay_dict()
            else:
                params['fygg_list'] = self.fygg_list
        if self.ktgg_list:
            if isinstance(self.ktgg_list, list):
                for i in range(0, len(self.ktgg_list)):
                    element = self.ktgg_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ktgg_list[i] = element.to_alipay_dict()
            if hasattr(self.ktgg_list, 'to_alipay_dict'):
                params['ktgg_list'] = self.ktgg_list.to_alipay_dict()
            else:
                params['ktgg_list'] = self.ktgg_list
        if self.sxgg_list:
            if isinstance(self.sxgg_list, list):
                for i in range(0, len(self.sxgg_list)):
                    element = self.sxgg_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sxgg_list[i] = element.to_alipay_dict()
            if hasattr(self.sxgg_list, 'to_alipay_dict'):
                params['sxgg_list'] = self.sxgg_list.to_alipay_dict()
            else:
                params['sxgg_list'] = self.sxgg_list
        if self.zxgg_list:
            if isinstance(self.zxgg_list, list):
                for i in range(0, len(self.zxgg_list)):
                    element = self.zxgg_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.zxgg_list[i] = element.to_alipay_dict()
            if hasattr(self.zxgg_list, 'to_alipay_dict'):
                params['zxgg_list'] = self.zxgg_list.to_alipay_dict()
            else:
                params['zxgg_list'] = self.zxgg_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LawsuitRecord()
        if 'ajlc_list' in d:
            o.ajlc_list = d['ajlc_list']
        if 'bgt_list' in d:
            o.bgt_list = d['bgt_list']
        if 'cpws_list' in d:
            o.cpws_list = d['cpws_list']
        if 'fygg_list' in d:
            o.fygg_list = d['fygg_list']
        if 'ktgg_list' in d:
            o.ktgg_list = d['ktgg_list']
        if 'sxgg_list' in d:
            o.sxgg_list = d['sxgg_list']
        if 'zxgg_list' in d:
            o.zxgg_list = d['zxgg_list']
        return o


