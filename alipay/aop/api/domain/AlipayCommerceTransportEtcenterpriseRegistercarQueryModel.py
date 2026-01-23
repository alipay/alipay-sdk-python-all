#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CarInfos import CarInfos


class AlipayCommerceTransportEtcenterpriseRegistercarQueryModel(object):

    def __init__(self):
        self._car_infos = None
        self._corp_id = None

    @property
    def car_infos(self):
        return self._car_infos

    @car_infos.setter
    def car_infos(self, value):
        if isinstance(value, list):
            self._car_infos = list()
            for i in value:
                if isinstance(i, CarInfos):
                    self._car_infos.append(i)
                else:
                    self._car_infos.append(CarInfos.from_alipay_dict(i))
    @property
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_infos:
            if isinstance(self.car_infos, list):
                for i in range(0, len(self.car_infos)):
                    element = self.car_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.car_infos[i] = element.to_alipay_dict()
            if hasattr(self.car_infos, 'to_alipay_dict'):
                params['car_infos'] = self.car_infos.to_alipay_dict()
            else:
                params['car_infos'] = self.car_infos
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcenterpriseRegistercarQueryModel()
        if 'car_infos' in d:
            o.car_infos = d['car_infos']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        return o


