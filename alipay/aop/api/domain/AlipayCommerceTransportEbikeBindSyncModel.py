#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EbikeBindInfo import EbikeBindInfo


class AlipayCommerceTransportEbikeBindSyncModel(object):

    def __init__(self):
        self._ebike_bind_list = None
        self._ebike_source = None
        self._open_id = None
        self._user_id = None

    @property
    def ebike_bind_list(self):
        return self._ebike_bind_list

    @ebike_bind_list.setter
    def ebike_bind_list(self, value):
        if isinstance(value, list):
            self._ebike_bind_list = list()
            for i in value:
                if isinstance(i, EbikeBindInfo):
                    self._ebike_bind_list.append(i)
                else:
                    self._ebike_bind_list.append(EbikeBindInfo.from_alipay_dict(i))
    @property
    def ebike_source(self):
        return self._ebike_source

    @ebike_source.setter
    def ebike_source(self, value):
        self._ebike_source = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ebike_bind_list:
            if isinstance(self.ebike_bind_list, list):
                for i in range(0, len(self.ebike_bind_list)):
                    element = self.ebike_bind_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ebike_bind_list[i] = element.to_alipay_dict()
            if hasattr(self.ebike_bind_list, 'to_alipay_dict'):
                params['ebike_bind_list'] = self.ebike_bind_list.to_alipay_dict()
            else:
                params['ebike_bind_list'] = self.ebike_bind_list
        if self.ebike_source:
            if hasattr(self.ebike_source, 'to_alipay_dict'):
                params['ebike_source'] = self.ebike_source.to_alipay_dict()
            else:
                params['ebike_source'] = self.ebike_source
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEbikeBindSyncModel()
        if 'ebike_bind_list' in d:
            o.ebike_bind_list = d['ebike_bind_list']
        if 'ebike_source' in d:
            o.ebike_source = d['ebike_source']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


