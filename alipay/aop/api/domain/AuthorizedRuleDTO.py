#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthorizeDetailDTO import AuthorizeDetailDTO


class AuthorizedRuleDTO(object):

    def __init__(self):
        self._authorized_detail_list = None
        self._authorized_type = None

    @property
    def authorized_detail_list(self):
        return self._authorized_detail_list

    @authorized_detail_list.setter
    def authorized_detail_list(self, value):
        if isinstance(value, list):
            self._authorized_detail_list = list()
            for i in value:
                if isinstance(i, AuthorizeDetailDTO):
                    self._authorized_detail_list.append(i)
                else:
                    self._authorized_detail_list.append(AuthorizeDetailDTO.from_alipay_dict(i))
    @property
    def authorized_type(self):
        return self._authorized_type

    @authorized_type.setter
    def authorized_type(self, value):
        self._authorized_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorized_detail_list:
            if isinstance(self.authorized_detail_list, list):
                for i in range(0, len(self.authorized_detail_list)):
                    element = self.authorized_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.authorized_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.authorized_detail_list, 'to_alipay_dict'):
                params['authorized_detail_list'] = self.authorized_detail_list.to_alipay_dict()
            else:
                params['authorized_detail_list'] = self.authorized_detail_list
        if self.authorized_type:
            if hasattr(self.authorized_type, 'to_alipay_dict'):
                params['authorized_type'] = self.authorized_type.to_alipay_dict()
            else:
                params['authorized_type'] = self.authorized_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthorizedRuleDTO()
        if 'authorized_detail_list' in d:
            o.authorized_detail_list = d['authorized_detail_list']
        if 'authorized_type' in d:
            o.authorized_type = d['authorized_type']
        return o


