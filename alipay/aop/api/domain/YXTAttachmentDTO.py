#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YXTAttachmentDTO(object):

    def __init__(self):
        self._attachment_id = None
        self._attachment_name = None
        self._duration = None
        self._sort = None

    @property
    def attachment_id(self):
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, value):
        self._attachment_id = value
    @property
    def attachment_name(self):
        return self._attachment_name

    @attachment_name.setter
    def attachment_name(self, value):
        self._attachment_name = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_id:
            if hasattr(self.attachment_id, 'to_alipay_dict'):
                params['attachment_id'] = self.attachment_id.to_alipay_dict()
            else:
                params['attachment_id'] = self.attachment_id
        if self.attachment_name:
            if hasattr(self.attachment_name, 'to_alipay_dict'):
                params['attachment_name'] = self.attachment_name.to_alipay_dict()
            else:
                params['attachment_name'] = self.attachment_name
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YXTAttachmentDTO()
        if 'attachment_id' in d:
            o.attachment_id = d['attachment_id']
        if 'attachment_name' in d:
            o.attachment_name = d['attachment_name']
        if 'duration' in d:
            o.duration = d['duration']
        if 'sort' in d:
            o.sort = d['sort']
        return o


