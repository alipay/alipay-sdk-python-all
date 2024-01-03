#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantComplainGovernmentSubmitModel(object):

    def __init__(self):
        self._complain_event_id = None
        self._feedback_code = None
        self._feedback_content = None
        self._feedback_images = None
        self._operator = None

    @property
    def complain_event_id(self):
        return self._complain_event_id

    @complain_event_id.setter
    def complain_event_id(self, value):
        self._complain_event_id = value
    @property
    def feedback_code(self):
        return self._feedback_code

    @feedback_code.setter
    def feedback_code(self, value):
        self._feedback_code = value
    @property
    def feedback_content(self):
        return self._feedback_content

    @feedback_content.setter
    def feedback_content(self, value):
        self._feedback_content = value
    @property
    def feedback_images(self):
        return self._feedback_images

    @feedback_images.setter
    def feedback_images(self, value):
        self._feedback_images = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value


    def to_alipay_dict(self):
        params = dict()
        if self.complain_event_id:
            if hasattr(self.complain_event_id, 'to_alipay_dict'):
                params['complain_event_id'] = self.complain_event_id.to_alipay_dict()
            else:
                params['complain_event_id'] = self.complain_event_id
        if self.feedback_code:
            if hasattr(self.feedback_code, 'to_alipay_dict'):
                params['feedback_code'] = self.feedback_code.to_alipay_dict()
            else:
                params['feedback_code'] = self.feedback_code
        if self.feedback_content:
            if hasattr(self.feedback_content, 'to_alipay_dict'):
                params['feedback_content'] = self.feedback_content.to_alipay_dict()
            else:
                params['feedback_content'] = self.feedback_content
        if self.feedback_images:
            if hasattr(self.feedback_images, 'to_alipay_dict'):
                params['feedback_images'] = self.feedback_images.to_alipay_dict()
            else:
                params['feedback_images'] = self.feedback_images
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantComplainGovernmentSubmitModel()
        if 'complain_event_id' in d:
            o.complain_event_id = d['complain_event_id']
        if 'feedback_code' in d:
            o.feedback_code = d['feedback_code']
        if 'feedback_content' in d:
            o.feedback_content = d['feedback_content']
        if 'feedback_images' in d:
            o.feedback_images = d['feedback_images']
        if 'operator' in d:
            o.operator = d['operator']
        return o


