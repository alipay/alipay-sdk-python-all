#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayMarketingIbsInfo import AlipayMarketingIbsInfo


class AlipayMarketingExtData(object):

    def __init__(self):
        self._lbs_info = None
        self._out_user_id = None

    @property
    def lbs_info(self):
        return self._lbs_info

    @lbs_info.setter
    def lbs_info(self, value):
        if isinstance(value, AlipayMarketingIbsInfo):
            self._lbs_info = value
        else:
            self._lbs_info = AlipayMarketingIbsInfo.from_alipay_dict(value)
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.lbs_info:
            if hasattr(self.lbs_info, 'to_alipay_dict'):
                params['lbs_info'] = self.lbs_info.to_alipay_dict()
            else:
                params['lbs_info'] = self.lbs_info
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingExtData()
        if 'lbs_info' in d:
            o.lbs_info = d['lbs_info']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        return o


