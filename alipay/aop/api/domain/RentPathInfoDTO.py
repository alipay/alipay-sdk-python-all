#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentServiceProtocolDTO import RentServiceProtocolDTO


class RentPathInfoDTO(object):

    def __init__(self):
        self._buyout_path = None
        self._detail_path = None
        self._protocols = None
        self._relet_path = None
        self._return_path = None

    @property
    def buyout_path(self):
        return self._buyout_path

    @buyout_path.setter
    def buyout_path(self, value):
        self._buyout_path = value
    @property
    def detail_path(self):
        return self._detail_path

    @detail_path.setter
    def detail_path(self, value):
        self._detail_path = value
    @property
    def protocols(self):
        return self._protocols

    @protocols.setter
    def protocols(self, value):
        if isinstance(value, list):
            self._protocols = list()
            for i in value:
                if isinstance(i, RentServiceProtocolDTO):
                    self._protocols.append(i)
                else:
                    self._protocols.append(RentServiceProtocolDTO.from_alipay_dict(i))
    @property
    def relet_path(self):
        return self._relet_path

    @relet_path.setter
    def relet_path(self, value):
        self._relet_path = value
    @property
    def return_path(self):
        return self._return_path

    @return_path.setter
    def return_path(self, value):
        self._return_path = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyout_path:
            if hasattr(self.buyout_path, 'to_alipay_dict'):
                params['buyout_path'] = self.buyout_path.to_alipay_dict()
            else:
                params['buyout_path'] = self.buyout_path
        if self.detail_path:
            if hasattr(self.detail_path, 'to_alipay_dict'):
                params['detail_path'] = self.detail_path.to_alipay_dict()
            else:
                params['detail_path'] = self.detail_path
        if self.protocols:
            if isinstance(self.protocols, list):
                for i in range(0, len(self.protocols)):
                    element = self.protocols[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.protocols[i] = element.to_alipay_dict()
            if hasattr(self.protocols, 'to_alipay_dict'):
                params['protocols'] = self.protocols.to_alipay_dict()
            else:
                params['protocols'] = self.protocols
        if self.relet_path:
            if hasattr(self.relet_path, 'to_alipay_dict'):
                params['relet_path'] = self.relet_path.to_alipay_dict()
            else:
                params['relet_path'] = self.relet_path
        if self.return_path:
            if hasattr(self.return_path, 'to_alipay_dict'):
                params['return_path'] = self.return_path.to_alipay_dict()
            else:
                params['return_path'] = self.return_path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentPathInfoDTO()
        if 'buyout_path' in d:
            o.buyout_path = d['buyout_path']
        if 'detail_path' in d:
            o.detail_path = d['detail_path']
        if 'protocols' in d:
            o.protocols = d['protocols']
        if 'relet_path' in d:
            o.relet_path = d['relet_path']
        if 'return_path' in d:
            o.return_path = d['return_path']
        return o


