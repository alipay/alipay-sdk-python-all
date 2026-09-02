#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalSfpartnerQueryModel(object):

    def __init__(self):
        self._ep_name = None
        self._ep_name_keyword = None

    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def ep_name_keyword(self):
        return self._ep_name_keyword

    @ep_name_keyword.setter
    def ep_name_keyword(self, value):
        self._ep_name_keyword = value


    def to_alipay_dict(self):
        params = dict()
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.ep_name_keyword:
            if hasattr(self.ep_name_keyword, 'to_alipay_dict'):
                params['ep_name_keyword'] = self.ep_name_keyword.to_alipay_dict()
            else:
                params['ep_name_keyword'] = self.ep_name_keyword
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfpartnerQueryModel()
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'ep_name_keyword' in d:
            o.ep_name_keyword = d['ep_name_keyword']
        return o


