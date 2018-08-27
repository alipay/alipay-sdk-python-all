#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpInfo import EpInfo
from alipay.aop.api.domain.EpInfo import EpInfo
from alipay.aop.api.domain.EpInfo import EpInfo
from alipay.aop.api.domain.EpInfo import EpInfo


class LawsuitPersonRecord(object):

    def __init__(self):
        self._bgt_list = None
        self._cpws_list = None
        self._sxgg_list = None
        self._zxgg_list = None

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
        o = LawsuitPersonRecord()
        if 'bgt_list' in d:
            o.bgt_list = d['bgt_list']
        if 'cpws_list' in d:
            o.cpws_list = d['cpws_list']
        if 'sxgg_list' in d:
            o.sxgg_list = d['sxgg_list']
        if 'zxgg_list' in d:
            o.zxgg_list = d['zxgg_list']
        return o


