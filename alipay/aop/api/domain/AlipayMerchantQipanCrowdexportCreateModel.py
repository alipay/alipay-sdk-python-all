#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantQipanCrowdexportCreateModel(object):

    def __init__(self):
        self._crowd_code = None
        self._export_channel_type = None
        self._out_biz_no = None

    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def export_channel_type(self):
        return self._export_channel_type

    @export_channel_type.setter
    def export_channel_type(self, value):
        self._export_channel_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_code:
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.export_channel_type:
            if hasattr(self.export_channel_type, 'to_alipay_dict'):
                params['export_channel_type'] = self.export_channel_type.to_alipay_dict()
            else:
                params['export_channel_type'] = self.export_channel_type
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
        o = AlipayMerchantQipanCrowdexportCreateModel()
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'export_channel_type' in d:
            o.export_channel_type = d['export_channel_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


