#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndrISVReceiptApplyDTO import IndrISVReceiptApplyDTO


class AlipayOverseasOpenIndrreceiptApplyModel(object):

    def __init__(self):
        self._apply_receipt_list = None
        self._scene_type = None

    @property
    def apply_receipt_list(self):
        return self._apply_receipt_list

    @apply_receipt_list.setter
    def apply_receipt_list(self, value):
        if isinstance(value, list):
            self._apply_receipt_list = list()
            for i in value:
                if isinstance(i, IndrISVReceiptApplyDTO):
                    self._apply_receipt_list.append(i)
                else:
                    self._apply_receipt_list.append(IndrISVReceiptApplyDTO.from_alipay_dict(i))
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_receipt_list:
            if isinstance(self.apply_receipt_list, list):
                for i in range(0, len(self.apply_receipt_list)):
                    element = self.apply_receipt_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_receipt_list[i] = element.to_alipay_dict()
            if hasattr(self.apply_receipt_list, 'to_alipay_dict'):
                params['apply_receipt_list'] = self.apply_receipt_list.to_alipay_dict()
            else:
                params['apply_receipt_list'] = self.apply_receipt_list
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenIndrreceiptApplyModel()
        if 'apply_receipt_list' in d:
            o.apply_receipt_list = d['apply_receipt_list']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


