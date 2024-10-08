#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreateMaterialsInfo import CreateMaterialsInfo


class AlipayOpenSpNordermaterialsapplyMaterialsCreateModel(object):

    def __init__(self):
        self._apply_id = None
        self._materials_info = None
        self._shop_order_no = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def materials_info(self):
        return self._materials_info

    @materials_info.setter
    def materials_info(self, value):
        if isinstance(value, list):
            self._materials_info = list()
            for i in value:
                if isinstance(i, CreateMaterialsInfo):
                    self._materials_info.append(i)
                else:
                    self._materials_info.append(CreateMaterialsInfo.from_alipay_dict(i))
    @property
    def shop_order_no(self):
        return self._shop_order_no

    @shop_order_no.setter
    def shop_order_no(self, value):
        self._shop_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.materials_info:
            if isinstance(self.materials_info, list):
                for i in range(0, len(self.materials_info)):
                    element = self.materials_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.materials_info[i] = element.to_alipay_dict()
            if hasattr(self.materials_info, 'to_alipay_dict'):
                params['materials_info'] = self.materials_info.to_alipay_dict()
            else:
                params['materials_info'] = self.materials_info
        if self.shop_order_no:
            if hasattr(self.shop_order_no, 'to_alipay_dict'):
                params['shop_order_no'] = self.shop_order_no.to_alipay_dict()
            else:
                params['shop_order_no'] = self.shop_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordermaterialsapplyMaterialsCreateModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'materials_info' in d:
            o.materials_info = d['materials_info']
        if 'shop_order_no' in d:
            o.shop_order_no = d['shop_order_no']
        return o


