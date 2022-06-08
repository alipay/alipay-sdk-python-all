#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessRelationAttachmentInfo(object):

    def __init__(self):
        self._attachment_type = None
        self._image_id = None
        self._invalid_time = None
        self._valid_time = None

    @property
    def attachment_type(self):
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, value):
        self._attachment_type = value
    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def invalid_time(self):
        return self._invalid_time

    @invalid_time.setter
    def invalid_time(self, value):
        self._invalid_time = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_type:
            if hasattr(self.attachment_type, 'to_alipay_dict'):
                params['attachment_type'] = self.attachment_type.to_alipay_dict()
            else:
                params['attachment_type'] = self.attachment_type
        if self.image_id:
            if hasattr(self.image_id, 'to_alipay_dict'):
                params['image_id'] = self.image_id.to_alipay_dict()
            else:
                params['image_id'] = self.image_id
        if self.invalid_time:
            if hasattr(self.invalid_time, 'to_alipay_dict'):
                params['invalid_time'] = self.invalid_time.to_alipay_dict()
            else:
                params['invalid_time'] = self.invalid_time
        if self.valid_time:
            if hasattr(self.valid_time, 'to_alipay_dict'):
                params['valid_time'] = self.valid_time.to_alipay_dict()
            else:
                params['valid_time'] = self.valid_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessRelationAttachmentInfo()
        if 'attachment_type' in d:
            o.attachment_type = d['attachment_type']
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'invalid_time' in d:
            o.invalid_time = d['invalid_time']
        if 'valid_time' in d:
            o.valid_time = d['valid_time']
        return o


