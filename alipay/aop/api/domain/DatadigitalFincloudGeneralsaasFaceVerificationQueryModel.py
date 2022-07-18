#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudGeneralsaasFaceVerificationQueryModel(object):

    def __init__(self):
        self._certify_id = None
        self._need_alive_photo = None

    @property
    def certify_id(self):
        return self._certify_id

    @certify_id.setter
    def certify_id(self, value):
        self._certify_id = value
    @property
    def need_alive_photo(self):
        return self._need_alive_photo

    @need_alive_photo.setter
    def need_alive_photo(self, value):
        self._need_alive_photo = value


    def to_alipay_dict(self):
        params = dict()
        if self.certify_id:
            if hasattr(self.certify_id, 'to_alipay_dict'):
                params['certify_id'] = self.certify_id.to_alipay_dict()
            else:
                params['certify_id'] = self.certify_id
        if self.need_alive_photo:
            if hasattr(self.need_alive_photo, 'to_alipay_dict'):
                params['need_alive_photo'] = self.need_alive_photo.to_alipay_dict()
            else:
                params['need_alive_photo'] = self.need_alive_photo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudGeneralsaasFaceVerificationQueryModel()
        if 'certify_id' in d:
            o.certify_id = d['certify_id']
        if 'need_alive_photo' in d:
            o.need_alive_photo = d['need_alive_photo']
        return o


