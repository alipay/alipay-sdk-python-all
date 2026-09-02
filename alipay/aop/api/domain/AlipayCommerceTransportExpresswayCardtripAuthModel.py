#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportExpresswayCardtripAuthModel(object):

    def __init__(self):
        self._channel_isv_id = None
        self._channel_out_biz_no = None
        self._mobile_no = None
        self._plate_color = None
        self._plate_no = None

    @property
    def channel_isv_id(self):
        return self._channel_isv_id

    @channel_isv_id.setter
    def channel_isv_id(self, value):
        self._channel_isv_id = value
    @property
    def channel_out_biz_no(self):
        return self._channel_out_biz_no

    @channel_out_biz_no.setter
    def channel_out_biz_no(self, value):
        self._channel_out_biz_no = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_isv_id:
            if hasattr(self.channel_isv_id, 'to_alipay_dict'):
                params['channel_isv_id'] = self.channel_isv_id.to_alipay_dict()
            else:
                params['channel_isv_id'] = self.channel_isv_id
        if self.channel_out_biz_no:
            if hasattr(self.channel_out_biz_no, 'to_alipay_dict'):
                params['channel_out_biz_no'] = self.channel_out_biz_no.to_alipay_dict()
            else:
                params['channel_out_biz_no'] = self.channel_out_biz_no
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportExpresswayCardtripAuthModel()
        if 'channel_isv_id' in d:
            o.channel_isv_id = d['channel_isv_id']
        if 'channel_out_biz_no' in d:
            o.channel_out_biz_no = d['channel_out_biz_no']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        return o


