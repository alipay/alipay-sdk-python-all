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
from alipay.aop.api.domain.EpInfo import EpInfo


class CompanyInfo(object):

    def __init__(self):
        self._alter_list = None
        self._basic_info = None
        self._case_info_list = None
        self._entinv_list = None
        self._fr_position_list = None
        self._frinv_list = None
        self._person_list = None
        self._share_holder_list = None

    @property
    def alter_list(self):
        return self._alter_list

    @alter_list.setter
    def alter_list(self, value):
        if isinstance(value, list):
            self._alter_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._alter_list.append(i)
                else:
                    self._alter_list.append(EpInfo.from_alipay_dict(i))
    @property
    def basic_info(self):
        return self._basic_info

    @basic_info.setter
    def basic_info(self, value):
        if isinstance(value, EpInfo):
            self._basic_info = value
        else:
            self._basic_info = EpInfo.from_alipay_dict(value)
    @property
    def case_info_list(self):
        return self._case_info_list

    @case_info_list.setter
    def case_info_list(self, value):
        if isinstance(value, list):
            self._case_info_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._case_info_list.append(i)
                else:
                    self._case_info_list.append(EpInfo.from_alipay_dict(i))
    @property
    def entinv_list(self):
        return self._entinv_list

    @entinv_list.setter
    def entinv_list(self, value):
        if isinstance(value, list):
            self._entinv_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._entinv_list.append(i)
                else:
                    self._entinv_list.append(EpInfo.from_alipay_dict(i))
    @property
    def fr_position_list(self):
        return self._fr_position_list

    @fr_position_list.setter
    def fr_position_list(self, value):
        if isinstance(value, list):
            self._fr_position_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._fr_position_list.append(i)
                else:
                    self._fr_position_list.append(EpInfo.from_alipay_dict(i))
    @property
    def frinv_list(self):
        return self._frinv_list

    @frinv_list.setter
    def frinv_list(self, value):
        if isinstance(value, list):
            self._frinv_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._frinv_list.append(i)
                else:
                    self._frinv_list.append(EpInfo.from_alipay_dict(i))
    @property
    def person_list(self):
        return self._person_list

    @person_list.setter
    def person_list(self, value):
        if isinstance(value, list):
            self._person_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._person_list.append(i)
                else:
                    self._person_list.append(EpInfo.from_alipay_dict(i))
    @property
    def share_holder_list(self):
        return self._share_holder_list

    @share_holder_list.setter
    def share_holder_list(self, value):
        if isinstance(value, list):
            self._share_holder_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._share_holder_list.append(i)
                else:
                    self._share_holder_list.append(EpInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.alter_list:
            if isinstance(self.alter_list, list):
                for i in range(0, len(self.alter_list)):
                    element = self.alter_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.alter_list[i] = element.to_alipay_dict()
            if hasattr(self.alter_list, 'to_alipay_dict'):
                params['alter_list'] = self.alter_list.to_alipay_dict()
            else:
                params['alter_list'] = self.alter_list
        if self.basic_info:
            if hasattr(self.basic_info, 'to_alipay_dict'):
                params['basic_info'] = self.basic_info.to_alipay_dict()
            else:
                params['basic_info'] = self.basic_info
        if self.case_info_list:
            if isinstance(self.case_info_list, list):
                for i in range(0, len(self.case_info_list)):
                    element = self.case_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.case_info_list[i] = element.to_alipay_dict()
            if hasattr(self.case_info_list, 'to_alipay_dict'):
                params['case_info_list'] = self.case_info_list.to_alipay_dict()
            else:
                params['case_info_list'] = self.case_info_list
        if self.entinv_list:
            if isinstance(self.entinv_list, list):
                for i in range(0, len(self.entinv_list)):
                    element = self.entinv_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.entinv_list[i] = element.to_alipay_dict()
            if hasattr(self.entinv_list, 'to_alipay_dict'):
                params['entinv_list'] = self.entinv_list.to_alipay_dict()
            else:
                params['entinv_list'] = self.entinv_list
        if self.fr_position_list:
            if isinstance(self.fr_position_list, list):
                for i in range(0, len(self.fr_position_list)):
                    element = self.fr_position_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fr_position_list[i] = element.to_alipay_dict()
            if hasattr(self.fr_position_list, 'to_alipay_dict'):
                params['fr_position_list'] = self.fr_position_list.to_alipay_dict()
            else:
                params['fr_position_list'] = self.fr_position_list
        if self.frinv_list:
            if isinstance(self.frinv_list, list):
                for i in range(0, len(self.frinv_list)):
                    element = self.frinv_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.frinv_list[i] = element.to_alipay_dict()
            if hasattr(self.frinv_list, 'to_alipay_dict'):
                params['frinv_list'] = self.frinv_list.to_alipay_dict()
            else:
                params['frinv_list'] = self.frinv_list
        if self.person_list:
            if isinstance(self.person_list, list):
                for i in range(0, len(self.person_list)):
                    element = self.person_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.person_list[i] = element.to_alipay_dict()
            if hasattr(self.person_list, 'to_alipay_dict'):
                params['person_list'] = self.person_list.to_alipay_dict()
            else:
                params['person_list'] = self.person_list
        if self.share_holder_list:
            if isinstance(self.share_holder_list, list):
                for i in range(0, len(self.share_holder_list)):
                    element = self.share_holder_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.share_holder_list[i] = element.to_alipay_dict()
            if hasattr(self.share_holder_list, 'to_alipay_dict'):
                params['share_holder_list'] = self.share_holder_list.to_alipay_dict()
            else:
                params['share_holder_list'] = self.share_holder_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyInfo()
        if 'alter_list' in d:
            o.alter_list = d['alter_list']
        if 'basic_info' in d:
            o.basic_info = d['basic_info']
        if 'case_info_list' in d:
            o.case_info_list = d['case_info_list']
        if 'entinv_list' in d:
            o.entinv_list = d['entinv_list']
        if 'fr_position_list' in d:
            o.fr_position_list = d['fr_position_list']
        if 'frinv_list' in d:
            o.frinv_list = d['frinv_list']
        if 'person_list' in d:
            o.person_list = d['person_list']
        if 'share_holder_list' in d:
            o.share_holder_list = d['share_holder_list']
        return o


