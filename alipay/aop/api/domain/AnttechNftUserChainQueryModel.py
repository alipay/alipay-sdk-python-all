#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftUserChainQueryModel(object):

    def __init__(self):
        self._fans_id = None
        self._fans_id_type = None

    @property
    def fans_id(self):
        return self._fans_id

    @fans_id.setter
    def fans_id(self, value):
        self._fans_id = value
    @property
    def fans_id_type(self):
        return self._fans_id_type

    @fans_id_type.setter
    def fans_id_type(self, value):
        self._fans_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.fans_id:
            if hasattr(self.fans_id, 'to_alipay_dict'):
                params['fans_id'] = self.fans_id.to_alipay_dict()
            else:
                params['fans_id'] = self.fans_id
        if self.fans_id_type:
            if hasattr(self.fans_id_type, 'to_alipay_dict'):
                params['fans_id_type'] = self.fans_id_type.to_alipay_dict()
            else:
                params['fans_id_type'] = self.fans_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftUserChainQueryModel()
        if 'fans_id' in d:
            o.fans_id = d['fans_id']
        if 'fans_id_type' in d:
            o.fans_id_type = d['fans_id_type']
        return o


