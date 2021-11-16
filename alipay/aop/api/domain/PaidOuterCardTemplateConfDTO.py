#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaidOuterCardCycleSellConfDTO import PaidOuterCardCycleSellConfDTO
from alipay.aop.api.domain.PaidOuterCardManageUrlConfDTO import PaidOuterCardManageUrlConfDTO
from alipay.aop.api.domain.PaidOuterCardSellingConfDTO import PaidOuterCardSellingConfDTO


class PaidOuterCardTemplateConfDTO(object):

    def __init__(self):
        self._cycle_selling_conf = None
        self._manage_url_conf = None
        self._open_selling_conf = None

    @property
    def cycle_selling_conf(self):
        return self._cycle_selling_conf

    @cycle_selling_conf.setter
    def cycle_selling_conf(self, value):
        if isinstance(value, PaidOuterCardCycleSellConfDTO):
            self._cycle_selling_conf = value
        else:
            self._cycle_selling_conf = PaidOuterCardCycleSellConfDTO.from_alipay_dict(value)
    @property
    def manage_url_conf(self):
        return self._manage_url_conf

    @manage_url_conf.setter
    def manage_url_conf(self, value):
        if isinstance(value, PaidOuterCardManageUrlConfDTO):
            self._manage_url_conf = value
        else:
            self._manage_url_conf = PaidOuterCardManageUrlConfDTO.from_alipay_dict(value)
    @property
    def open_selling_conf(self):
        return self._open_selling_conf

    @open_selling_conf.setter
    def open_selling_conf(self, value):
        if isinstance(value, PaidOuterCardSellingConfDTO):
            self._open_selling_conf = value
        else:
            self._open_selling_conf = PaidOuterCardSellingConfDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.cycle_selling_conf:
            if hasattr(self.cycle_selling_conf, 'to_alipay_dict'):
                params['cycle_selling_conf'] = self.cycle_selling_conf.to_alipay_dict()
            else:
                params['cycle_selling_conf'] = self.cycle_selling_conf
        if self.manage_url_conf:
            if hasattr(self.manage_url_conf, 'to_alipay_dict'):
                params['manage_url_conf'] = self.manage_url_conf.to_alipay_dict()
            else:
                params['manage_url_conf'] = self.manage_url_conf
        if self.open_selling_conf:
            if hasattr(self.open_selling_conf, 'to_alipay_dict'):
                params['open_selling_conf'] = self.open_selling_conf.to_alipay_dict()
            else:
                params['open_selling_conf'] = self.open_selling_conf
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaidOuterCardTemplateConfDTO()
        if 'cycle_selling_conf' in d:
            o.cycle_selling_conf = d['cycle_selling_conf']
        if 'manage_url_conf' in d:
            o.manage_url_conf = d['manage_url_conf']
        if 'open_selling_conf' in d:
            o.open_selling_conf = d['open_selling_conf']
        return o


