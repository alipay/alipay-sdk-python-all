#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DistLogisticsInfoDTO(object):

    def __init__(self):
        self._express_comp_name = None
        self._express_no = None

    @property
    def express_comp_name(self):
        return self._express_comp_name

    @express_comp_name.setter
    def express_comp_name(self, value):
        self._express_comp_name = value
    @property
    def express_no(self):
        return self._express_no

    @express_no.setter
    def express_no(self, value):
        self._express_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.express_comp_name:
            if hasattr(self.express_comp_name, 'to_alipay_dict'):
                params['express_comp_name'] = self.express_comp_name.to_alipay_dict()
            else:
                params['express_comp_name'] = self.express_comp_name
        if self.express_no:
            if hasattr(self.express_no, 'to_alipay_dict'):
                params['express_no'] = self.express_no.to_alipay_dict()
            else:
                params['express_no'] = self.express_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DistLogisticsInfoDTO()
        if 'express_comp_name' in d:
            o.express_comp_name = d['express_comp_name']
        if 'express_no' in d:
            o.express_no = d['express_no']
        return o


