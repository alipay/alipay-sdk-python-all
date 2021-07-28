#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishVirtualCatetorySimplifyInfo import KbdishVirtualCatetorySimplifyInfo


class KbdishVirtualShopSimplifyInfo(object):

    def __init__(self):
        self._catetory_list = None
        self._out_shop_id = None
        self._shop_id = None

    @property
    def catetory_list(self):
        return self._catetory_list

    @catetory_list.setter
    def catetory_list(self, value):
        if isinstance(value, list):
            self._catetory_list = list()
            for i in value:
                if isinstance(i, KbdishVirtualCatetorySimplifyInfo):
                    self._catetory_list.append(i)
                else:
                    self._catetory_list.append(KbdishVirtualCatetorySimplifyInfo.from_alipay_dict(i))
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.catetory_list:
            if isinstance(self.catetory_list, list):
                for i in range(0, len(self.catetory_list)):
                    element = self.catetory_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.catetory_list[i] = element.to_alipay_dict()
            if hasattr(self.catetory_list, 'to_alipay_dict'):
                params['catetory_list'] = self.catetory_list.to_alipay_dict()
            else:
                params['catetory_list'] = self.catetory_list
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishVirtualShopSimplifyInfo()
        if 'catetory_list' in d:
            o.catetory_list = d['catetory_list']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


