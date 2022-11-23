#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCardMessageNotifyModel(object):

    def __init__(self):
        self._notify_info = None
        self._notify_no = None
        self._notify_type = None
        self._occur_time = None
        self._target_card_no = None
        self._target_card_no_type = None

    @property
    def notify_info(self):
        return self._notify_info

    @notify_info.setter
    def notify_info(self, value):
        self._notify_info = value
    @property
    def notify_no(self):
        return self._notify_no

    @notify_no.setter
    def notify_no(self, value):
        self._notify_no = value
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def occur_time(self):
        return self._occur_time

    @occur_time.setter
    def occur_time(self, value):
        self._occur_time = value
    @property
    def target_card_no(self):
        return self._target_card_no

    @target_card_no.setter
    def target_card_no(self, value):
        self._target_card_no = value
    @property
    def target_card_no_type(self):
        return self._target_card_no_type

    @target_card_no_type.setter
    def target_card_no_type(self, value):
        self._target_card_no_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.notify_info:
            if hasattr(self.notify_info, 'to_alipay_dict'):
                params['notify_info'] = self.notify_info.to_alipay_dict()
            else:
                params['notify_info'] = self.notify_info
        if self.notify_no:
            if hasattr(self.notify_no, 'to_alipay_dict'):
                params['notify_no'] = self.notify_no.to_alipay_dict()
            else:
                params['notify_no'] = self.notify_no
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.occur_time:
            if hasattr(self.occur_time, 'to_alipay_dict'):
                params['occur_time'] = self.occur_time.to_alipay_dict()
            else:
                params['occur_time'] = self.occur_time
        if self.target_card_no:
            if hasattr(self.target_card_no, 'to_alipay_dict'):
                params['target_card_no'] = self.target_card_no.to_alipay_dict()
            else:
                params['target_card_no'] = self.target_card_no
        if self.target_card_no_type:
            if hasattr(self.target_card_no_type, 'to_alipay_dict'):
                params['target_card_no_type'] = self.target_card_no_type.to_alipay_dict()
            else:
                params['target_card_no_type'] = self.target_card_no_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCardMessageNotifyModel()
        if 'notify_info' in d:
            o.notify_info = d['notify_info']
        if 'notify_no' in d:
            o.notify_no = d['notify_no']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'occur_time' in d:
            o.occur_time = d['occur_time']
        if 'target_card_no' in d:
            o.target_card_no = d['target_card_no']
        if 'target_card_no_type' in d:
            o.target_card_no_type = d['target_card_no_type']
        return o


