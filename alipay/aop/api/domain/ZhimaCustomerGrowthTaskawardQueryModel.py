#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerGrowthTaskawardQueryModel(object):

    def __init__(self):
        self._behavior_id = None
        self._havana_user_id = None
        self._out_biz_no = None

    @property
    def behavior_id(self):
        return self._behavior_id

    @behavior_id.setter
    def behavior_id(self, value):
        self._behavior_id = value
    @property
    def havana_user_id(self):
        return self._havana_user_id

    @havana_user_id.setter
    def havana_user_id(self, value):
        self._havana_user_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.behavior_id:
            if hasattr(self.behavior_id, 'to_alipay_dict'):
                params['behavior_id'] = self.behavior_id.to_alipay_dict()
            else:
                params['behavior_id'] = self.behavior_id
        if self.havana_user_id:
            if hasattr(self.havana_user_id, 'to_alipay_dict'):
                params['havana_user_id'] = self.havana_user_id.to_alipay_dict()
            else:
                params['havana_user_id'] = self.havana_user_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerGrowthTaskawardQueryModel()
        if 'behavior_id' in d:
            o.behavior_id = d['behavior_id']
        if 'havana_user_id' in d:
            o.havana_user_id = d['havana_user_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


