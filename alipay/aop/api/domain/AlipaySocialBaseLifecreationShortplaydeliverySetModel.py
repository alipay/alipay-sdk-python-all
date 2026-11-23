#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseLifecreationShortplaydeliverySetModel(object):

    def __init__(self):
        self._album_id = None
        self._channel = None
        self._iaa_free_count = None
        self._merchant_album_id = None

    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, value):
        self._album_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def iaa_free_count(self):
        return self._iaa_free_count

    @iaa_free_count.setter
    def iaa_free_count(self, value):
        self._iaa_free_count = value
    @property
    def merchant_album_id(self):
        return self._merchant_album_id

    @merchant_album_id.setter
    def merchant_album_id(self, value):
        self._merchant_album_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.album_id:
            if hasattr(self.album_id, 'to_alipay_dict'):
                params['album_id'] = self.album_id.to_alipay_dict()
            else:
                params['album_id'] = self.album_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.iaa_free_count:
            if hasattr(self.iaa_free_count, 'to_alipay_dict'):
                params['iaa_free_count'] = self.iaa_free_count.to_alipay_dict()
            else:
                params['iaa_free_count'] = self.iaa_free_count
        if self.merchant_album_id:
            if hasattr(self.merchant_album_id, 'to_alipay_dict'):
                params['merchant_album_id'] = self.merchant_album_id.to_alipay_dict()
            else:
                params['merchant_album_id'] = self.merchant_album_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseLifecreationShortplaydeliverySetModel()
        if 'album_id' in d:
            o.album_id = d['album_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'iaa_free_count' in d:
            o.iaa_free_count = d['iaa_free_count']
        if 'merchant_album_id' in d:
            o.merchant_album_id = d['merchant_album_id']
        return o


