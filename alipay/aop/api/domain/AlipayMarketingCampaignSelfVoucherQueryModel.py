#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignSelfVoucherQueryModel(object):

    def __init__(self):
        self._scene_code = None
        self._voucher_id = None

    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        if isinstance(value, list):
            self._scene_code = list()
            for i in value:
                self._scene_code.append(i)
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene_code:
            if isinstance(self.scene_code, list):
                for i in range(0, len(self.scene_code)):
                    element = self.scene_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_code[i] = element.to_alipay_dict()
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignSelfVoucherQueryModel()
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


