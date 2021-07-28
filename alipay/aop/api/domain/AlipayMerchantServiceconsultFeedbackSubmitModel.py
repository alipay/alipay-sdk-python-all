#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantServiceconsultFeedbackSubmitModel(object):

    def __init__(self):
        self._consult_event_id = None
        self._reply_content = None
        self._reply_images = None

    @property
    def consult_event_id(self):
        return self._consult_event_id

    @consult_event_id.setter
    def consult_event_id(self, value):
        self._consult_event_id = value
    @property
    def reply_content(self):
        return self._reply_content

    @reply_content.setter
    def reply_content(self, value):
        self._reply_content = value
    @property
    def reply_images(self):
        return self._reply_images

    @reply_images.setter
    def reply_images(self, value):
        self._reply_images = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_event_id:
            if hasattr(self.consult_event_id, 'to_alipay_dict'):
                params['consult_event_id'] = self.consult_event_id.to_alipay_dict()
            else:
                params['consult_event_id'] = self.consult_event_id
        if self.reply_content:
            if hasattr(self.reply_content, 'to_alipay_dict'):
                params['reply_content'] = self.reply_content.to_alipay_dict()
            else:
                params['reply_content'] = self.reply_content
        if self.reply_images:
            if hasattr(self.reply_images, 'to_alipay_dict'):
                params['reply_images'] = self.reply_images.to_alipay_dict()
            else:
                params['reply_images'] = self.reply_images
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantServiceconsultFeedbackSubmitModel()
        if 'consult_event_id' in d:
            o.consult_event_id = d['consult_event_id']
        if 'reply_content' in d:
            o.reply_content = d['reply_content']
        if 'reply_images' in d:
            o.reply_images = d['reply_images']
        return o


