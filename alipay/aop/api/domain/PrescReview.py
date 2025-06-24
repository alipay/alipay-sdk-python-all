#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrescReview(object):

    def __init__(self):
        self._pharmacist_name = None
        self._review_reject_note = None
        self._review_status = None
        self._review_time = None

    @property
    def pharmacist_name(self):
        return self._pharmacist_name

    @pharmacist_name.setter
    def pharmacist_name(self, value):
        self._pharmacist_name = value
    @property
    def review_reject_note(self):
        return self._review_reject_note

    @review_reject_note.setter
    def review_reject_note(self, value):
        self._review_reject_note = value
    @property
    def review_status(self):
        return self._review_status

    @review_status.setter
    def review_status(self, value):
        self._review_status = value
    @property
    def review_time(self):
        return self._review_time

    @review_time.setter
    def review_time(self, value):
        self._review_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.pharmacist_name:
            if hasattr(self.pharmacist_name, 'to_alipay_dict'):
                params['pharmacist_name'] = self.pharmacist_name.to_alipay_dict()
            else:
                params['pharmacist_name'] = self.pharmacist_name
        if self.review_reject_note:
            if hasattr(self.review_reject_note, 'to_alipay_dict'):
                params['review_reject_note'] = self.review_reject_note.to_alipay_dict()
            else:
                params['review_reject_note'] = self.review_reject_note
        if self.review_status:
            if hasattr(self.review_status, 'to_alipay_dict'):
                params['review_status'] = self.review_status.to_alipay_dict()
            else:
                params['review_status'] = self.review_status
        if self.review_time:
            if hasattr(self.review_time, 'to_alipay_dict'):
                params['review_time'] = self.review_time.to_alipay_dict()
            else:
                params['review_time'] = self.review_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrescReview()
        if 'pharmacist_name' in d:
            o.pharmacist_name = d['pharmacist_name']
        if 'review_reject_note' in d:
            o.review_reject_note = d['review_reject_note']
        if 'review_status' in d:
            o.review_status = d['review_status']
        if 'review_time' in d:
            o.review_time = d['review_time']
        return o


