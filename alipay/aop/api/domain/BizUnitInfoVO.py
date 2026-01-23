#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizUnitInfoVO(object):

    def __init__(self):
        self._biz_unit_id = None

    @property
    def biz_unit_id(self):
        return self._biz_unit_id

    @biz_unit_id.setter
    def biz_unit_id(self, value):
        self._biz_unit_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_unit_id:
            if hasattr(self.biz_unit_id, 'to_alipay_dict'):
                params['biz_unit_id'] = self.biz_unit_id.to_alipay_dict()
            else:
                params['biz_unit_id'] = self.biz_unit_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizUnitInfoVO()
        if 'biz_unit_id' in d:
            o.biz_unit_id = d['biz_unit_id']
        return o


