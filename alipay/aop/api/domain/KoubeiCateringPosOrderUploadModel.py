#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PosDeviceInfoVO import PosDeviceInfoVO
from alipay.aop.api.domain.PosOrderInfoVO import PosOrderInfoVO


class KoubeiCateringPosOrderUploadModel(object):

    def __init__(self):
        self._pos_device_infos = None
        self._pos_order_infos = None
        self._source_type = None

    @property
    def pos_device_infos(self):
        return self._pos_device_infos

    @pos_device_infos.setter
    def pos_device_infos(self, value):
        if isinstance(value, list):
            self._pos_device_infos = list()
            for i in value:
                if isinstance(i, PosDeviceInfoVO):
                    self._pos_device_infos.append(i)
                else:
                    self._pos_device_infos.append(PosDeviceInfoVO.from_alipay_dict(i))
    @property
    def pos_order_infos(self):
        return self._pos_order_infos

    @pos_order_infos.setter
    def pos_order_infos(self, value):
        if isinstance(value, list):
            self._pos_order_infos = list()
            for i in value:
                if isinstance(i, PosOrderInfoVO):
                    self._pos_order_infos.append(i)
                else:
                    self._pos_order_infos.append(PosOrderInfoVO.from_alipay_dict(i))
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.pos_device_infos:
            if isinstance(self.pos_device_infos, list):
                for i in range(0, len(self.pos_device_infos)):
                    element = self.pos_device_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pos_device_infos[i] = element.to_alipay_dict()
            if hasattr(self.pos_device_infos, 'to_alipay_dict'):
                params['pos_device_infos'] = self.pos_device_infos.to_alipay_dict()
            else:
                params['pos_device_infos'] = self.pos_device_infos
        if self.pos_order_infos:
            if isinstance(self.pos_order_infos, list):
                for i in range(0, len(self.pos_order_infos)):
                    element = self.pos_order_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pos_order_infos[i] = element.to_alipay_dict()
            if hasattr(self.pos_order_infos, 'to_alipay_dict'):
                params['pos_order_infos'] = self.pos_order_infos.to_alipay_dict()
            else:
                params['pos_order_infos'] = self.pos_order_infos
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosOrderUploadModel()
        if 'pos_device_infos' in d:
            o.pos_device_infos = d['pos_device_infos']
        if 'pos_order_infos' in d:
            o.pos_order_infos = d['pos_order_infos']
        if 'source_type' in d:
            o.source_type = d['source_type']
        return o


