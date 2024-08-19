#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitQueryComponent(object):

    def __init__(self):
        self._channel = None
        self._latitude = None
        self._longitude = None
        self._skip_voucher_info = None
        self._source = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def skip_voucher_info(self):
        return self._skip_voucher_info

    @skip_voucher_info.setter
    def skip_voucher_info(self, value):
        self._skip_voucher_info = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.skip_voucher_info:
            if hasattr(self.skip_voucher_info, 'to_alipay_dict'):
                params['skip_voucher_info'] = self.skip_voucher_info.to_alipay_dict()
            else:
                params['skip_voucher_info'] = self.skip_voucher_info
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitQueryComponent()
        if 'channel' in d:
            o.channel = d['channel']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'skip_voucher_info' in d:
            o.skip_voucher_info = d['skip_voucher_info']
        if 'source' in d:
            o.source = d['source']
        return o


