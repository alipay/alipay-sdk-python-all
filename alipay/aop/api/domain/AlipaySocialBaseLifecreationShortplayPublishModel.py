#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShortPlayCopyrightMaterial import ShortPlayCopyrightMaterial


class AlipaySocialBaseLifecreationShortplayPublishModel(object):

    def __init__(self):
        self._album_id = None
        self._broadcast_record_number = None
        self._channels = None
        self._copyright_material = None
        self._public_id = None

    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, value):
        self._album_id = value
    @property
    def broadcast_record_number(self):
        return self._broadcast_record_number

    @broadcast_record_number.setter
    def broadcast_record_number(self, value):
        self._broadcast_record_number = value
    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, value):
        if isinstance(value, list):
            self._channels = list()
            for i in value:
                self._channels.append(i)
    @property
    def copyright_material(self):
        return self._copyright_material

    @copyright_material.setter
    def copyright_material(self, value):
        if isinstance(value, ShortPlayCopyrightMaterial):
            self._copyright_material = value
        else:
            self._copyright_material = ShortPlayCopyrightMaterial.from_alipay_dict(value)
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.album_id:
            if hasattr(self.album_id, 'to_alipay_dict'):
                params['album_id'] = self.album_id.to_alipay_dict()
            else:
                params['album_id'] = self.album_id
        if self.broadcast_record_number:
            if hasattr(self.broadcast_record_number, 'to_alipay_dict'):
                params['broadcast_record_number'] = self.broadcast_record_number.to_alipay_dict()
            else:
                params['broadcast_record_number'] = self.broadcast_record_number
        if self.channels:
            if isinstance(self.channels, list):
                for i in range(0, len(self.channels)):
                    element = self.channels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channels[i] = element.to_alipay_dict()
            if hasattr(self.channels, 'to_alipay_dict'):
                params['channels'] = self.channels.to_alipay_dict()
            else:
                params['channels'] = self.channels
        if self.copyright_material:
            if hasattr(self.copyright_material, 'to_alipay_dict'):
                params['copyright_material'] = self.copyright_material.to_alipay_dict()
            else:
                params['copyright_material'] = self.copyright_material
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseLifecreationShortplayPublishModel()
        if 'album_id' in d:
            o.album_id = d['album_id']
        if 'broadcast_record_number' in d:
            o.broadcast_record_number = d['broadcast_record_number']
        if 'channels' in d:
            o.channels = d['channels']
        if 'copyright_material' in d:
            o.copyright_material = d['copyright_material']
        if 'public_id' in d:
            o.public_id = d['public_id']
        return o


