#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateWhiteuserAddModel(object):

    def __init__(self):
        self._inst_id = None
        self._roster_id = None
        self._white_type_id = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def roster_id(self):
        return self._roster_id

    @roster_id.setter
    def roster_id(self, value):
        self._roster_id = value
    @property
    def white_type_id(self):
        return self._white_type_id

    @white_type_id.setter
    def white_type_id(self, value):
        if isinstance(value, list):
            self._white_type_id = list()
            for i in value:
                self._white_type_id.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.roster_id:
            if hasattr(self.roster_id, 'to_alipay_dict'):
                params['roster_id'] = self.roster_id.to_alipay_dict()
            else:
                params['roster_id'] = self.roster_id
        if self.white_type_id:
            if isinstance(self.white_type_id, list):
                for i in range(0, len(self.white_type_id)):
                    element = self.white_type_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.white_type_id[i] = element.to_alipay_dict()
            if hasattr(self.white_type_id, 'to_alipay_dict'):
                params['white_type_id'] = self.white_type_id.to_alipay_dict()
            else:
                params['white_type_id'] = self.white_type_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateWhiteuserAddModel()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'roster_id' in d:
            o.roster_id = d['roster_id']
        if 'white_type_id' in d:
            o.white_type_id = d['white_type_id']
        return o


