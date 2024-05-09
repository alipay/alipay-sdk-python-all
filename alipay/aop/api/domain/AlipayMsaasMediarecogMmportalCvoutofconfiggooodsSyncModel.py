#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OutOfConfigGoodsResult import OutOfConfigGoodsResult


class AlipayMsaasMediarecogMmportalCvoutofconfiggooodsSyncModel(object):

    def __init__(self):
        self._device_id = None
        self._out_of_config_goods = None
        self._transaction_id = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def out_of_config_goods(self):
        return self._out_of_config_goods

    @out_of_config_goods.setter
    def out_of_config_goods(self, value):
        if isinstance(value, list):
            self._out_of_config_goods = list()
            for i in value:
                if isinstance(i, OutOfConfigGoodsResult):
                    self._out_of_config_goods.append(i)
                else:
                    self._out_of_config_goods.append(OutOfConfigGoodsResult.from_alipay_dict(i))
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.out_of_config_goods:
            if isinstance(self.out_of_config_goods, list):
                for i in range(0, len(self.out_of_config_goods)):
                    element = self.out_of_config_goods[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_of_config_goods[i] = element.to_alipay_dict()
            if hasattr(self.out_of_config_goods, 'to_alipay_dict'):
                params['out_of_config_goods'] = self.out_of_config_goods.to_alipay_dict()
            else:
                params['out_of_config_goods'] = self.out_of_config_goods
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmportalCvoutofconfiggooodsSyncModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'out_of_config_goods' in d:
            o.out_of_config_goods = d['out_of_config_goods']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


