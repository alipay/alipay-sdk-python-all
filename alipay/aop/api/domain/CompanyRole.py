#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpInfo import EpInfo
from alipay.aop.api.domain.EpInfo import EpInfo
from alipay.aop.api.domain.EpInfo import EpInfo


class CompanyRole(object):

    def __init__(self):
        self._ry_pos_fr_list = None
        self._ry_pos_sha_list = None
        self._share_holder_list = None

    @property
    def ry_pos_fr_list(self):
        return self._ry_pos_fr_list

    @ry_pos_fr_list.setter
    def ry_pos_fr_list(self, value):
        if isinstance(value, list):
            self._ry_pos_fr_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._ry_pos_fr_list.append(i)
                else:
                    self._ry_pos_fr_list.append(EpInfo.from_alipay_dict(i))
    @property
    def ry_pos_sha_list(self):
        return self._ry_pos_sha_list

    @ry_pos_sha_list.setter
    def ry_pos_sha_list(self, value):
        if isinstance(value, list):
            self._ry_pos_sha_list = list()
            for i in value:
                if isinstance(i, EpInfo):
                    self._ry_pos_sha_list.append(i)
                else:
                    self._ry_pos_sha_list.append(EpInfo.from_alipay_dict(i))
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
        if self.ry_pos_fr_list:
            if isinstance(self.ry_pos_fr_list, list):
                for i in range(0, len(self.ry_pos_fr_list)):
                    element = self.ry_pos_fr_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ry_pos_fr_list[i] = element.to_alipay_dict()
            if hasattr(self.ry_pos_fr_list, 'to_alipay_dict'):
                params['ry_pos_fr_list'] = self.ry_pos_fr_list.to_alipay_dict()
            else:
                params['ry_pos_fr_list'] = self.ry_pos_fr_list
        if self.ry_pos_sha_list:
            if isinstance(self.ry_pos_sha_list, list):
                for i in range(0, len(self.ry_pos_sha_list)):
                    element = self.ry_pos_sha_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ry_pos_sha_list[i] = element.to_alipay_dict()
            if hasattr(self.ry_pos_sha_list, 'to_alipay_dict'):
                params['ry_pos_sha_list'] = self.ry_pos_sha_list.to_alipay_dict()
            else:
                params['ry_pos_sha_list'] = self.ry_pos_sha_list
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
        o = CompanyRole()
        if 'ry_pos_fr_list' in d:
            o.ry_pos_fr_list = d['ry_pos_fr_list']
        if 'ry_pos_sha_list' in d:
            o.ry_pos_sha_list = d['ry_pos_sha_list']
        if 'share_holder_list' in d:
            o.share_holder_list = d['share_holder_list']
        return o


