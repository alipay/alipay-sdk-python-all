#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantRelationEntity import MerchantRelationEntity


class AlipayTradeSettleDistributionrelationUnbindModel(object):

    def __init__(self):
        self._out_request_no = None
        self._receiver_list = None
        self._scene = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def receiver_list(self):
        return self._receiver_list

    @receiver_list.setter
    def receiver_list(self, value):
        if isinstance(value, list):
            self._receiver_list = list()
            for i in value:
                if isinstance(i, MerchantRelationEntity):
                    self._receiver_list.append(i)
                else:
                    self._receiver_list.append(MerchantRelationEntity.from_alipay_dict(i))
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.receiver_list:
            if isinstance(self.receiver_list, list):
                for i in range(0, len(self.receiver_list)):
                    element = self.receiver_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.receiver_list[i] = element.to_alipay_dict()
            if hasattr(self.receiver_list, 'to_alipay_dict'):
                params['receiver_list'] = self.receiver_list.to_alipay_dict()
            else:
                params['receiver_list'] = self.receiver_list
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSettleDistributionrelationUnbindModel()
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'receiver_list' in d:
            o.receiver_list = d['receiver_list']
        if 'scene' in d:
            o.scene = d['scene']
        return o


