#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaidOuterCardCycleInfoDTO(object):

    def __init__(self):
        self._alipay_deduct_agreement = None
        self._alipay_deduct_product_code = None
        self._alipay_deduct_scene = None
        self._close_reason = None
        self._cycle_type = None
        self._open_status = None

    @property
    def alipay_deduct_agreement(self):
        return self._alipay_deduct_agreement

    @alipay_deduct_agreement.setter
    def alipay_deduct_agreement(self, value):
        self._alipay_deduct_agreement = value
    @property
    def alipay_deduct_product_code(self):
        return self._alipay_deduct_product_code

    @alipay_deduct_product_code.setter
    def alipay_deduct_product_code(self, value):
        self._alipay_deduct_product_code = value
    @property
    def alipay_deduct_scene(self):
        return self._alipay_deduct_scene

    @alipay_deduct_scene.setter
    def alipay_deduct_scene(self, value):
        self._alipay_deduct_scene = value
    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
    @property
    def cycle_type(self):
        return self._cycle_type

    @cycle_type.setter
    def cycle_type(self, value):
        self._cycle_type = value
    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_deduct_agreement:
            if hasattr(self.alipay_deduct_agreement, 'to_alipay_dict'):
                params['alipay_deduct_agreement'] = self.alipay_deduct_agreement.to_alipay_dict()
            else:
                params['alipay_deduct_agreement'] = self.alipay_deduct_agreement
        if self.alipay_deduct_product_code:
            if hasattr(self.alipay_deduct_product_code, 'to_alipay_dict'):
                params['alipay_deduct_product_code'] = self.alipay_deduct_product_code.to_alipay_dict()
            else:
                params['alipay_deduct_product_code'] = self.alipay_deduct_product_code
        if self.alipay_deduct_scene:
            if hasattr(self.alipay_deduct_scene, 'to_alipay_dict'):
                params['alipay_deduct_scene'] = self.alipay_deduct_scene.to_alipay_dict()
            else:
                params['alipay_deduct_scene'] = self.alipay_deduct_scene
        if self.close_reason:
            if hasattr(self.close_reason, 'to_alipay_dict'):
                params['close_reason'] = self.close_reason.to_alipay_dict()
            else:
                params['close_reason'] = self.close_reason
        if self.cycle_type:
            if hasattr(self.cycle_type, 'to_alipay_dict'):
                params['cycle_type'] = self.cycle_type.to_alipay_dict()
            else:
                params['cycle_type'] = self.cycle_type
        if self.open_status:
            if hasattr(self.open_status, 'to_alipay_dict'):
                params['open_status'] = self.open_status.to_alipay_dict()
            else:
                params['open_status'] = self.open_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaidOuterCardCycleInfoDTO()
        if 'alipay_deduct_agreement' in d:
            o.alipay_deduct_agreement = d['alipay_deduct_agreement']
        if 'alipay_deduct_product_code' in d:
            o.alipay_deduct_product_code = d['alipay_deduct_product_code']
        if 'alipay_deduct_scene' in d:
            o.alipay_deduct_scene = d['alipay_deduct_scene']
        if 'close_reason' in d:
            o.close_reason = d['close_reason']
        if 'cycle_type' in d:
            o.cycle_type = d['cycle_type']
        if 'open_status' in d:
            o.open_status = d['open_status']
        return o


