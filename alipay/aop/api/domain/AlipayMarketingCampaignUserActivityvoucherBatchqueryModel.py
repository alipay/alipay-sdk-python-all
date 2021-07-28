#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignUserActivityvoucherBatchqueryModel(object):

    def __init__(self):
        self._scene_code = None
        self._voucher_status = None

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
    def voucher_status(self):
        return self._voucher_status

    @voucher_status.setter
    def voucher_status(self, value):
        self._voucher_status = value


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
        if self.voucher_status:
            if hasattr(self.voucher_status, 'to_alipay_dict'):
                params['voucher_status'] = self.voucher_status.to_alipay_dict()
            else:
                params['voucher_status'] = self.voucher_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignUserActivityvoucherBatchqueryModel()
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'voucher_status' in d:
            o.voucher_status = d['voucher_status']
        return o


