#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcOrderExtInfo import EcOrderExtInfo


class EcOrderGoodsInfo(object):

    def __init__(self):
        self._ext_info = None
        self._goods_name = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, EcOrderExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(EcOrderExtInfo.from_alipay_dict(i))
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcOrderGoodsInfo()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        return o


