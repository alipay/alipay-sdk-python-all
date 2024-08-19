#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitRight import BenefitRight


class BenefitRewardInfo(object):

    def __init__(self):
        self._id = None
        self._out_right_id = None
        self._right_list = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def out_right_id(self):
        return self._out_right_id

    @out_right_id.setter
    def out_right_id(self, value):
        self._out_right_id = value
    @property
    def right_list(self):
        return self._right_list

    @right_list.setter
    def right_list(self, value):
        if isinstance(value, list):
            self._right_list = list()
            for i in value:
                if isinstance(i, BenefitRight):
                    self._right_list.append(i)
                else:
                    self._right_list.append(BenefitRight.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.out_right_id:
            if hasattr(self.out_right_id, 'to_alipay_dict'):
                params['out_right_id'] = self.out_right_id.to_alipay_dict()
            else:
                params['out_right_id'] = self.out_right_id
        if self.right_list:
            if isinstance(self.right_list, list):
                for i in range(0, len(self.right_list)):
                    element = self.right_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.right_list[i] = element.to_alipay_dict()
            if hasattr(self.right_list, 'to_alipay_dict'):
                params['right_list'] = self.right_list.to_alipay_dict()
            else:
                params['right_list'] = self.right_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitRewardInfo()
        if 'id' in d:
            o.id = d['id']
        if 'out_right_id' in d:
            o.out_right_id = d['out_right_id']
        if 'right_list' in d:
            o.right_list = d['right_list']
        return o


