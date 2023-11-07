#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceComplaintReplySubmitModel(object):

    def __init__(self):
        self._complaint_id = None
        self._merchant_pid = None
        self._reply_content = None

    @property
    def complaint_id(self):
        return self._complaint_id

    @complaint_id.setter
    def complaint_id(self, value):
        self._complaint_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def reply_content(self):
        return self._reply_content

    @reply_content.setter
    def reply_content(self, value):
        self._reply_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.complaint_id:
            if hasattr(self.complaint_id, 'to_alipay_dict'):
                params['complaint_id'] = self.complaint_id.to_alipay_dict()
            else:
                params['complaint_id'] = self.complaint_id
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.reply_content:
            if hasattr(self.reply_content, 'to_alipay_dict'):
                params['reply_content'] = self.reply_content.to_alipay_dict()
            else:
                params['reply_content'] = self.reply_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceComplaintReplySubmitModel()
        if 'complaint_id' in d:
            o.complaint_id = d['complaint_id']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'reply_content' in d:
            o.reply_content = d['reply_content']
        return o


