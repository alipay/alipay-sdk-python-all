#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessItem import BusinessItem


class AlipayEcoMycarParkingParkinglotbizTransferModel(object):

    def __init__(self):
        self._business_isv = None
        self._parking_id = None

    @property
    def business_isv(self):
        return self._business_isv

    @business_isv.setter
    def business_isv(self, value):
        if isinstance(value, list):
            self._business_isv = list()
            for i in value:
                if isinstance(i, BusinessItem):
                    self._business_isv.append(i)
                else:
                    self._business_isv.append(BusinessItem.from_alipay_dict(i))
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_isv:
            if isinstance(self.business_isv, list):
                for i in range(0, len(self.business_isv)):
                    element = self.business_isv[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_isv[i] = element.to_alipay_dict()
            if hasattr(self.business_isv, 'to_alipay_dict'):
                params['business_isv'] = self.business_isv.to_alipay_dict()
            else:
                params['business_isv'] = self.business_isv
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingParkinglotbizTransferModel()
        if 'business_isv' in d:
            o.business_isv = d['business_isv']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        return o


