#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsCompany import InsCompany


class AlipayInsSceneEmploymentProductOrderModel(object):

    def __init__(self):
        self._channel = None
        self._merchant = None
        self._out_biz_no = None
        self._recom_flow_no_list = None
        self._scene_code = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def merchant(self):
        return self._merchant

    @merchant.setter
    def merchant(self, value):
        if isinstance(value, InsCompany):
            self._merchant = value
        else:
            self._merchant = InsCompany.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def recom_flow_no_list(self):
        return self._recom_flow_no_list

    @recom_flow_no_list.setter
    def recom_flow_no_list(self, value):
        if isinstance(value, list):
            self._recom_flow_no_list = list()
            for i in value:
                self._recom_flow_no_list.append(i)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.merchant:
            if hasattr(self.merchant, 'to_alipay_dict'):
                params['merchant'] = self.merchant.to_alipay_dict()
            else:
                params['merchant'] = self.merchant
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.recom_flow_no_list:
            if isinstance(self.recom_flow_no_list, list):
                for i in range(0, len(self.recom_flow_no_list)):
                    element = self.recom_flow_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.recom_flow_no_list[i] = element.to_alipay_dict()
            if hasattr(self.recom_flow_no_list, 'to_alipay_dict'):
                params['recom_flow_no_list'] = self.recom_flow_no_list.to_alipay_dict()
            else:
                params['recom_flow_no_list'] = self.recom_flow_no_list
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneEmploymentProductOrderModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'merchant' in d:
            o.merchant = d['merchant']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'recom_flow_no_list' in d:
            o.recom_flow_no_list = d['recom_flow_no_list']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


