#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderExpoCheckplaceModifyModel(object):

    def __init__(self):
        self._activity_code = None
        self._card_edge_bg_image = None
        self._card_edge_image = None
        self._card_name = None
        self._card_url = None
        self._check_place_type = None
        self._device_sn = None
        self._external_place_mark = None
        self._place_id = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def card_edge_bg_image(self):
        return self._card_edge_bg_image

    @card_edge_bg_image.setter
    def card_edge_bg_image(self, value):
        self._card_edge_bg_image = value
    @property
    def card_edge_image(self):
        return self._card_edge_image

    @card_edge_image.setter
    def card_edge_image(self, value):
        self._card_edge_image = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_url(self):
        return self._card_url

    @card_url.setter
    def card_url(self, value):
        self._card_url = value
    @property
    def check_place_type(self):
        return self._check_place_type

    @check_place_type.setter
    def check_place_type(self, value):
        self._check_place_type = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def external_place_mark(self):
        return self._external_place_mark

    @external_place_mark.setter
    def external_place_mark(self, value):
        self._external_place_mark = value
    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        self._place_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.card_edge_bg_image:
            if hasattr(self.card_edge_bg_image, 'to_alipay_dict'):
                params['card_edge_bg_image'] = self.card_edge_bg_image.to_alipay_dict()
            else:
                params['card_edge_bg_image'] = self.card_edge_bg_image
        if self.card_edge_image:
            if hasattr(self.card_edge_image, 'to_alipay_dict'):
                params['card_edge_image'] = self.card_edge_image.to_alipay_dict()
            else:
                params['card_edge_image'] = self.card_edge_image
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.card_url:
            if hasattr(self.card_url, 'to_alipay_dict'):
                params['card_url'] = self.card_url.to_alipay_dict()
            else:
                params['card_url'] = self.card_url
        if self.check_place_type:
            if hasattr(self.check_place_type, 'to_alipay_dict'):
                params['check_place_type'] = self.check_place_type.to_alipay_dict()
            else:
                params['check_place_type'] = self.check_place_type
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.external_place_mark:
            if hasattr(self.external_place_mark, 'to_alipay_dict'):
                params['external_place_mark'] = self.external_place_mark.to_alipay_dict()
            else:
                params['external_place_mark'] = self.external_place_mark
        if self.place_id:
            if hasattr(self.place_id, 'to_alipay_dict'):
                params['place_id'] = self.place_id.to_alipay_dict()
            else:
                params['place_id'] = self.place_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderExpoCheckplaceModifyModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'card_edge_bg_image' in d:
            o.card_edge_bg_image = d['card_edge_bg_image']
        if 'card_edge_image' in d:
            o.card_edge_image = d['card_edge_image']
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'card_url' in d:
            o.card_url = d['card_url']
        if 'check_place_type' in d:
            o.check_place_type = d['check_place_type']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'external_place_mark' in d:
            o.external_place_mark = d['external_place_mark']
        if 'place_id' in d:
            o.place_id = d['place_id']
        return o


