#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryDetailPositionContentVO import DeliveryDetailPositionContentVO


class DeliveryDetailPositionVO(object):

    def __init__(self):
        self._position_code = None
        self._position_content = None

    @property
    def position_code(self):
        return self._position_code

    @position_code.setter
    def position_code(self, value):
        self._position_code = value
    @property
    def position_content(self):
        return self._position_content

    @position_content.setter
    def position_content(self, value):
        if isinstance(value, DeliveryDetailPositionContentVO):
            self._position_content = value
        else:
            self._position_content = DeliveryDetailPositionContentVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.position_code:
            if hasattr(self.position_code, 'to_alipay_dict'):
                params['position_code'] = self.position_code.to_alipay_dict()
            else:
                params['position_code'] = self.position_code
        if self.position_content:
            if hasattr(self.position_content, 'to_alipay_dict'):
                params['position_content'] = self.position_content.to_alipay_dict()
            else:
                params['position_content'] = self.position_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryDetailPositionVO()
        if 'position_code' in d:
            o.position_code = d['position_code']
        if 'position_content' in d:
            o.position_content = d['position_content']
        return o


