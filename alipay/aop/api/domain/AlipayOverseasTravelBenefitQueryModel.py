#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelBenefitQueryModel(object):

    def __init__(self):
        self._sync_out_biz_no = None

    @property
    def sync_out_biz_no(self):
        return self._sync_out_biz_no

    @sync_out_biz_no.setter
    def sync_out_biz_no(self, value):
        self._sync_out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.sync_out_biz_no:
            if hasattr(self.sync_out_biz_no, 'to_alipay_dict'):
                params['sync_out_biz_no'] = self.sync_out_biz_no.to_alipay_dict()
            else:
                params['sync_out_biz_no'] = self.sync_out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelBenefitQueryModel()
        if 'sync_out_biz_no' in d:
            o.sync_out_biz_no = d['sync_out_biz_no']
        return o


