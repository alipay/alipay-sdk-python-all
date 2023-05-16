#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryPositionContentVO import DeliveryPositionContentVO


class DeliveryPositionVO(object):

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
        if isinstance(value, list):
            self._position_content = list()
            for i in value:
                if isinstance(i, DeliveryPositionContentVO):
                    self._position_content.append(i)
                else:
                    self._position_content.append(DeliveryPositionContentVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.position_code:
            if hasattr(self.position_code, 'to_alipay_dict'):
                params['position_code'] = self.position_code.to_alipay_dict()
            else:
                params['position_code'] = self.position_code
        if self.position_content:
            if isinstance(self.position_content, list):
                for i in range(0, len(self.position_content)):
                    element = self.position_content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.position_content[i] = element.to_alipay_dict()
            if hasattr(self.position_content, 'to_alipay_dict'):
                params['position_content'] = self.position_content.to_alipay_dict()
            else:
                params['position_content'] = self.position_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryPositionVO()
        if 'position_code' in d:
            o.position_code = d['position_code']
        if 'position_content' in d:
            o.position_content = d['position_content']
        return o


