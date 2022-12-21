#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AiPictureVO(object):

    def __init__(self):
        self._image_id = None
        self._sec_status = None

    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def sec_status(self):
        return self._sec_status

    @sec_status.setter
    def sec_status(self, value):
        self._sec_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_id:
            if hasattr(self.image_id, 'to_alipay_dict'):
                params['image_id'] = self.image_id.to_alipay_dict()
            else:
                params['image_id'] = self.image_id
        if self.sec_status:
            if hasattr(self.sec_status, 'to_alipay_dict'):
                params['sec_status'] = self.sec_status.to_alipay_dict()
            else:
                params['sec_status'] = self.sec_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AiPictureVO()
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'sec_status' in d:
            o.sec_status = d['sec_status']
        return o


